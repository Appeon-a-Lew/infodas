from __future__ import annotations

import hashlib
import os
import pickle
import sys
from pathlib import Path
from typing import Literal

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Requirement

QUERY_EMB_CACHE_DIR = Path(os.environ.get("QUERY_EMB_CACHE_DIR", ".cache/query_emb"))


def _query_text(q: Requirement) -> str:
    return f"query: {q.title}. {q.text[:500]}"


def _text_hash(model_name: str, text: str) -> str:
    h = hashlib.sha256()
    h.update(model_name.encode("utf-8"))
    h.update(b"\x00")
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def _precompute_with_cache(model, queries: list[Requirement], model_name: str) -> dict:
    """Encode query embeddings, reusing disk cache for unchanged texts."""
    safe = model_name.replace("/", "_")
    cache_file = QUERY_EMB_CACHE_DIR / f"{safe}.pkl"
    cache: dict[str, "np.ndarray"] = {}
    if cache_file.exists():
        try:
            with open(cache_file, "rb") as f:
                cache = pickle.load(f)
        except Exception:
            cache = {}

    texts = [_text_hash(model_name, _query_text(q)) for q in queries]
    missing_idx = [i for i, h in enumerate(texts) if h not in cache]

    if missing_idx:
        print(
            f"[i] query-emb cache: {len(queries) - len(missing_idx)} hit, {len(missing_idx)} miss; encoding ...",
            file=sys.stderr,
        )
        to_encode = [_query_text(queries[i]) for i in missing_idx]
        new_embs = model.encode(
            to_encode,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,
            batch_size=32,
        )
        for j, i in enumerate(missing_idx):
            cache[texts[i]] = new_embs[j]
        QUERY_EMB_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        tmp = cache_file.with_suffix(".tmp")
        with open(tmp, "wb") as f:
            pickle.dump(cache, f, protocol=pickle.HIGHEST_PROTOCOL)
        tmp.replace(cache_file)
    else:
        print(f"[i] query-emb cache: all {len(queries)} hit, no encode needed", file=sys.stderr)

    return {q.id: cache[texts[i]] for i, q in enumerate(queries)}

GERMAN_STOPWORDS = {
    "aber","alle","allem","allen","aller","alles","als","also","am","an","ander","andere","anderem",
    "anderen","anderer","anderes","anderm","andern","anders","auch","auf","aus","bei","bin","bis",
    "bist","da","damit","dann","der","den","des","dem","die","das","dass","daß","derselbe","derselben",
    "denselben","desselben","demselben","dieselbe","dieselben","dasselbe","dazu","dein","deine","deinem",
    "deinen","deiner","deines","denn","derer","dessen","dich","dir","du","dies","diese","diesem","diesen",
    "dieser","dieses","doch","dort","durch","ein","eine","einem","einen","einer","eines","einig","einige",
    "einigem","einigen","einiger","einiges","einmal","er","ihn","ihm","es","etwas","euer","eure","eurem",
    "euren","eurer","eures","für","gegen","gewesen","hab","habe","haben","hat","hatte","hatten","hier",
    "hin","hinter","ich","mich","mir","ihr","ihre","ihrem","ihren","ihrer","ihres","euch","im","in",
    "indem","ins","ist","jede","jedem","jeden","jeder","jedes","jene","jenem","jenen","jener","jenes",
    "jetzt","kann","kein","keine","keinem","keinen","keiner","keines","können","könnte","machen","man",
    "manche","manchem","manchen","mancher","manches","mein","meine","meinem","meinen","meiner","meines",
    "mit","muss","musste","nach","nicht","nichts","noch","nun","nur","ob","oder","ohne","sehr","sein",
    "seine","seinem","seinen","seiner","seines","selbst","sich","sie","ihnen","sind","so","solche",
    "solchem","solchen","solcher","solches","soll","sollte","sondern","sonst","über","um","und","uns",
    "unse","unsem","unsen","unser","unses","unter","viel","vom","von","vor","während","war","waren",
    "warst","was","weg","weil","weiter","welche","welchem","welchen","welcher","welches","wenn","werde",
    "werden","wie","wieder","will","wir","wird","wirst","wo","wollen","wollte","würde","würden","zu",
    "zum","zur","zwar","zwischen",
}


