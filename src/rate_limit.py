from __future__ import annotations

import os
import threading
import time
from collections import deque


class RateLimiter:
    """Sliding 60s window: enforces TPM (tokens/min) and RPM (requests/min)."""

    def __init__(self, tpm: int, rpm: int) -> None:
        self.tpm = tpm
        self.rpm = rpm
        self.tokens: deque[tuple[float, int]] = deque()
        self.requests: deque[float] = deque()
        self.cv = threading.Condition()

    def _prune(self, now: float) -> None:
        cutoff = now - 60.0
        while self.tokens and self.tokens[0][0] < cutoff:
            self.tokens.popleft()
        while self.requests and self.requests[0] < cutoff:
            self.requests.popleft()

    def acquire(self, estimated_tokens: int) -> None:
        estimated_tokens = max(1, int(estimated_tokens))
        with self.cv:
            while True:
                now = time.time()
                self._prune(now)
                used = sum(n for _, n in self.tokens)
                wait = 0.0
                if used + estimated_tokens > self.tpm and self.tokens:
                    wait = max(wait, 60.0 - (now - self.tokens[0][0]) + 0.05)
                if len(self.requests) + 1 > self.rpm and self.requests:
                    wait = max(wait, 60.0 - (now - self.requests[0]) + 0.05)
                if wait <= 0:
                    self.tokens.append((now, estimated_tokens))
                    self.requests.append(now)
                    return
                self.cv.wait(timeout=min(wait, 5.0))

    def reconcile(self, actual_tokens: int) -> None:
        """Replace last estimate with actual usage from response."""
        if actual_tokens <= 0:
            return
        with self.cv:
            if self.tokens:
                ts, _ = self.tokens.pop()
                self.tokens.append((ts, int(actual_tokens)))
                self.cv.notify_all()


_LIMITERS: dict[str, RateLimiter] = {}
_LOCK = threading.Lock()

DEFAULT_TPM = {
    "OPENAI": 180_000,
    "ANTHROPIC": 180_000,
    "OPENROUTER": 1_000_000,
}
DEFAULT_RPM = {
    "OPENAI": 450,
    "ANTHROPIC": 450,
    "OPENROUTER": 1000,
}


def get_limiter(provider: str) -> RateLimiter:
    """Per-provider limiter, configurable via {PROVIDER}_TPM / {PROVIDER}_RPM."""
    key = provider.upper()
    with _LOCK:
        if key not in _LIMITERS:
            tpm = int(os.environ.get(f"{key}_TPM", DEFAULT_TPM.get(key, 180_000)))
            rpm = int(os.environ.get(f"{key}_RPM", DEFAULT_RPM.get(key, 450)))
            _LIMITERS[key] = RateLimiter(tpm, rpm)
        return _LIMITERS[key]


def estimate_tokens(*texts: str) -> int:
    """Cheap heuristic: 1 token ≈ 4 chars. Plus 512 buffer for completion."""
    chars = sum(len(t) for t in texts if t)
    return chars // 4 + 512
