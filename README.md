# project name

## installation

### create python virtual environment

```bash
cd /path/to/this/repository
uv sync
```

### (optional) install pre-commit hooks

for pre-commit hooks.

```bash
uv run pre-commit install
```

### check and format code lint/type

```bash
uv run nox
```

or 
```bash
uv run nox -s lint
uv run nox -s lint_fix
```
and then
```bash
uv run nox -s fmt
```
## usage

```bash
❯ uv run .\experiments\experiment_name\main.py
[2025-05-09 20:54:03][INFO][logger.py][setup_logger][line 95] logger initialized
[2025-05-09 20:54:03][INFO][main.py][main][line 7] Executing the main function...
```

## else

project blueprint reference:
https://github.com/johnthagen/python-blueprint