class TfidfShortlister:
    """Original TF-IDF based shortlister (fast, lightweight)."""
    
    def __init__(self, corpus: list[Requirement], ngram_range: tuple[int, int] = (1, 2)) -> None:
        self.corpus = corpus
        self.vectorizer = TfidfVectorizer(
            stop_words=list(GERMAN_STOPWORDS),
            ngram_range=ngram_range,
            min_df=1,
            sublinear_tf=True,
        )
        self.matrix = self.vectorizer.fit_transform(self._doc(r) for r in corpus)

    @staticmethod
    def _doc(r: Requirement) -> str:
        return f"{r.title}\n{r.text}"

    def top_k(self, query: Requirement, k: int = 15) -> list[tuple[Requirement, float]]:
        qv = self.vectorizer.transform([self._doc(query)])
        sims = cosine_similarity(qv, self.matrix).ravel()
        idx = sims.argsort()[::-1][:k]
        return [(self.corpus[i], float(sims[i])) for i in idx]


class EmbeddingShortlister:
    """Semantic embedding-based shortlister using sentence-transformers.
    
    Requires: pip install sentence-transformers
    
    Recommended models for German:
    - "Sahajtomar/German-semantic" (German-specific)
    - "intfloat/multilingual-e5-large" (multilingual, better quality)
    - "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2" (fast, multilingual)
    """
    
    def __init__(
        self,
        corpus: list[Requirement],
        model_name: str = "intfloat/multilingual-e5-large",
        device: str = "cpu",
    ) -> None:
        from sentence_transformers import SentenceTransformer
        
        self.corpus = corpus
        self.model_name = model_name
        self.model = SentenceTransformer(model_name, device=device)

        # Pre-compute embeddings for corpus (this takes time but makes queries fast)
        print(f"[i] Computing embeddings for {len(corpus)} requirements using {model_name}...")
        self.embeddings = self.model.encode(
            [self._doc(r) for r in corpus],
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,  # Normalize for cosine similarity
        )
        print(f"[i] Embeddings computed: {self.embeddings.shape}")

    @staticmethod
    def _doc(r: Requirement) -> str:
        # E5 models expect "query:" or "passage:" prefix
        return f"passage: {r.title}. {r.text[:500]}"  # Truncate long texts

    def top_k(self, query: Requirement, k: int = 15) -> list[tuple[Requirement, float]]:
        from sentence_transformers.util import cos_sim

        cached = getattr(self, "_query_emb", {}).get(query.id)
        if cached is not None:
            query_embedding = cached
        else:
            query_embedding = self.model.encode(
                f"query: {query.title}. {query.text[:500]}",
                normalize_embeddings=True,
            )

        similarities = cos_sim(query_embedding, self.embeddings)[0]
        top_indices = similarities.argsort(descending=True)[:k]
        return [(self.corpus[i], float(similarities[i])) for i in top_indices]

    def precompute_queries(self, queries: list[Requirement]) -> None:
        self._query_emb = _precompute_with_cache(self.model, queries, model_name=getattr(self, "model_name", type(self.model).__name__))


