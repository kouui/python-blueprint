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

(unecessary) to import module under develepment 
```
uv pip install -e .
```


project blueprint reference:
https://github.com/johnthagen/python-blueprint

