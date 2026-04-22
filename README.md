# GS++ → IT-Grundschutz Mapping Tool

Maps BSI Grundschutz++ (GS++) requirements to classic IT-Grundschutz (GS) requirements using LLM-based semantic matching.

## Features

- **Semantic Matching**: Uses TF-IDF (default) or semantic embeddings for candidate retrieval
- **Multi-Model Support**: OpenAI (GPT), Anthropic (Claude), with ensemble voting
- **Anti-Hallucination**: Built-in validation to catch invalid/non-existent GS IDs
- **Discriminator**: LLM-based filtering to remove redundant candidates
- **Golden Dataset**: Built-in evaluation dataset for quality assessment
- **Quality Validation**: Automatic validation of coverage/confidence consistency

## Setup

```bash
# Install dependencies
python3.11 -m pip install -r requirements.txt

# Optional: For semantic embeddings (better quality)
python3.11 -m pip install sentence-transformers

# Set API keys
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."  # Optional
```

## Basic Usage

```bash
# Basic run with defaults
python3.11 -m src.run --model gpt-5.4-mini

# Process more controls
python3.11 -m src.run --model gpt-5.4-mini --limit 50

# Multi-model ensemble (better quality)
python3.11 -m src.run --model gpt-5.4-mini,claude-sonnet-4-5 --limit 20
```

## Core Options

| Option | Description | Default |
|--------|-------------|---------|
| `--model` | LLM(s) to use. Comma-separated for ensemble | `claude-sonnet-4-5` |
| `--gs-levels` | GS levels: Basis,Standard,Hoch | `Basis,Standard,Hoch` |
| `--top-k` | Number of GS candidates to retrieve | `15` |
| `--limit` | Max GS++ controls to process (0=all) | `0` |
| `--scope` | Filter by GS++ prefix (e.g., GC, ARCH) | (all) |
| `--sample-ratio` | Sampling per category | `0.20` |

## Shortlisting Methods

Control how GS candidates are retrieved:

```bash
# TF-IDF (default) - fast, good quality
python3.11 -m src.run --model gpt-5.4-mini --shortlist-method tfidf

# Semantic embeddings - slower, better quality
python3.11 -m src.run --model gpt-5.4-mini --shortlist-method embedding

# Cached embeddings - fast after first run
python3.11 -m src.run --model gpt-5.4-mini --shortlist-method cached_embedding
```

**Recommendation**: Use `cached_embedding` for production runs after initial cache warmup.

## Discriminator (Remove Redundancies)

The discriminator filters redundant GS candidates:

```bash
# Basic discrimination
python3.11 -m src.run --model gpt-5.4-mini --discriminator

# Use reasoning model for better discrimination
python3.11 -m src.run --model gpt-5.4-mini --discriminator --discriminator-model gpt-5.4-thinking

# Strict mode (max 3 candidates, aggressive filtering)
python3.11 -m src.run --model gpt-5.4-mini --discriminator --discriminator-strict

# Full pipeline
python3.11 -m src.run --model gpt-5.4-mini \
    --discriminator --discriminator-model gpt-5.4-thinking --discriminator-strict \
    --limit 50
```

### Discriminator Models

| Model | Type | Quality | Speed |
|-------|------|---------|-------|
| `gpt-5.4-mini` | Standard | Good | Fast |
| `gpt-5.4-thinking` | Reasoning | ⭐⭐⭐ Excellent | Slow |
| `o3-mini` | Reasoning | ⭐⭐⭐ Excellent | Slow |
| `claude-sonnet-4-5` | Standard | Good | Fast |

## Quality Evaluation

### Golden Dataset Evaluation

Evaluate mapping quality against expert-verified mappings:

```bash
# Evaluate GC scope (has golden mappings)
python3.11 -m src.run --model gpt-5.4-mini --evaluate --scope GC --limit 20
```

Reports:
- Coverage Accuracy (%)
- Precision / Recall / F1 Score
- Confidence Error
- Confusion Matrix (TP/FP/FN)

### Validation

Automatic validation runs on every execution:

```
[i] validating matches ...
[i] validation complete: 0 errors, 2 warnings
```

Checks for:
- Invalid/hallucinated GS IDs
- Coverage/candidate mismatches
- Missing gap notes for partial coverage
- Confidence inflation detection

## Complete Examples

### Quick Test
```bash
python3.11 -m src.run --model gpt-5.4-mini --limit 5

```

### Testing withz Gs-> Gs
'''
python -m src.run \
  --testing-mode \
  --testing-gs-xml data/fake.xml \
  --model gpt-5.4,gpt-5.4-mini \     
  --expand-hierarchical \   
  --discriminator \
  --sample-ratio 1.0   --testing-limit 20 --discriminator-model gpt-5.4-thinking --shortlist-method embedding

'''

### High Quality Mapping (Recommended)
```bash
python3.11 -m src.run \
    --model gpt-5.4-mini \
    --shortlist-method cached_embedding \
    --discriminator --discriminator-model gpt-5.4-thinking \
    --gs-levels Basis,Standard,Hoch \
    --limit 100
```

### Research & Comparison
```bash
# Compare models
python3.11 -m src.run --model gpt-5.4-mini,gpt-4o-2024-11-20 --evaluate --scope GC

# Full evaluation with all features
python3.11 -m src.run \
    --model gpt-5.4-mini,claude-sonnet-4-5 \
    --shortlist-method cached_embedding \
    --discriminator --discriminator-model gpt-5.4-thinking --discriminator-strict \
    --evaluate --scope GC \
    --limit 50
```

## Output Files

All outputs saved to `out/` directory:

| File | Description |
|------|-------------|
| `mapping_*.csv` | Full mapping results |
| `mapping_*.md` | Human-readable report |
| `discriminated_*.csv` | Per-candidate decisions (if --discriminator) |
| `discriminated_*.html` | Visualization graph (if --discriminator) |

## Manual Mappings

By default, the tool loads `out/gspp_compliance_v3approach.csv` as an additional source. Override:

```bash
python3.11 -m src.run --model gpt-5.4-mini --manual-csv /path/to/custom.csv
```

## Architecture

```
GS++ Requirement → Shortlist (TF-IDF/Embeddings) → Judge (LLM) → Discriminator (LLM) → Output
                      ↓                              ↓                ↓
                 Top-K GS                    Coverage/Conf    Remove Redundant
                 Candidates                  Assessment       Candidates
```

## Tips

1. **Start small**: Use `--limit 10` to test before full runs
2. **Use cached embeddings**: First run builds cache, subsequent runs are fast
3. **Reasoning discriminator**: Worth the wait for final quality
4. **Multi-model**: Ensemble of 2-3 models improves accuracy
5. **Golden eval**: Use `--evaluate --scope GC` to check quality
