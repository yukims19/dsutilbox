# 🛠️ Developer Guide for `dsutilbox`

This guide is for contributors and maintainers of the `dsutilbox` package. It includes instructions on setup, development workflow, testing, and publishing.

## 📁 Project Structure

```
dsutilbox/
├── dsutilbox/              # Core package code
│   ├── __init__.py
│   └── preprocessing.py
│   └── ...
├── tests/                  # Unit tests
├── pyproject.toml          # Package metadata
├── requirements.txt
├── README.md
├── DEVELOPER.md            # ← You're here
├── .gitignore
├── LICENSE
└── setup.py
```

## 🚀 Setup for Local Development

1. Clone the repo:

   ```bash
   git clone git@github.com:yukims19/dsutilbox.git
   cd dsutilbox
   ```

2. (Optional but recommended) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install in editable mode:

   ```bash
   pip install -e .
   ```

4. Install development/test dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## 🧪 Running Tests

We use `pytest` for testing:

```bash
pytest tests/
```

You can also run a specific test file:

```bash
pytest tests/test_preprocessing.py
```

## 🏷️ Releasing to PyPI

1. Bump the version in `pyproject.toml`.

2. Commit, tag, and push:

   ```bash
   git add pyproject.toml
   git commit -m "Release v0.X.Y"
   git tag v0.X.Y
   git push origin main --tags
   ```

3. Build and upload:

   ```bash
   python -m build
   twine upload dist/*
   ```

## 🔧 Common Scripts

- Clean up old build artifacts:

  ```bash
  rm -rf dist/ build/ *.egg-info/
  ```

- Reinstall the package:

  ```bash
  pip uninstall dsutilbox
  pip install -e .
  ```
