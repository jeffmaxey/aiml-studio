# Getting Started

Build, run, and explore AIML Studio locally in a few minutes.

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for dependency management

## Install dependencies

```bash
uv sync
```

## Run the app

```bash
uv run python -m aiml_studio.app
```

The app will be available at `http://localhost:8050`.

## Development shortcuts

```bash
make install   # Create env + install pre-commit hooks
make check     # Lint, type-check, dependency checks
make test      # Run pytest
```

## Build the documentation

```bash
make docs-test   # Build docs without warnings
make docs        # Serve docs locally
```

## Configuration notes

- Application settings are managed in `aiml_studio/settings.py`.
- Theme customization lives in `aiml_studio/styles/theme.py`.
- Layouts and components are organized under `aiml_studio/layouts` and `aiml_studio/components`.
