# project name

...

```bash
cd /path/to/this/repository
uv sync
```

for pre-commit hooks.

```bash
uv run pre-commit install
```

```bash
uv run nox
```
or 
```bash
uv run nox -s lint
uv run nox -s lint_fix
```
```bash
uv run nox -s fmt
```

to import module under develepment
```
uv pip install -e .
```

### auto type annotate generation

reference: https://github.com/getsentry/auto-type-annotate
add the following two config into pyproject.toml for mypy
```
check_untyped_defs = true
local_partial_types = true
```
and then check dmypy server is running
```bash
$ uv run dmypy stop
Daemon stopped
$ uv run dmypy run
Daemon started
Success: no issues found in 6839 source files
```
auto annotate some file
```bash
auto-type-annotate \
    --application-directories .:src \
    src/path/to/authentication.py
```

project blueprint reference:
https://github.com/johnthagen/python-blueprint

