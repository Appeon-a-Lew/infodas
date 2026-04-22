# Infodas project 

## How to use 

### Setup
```bash
python3.11 -m pip install -r requirements.txt
```

### Basic Usage
```bash
# Basic run with default settings (Basis + Standard levels)
python3.11 -m src.run --model gpt-5.4-mini

# Include Hoch level requirements (full corpus - recommended)
python3.11 -m src.run --model gpt-5.4-mini --gs-levels Basis,Standard,Hoch

# Multi-model ensemble
python3.11 -m src.run --model claude-sonnet-4-5,gpt-5.4-mini
```

### Key Options
- `--model`: LLM to use (gpt-*, claude-*). Can specify multiple for ensemble.
- `--gs-levels`: Which GS levels to include (default: Basis,Standard). Use Basis,Standard,Hoch for full coverage.
- `--scope`: Filter by GS++ ID prefix (e.g., GC, ARCH, OPS)
- `--limit`: Limit number of GS++ controls processed
- `--discriminator`: Enable LLM-based filtering of redundant mappings
- `--evaluate`: Evaluate against golden dataset (for GC scope)

### Examples
```bash
# Evaluate quality against golden dataset (GC controls)
python3.11 -m src.run --model gpt-5.4-mini --evaluate --scope GC --gs-levels Basis,Standard,Hoch

# Run with discrimination to remove redundant candidates
python3.11 -m src.run --model gpt-5.4-mini --discriminator --discriminator-model gpt-5.4-mini

# Full pipeline: multi-model + discrimination + evaluation
python3.11 -m src.run --model gpt-5.4-mini,claude-sonnet-4-5 --discriminator --evaluate --scope GC --gs-levels Basis,Standard,Hoch
```

### Manual Mappings
By default the run looks for `out/gspp_compliance_v3approach.csv` and adds those as an additional source. Override with `--manual-csv /path/to/file.csv`.