class CachedEmbeddingShortlister:
    """Embedding shortlister with disk caching for faster reloads."""
    
    def __init__(
        self,
        corpus: list[Requirement],
        model_name: str = "intfloat/multilingual-e5-large",
        cache_dir: str = ".cache",
        device: str = "cpu",
    ) -> None:
        from sentence_transformers import SentenceTransformer
        import numpy as np
        from pathlib import Path
        
        self.corpus = corpus
        self.model_name = model_name
        
        # Create cache directory
        cache_path = Path(cache_dir)
        cache_path.mkdir(exist_ok=True)
        
        # Create cache key from model name and corpus size
        safe_model_name = model_name.replace("/", "_")
        cache_file = cache_path / f"{safe_model_name}_embeddings_{len(corpus)}.npy"
        
        if cache_file.exists():
            print(f"[i] Loading cached embeddings from {cache_file}")
            self.embeddings = np.load(cache_file)
            self.model = SentenceTransformer(model_name, device=device)
        else:
            print(f"[i] Computing embeddings for {len(corpus)} requirements...")
            self.model = SentenceTransformer(model_name, device=device)
            self.embeddings = self.model.encode(
                [self._doc(r) for r in corpus],
                show_progress_bar=True,
                convert_to_numpy=True,
                normalize_embeddings=True,
            )
            np.save(cache_file, self.embeddings)
            print(f"[i] Saved embeddings to {cache_file}")

    @staticmethod
    def _doc(r: Requirement) -> str:
        return f"passage: {r.title}. {r.text[:500]}"

    def top_k(self, query: Requirement, k: int = 15) -> list[tuple[Requirement, float]]:
        from sentence_transformers.util import cos_sim

        cached = getattr(self, "_query_emb", {}).get(query.id)
        if cached is not None:
            query_embedding = cached
        else:
            query_embedding = self.model.encode(
                f"query: {query.title}. {query.text[:500]}",
                normalize_embeddings=True,
            )

        similarities = cos_sim(query_embedding, self.embeddings)[0]
        top_indices = similarities.argsort(descending=True)[:k]
        return [(self.corpus[i], float(similarities[i])) for i in top_indices]

    def precompute_queries(self, queries: list[Requirement]) -> None:
        self._query_emb = _precompute_with_cache(self.model, queries, model_name=self.model_name)


def make_shortlister(
    corpus: list[Requirement],
    method: Literal["tfidf", "embedding", "cached_embedding"] = "tfidf",
    **kwargs,
) -> TfidfShortlister | EmbeddingShortlister | CachedEmbeddingShortlister:
    """Factory to create appropriate shortlister.
    
    Args:
        corpus: List of GS requirements
        method: "tfidf" (fast), "embedding" (better quality), or "cached_embedding"
        **kwargs: Passed to shortlister constructor
    """
    if method == "tfidf":
        return TfidfShortlister(corpus, **kwargs)
    elif method == "embedding":
        return EmbeddingShortlister(corpus, **kwargs)
    elif method == "cached_embedding":
        return CachedEmbeddingShortlister(corpus, **kwargs)
    else:
        raise ValueError(f"Unknown method: {method}")


# Backwards compatibility - Shortlister is now TfidfShortlister
Shortlister = TfidfShortlister


if __name__ == "__main__":
    from pathlib import Path
    from . import parse_gs, parse_gspp

    root = Path(__file__).resolve().parent.parent
    gs_reqs = parse_gs.parse(root / "data" / "gs.xml")
    gspp_reqs = parse_gspp.parse(root / "data" / "gspp.json")

    print("=" * 60)
    print("TF-IDF Shortlister")
    print("=" * 60)
    sl = TfidfShortlister(gs_reqs)
    for q in gspp_reqs[:3]:
        print(f"\n== {q.id} {q.title} ==")
        for r, s in sl.top_k(q, k=5):
            print(f"  {s:.3f}  {r.id}  [{r.level}]  {r.title[:70]}")

    # Try embedding if sentence-transformers is available
    try:
        print("\n" + "=" * 60)
        print("Embedding Shortlister (multilingual-e5-large)")
        print("=" * 60)
        sl_emb = EmbeddingShortlister(gs_reqs[:100])  # Test with subset
        for q in gspp_reqs[:3]:
            print(f"\n== {q.id} {q.title} ==")
            for r, s in sl_emb.top_k(q, k=5):
                print(f"  {s:.3f}  {r.id}  [{r.level}]  {r.title[:70]}")
    except ImportError:
        print("\n[i] sentence-transformers not installed, skipping embedding test")
        print("    Install with: pip install sentence-transformers")
