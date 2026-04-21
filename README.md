# Infodas project 

## How to use 
make venv and install requirements. `python -m src.run --model gpt-5-mini`. Model can be either an anthropic model or an openai model.

To run multiple models in one pass, pass either a comma-separated list or multiple values after `--model`. Their selected GS candidates are combined additively and sorted by the summed model confidences, for example: `python -m src.run --model claude-sonnet-4-5,gpt-5.4-mini` or `python -m src.run --model claude-sonnet-4-5 gpt-5.4-mini`.

By default the run also looks for `out/gspp_compliance_v2.csv` and, if present, adds those mappings after the model run as an additional source. You can override that file with `--manual-csv /path/to/file.csv`.
