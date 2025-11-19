# Code Coverage Configuration

## Goals

- **Target**: 95%+ coverage for all implementation files
- Prevents untested code paths
- Detects breaking changes early

## Configuration File

`.coveragerc` at project root controls coverage:

```ini
[report]
exclude_lines =
    pragma: no cover
    if __name__ == .__main__.:
    raise NotImplementedError

omit =
    */tests/*
    */venv/*
```

## Running Coverage

```bash
# Individual module with coverage report
.venv/bin/python tests/subpackage/test_module.py

# Entire package
.venv/bin/python tests/subpackage/all.py

# All tests
.venv/bin/python tests/all.py
```

Output: HTML report in `htmlcov/` showing covered/uncovered lines.

## Marking Code as Non-Testable

Use `# pragma: no cover` for untestable code:

```python
if sys.platform == "win32":  # pragma: no cover
    return "windows"
```

Use for:
- Platform-specific code
- Emergency fallbacks
- Code that shouldn't occur in normal operation

Don't use for regular logic or error handling.
