# Test File Naming & Organization

## Convention

Test files mirror source directory structure with consistent naming:

```
Source: <project>/<subpackage>/<module>.py
Test:   tests/<subpackage>/test_<subpackage>_<module>.py
```

## Examples

| Source | Test |
|--------|------|
| `learn_haystack/math/calculator.py` | `tests/math/test_math_calculator.py` |
| `learn_haystack/math/ops/add.py` | `tests/math/ops/test_math_ops_add.py` |
| `learn_haystack/utils.py` | `tests/test_utils.py` |

## Finding Test Location

Use the script to determine correct test path:
```bash
python scripts/locate_test_file.py /absolute/path/to/source.py
```

## Directory Structure

Test directories mirror source packages:
```
learn_haystack/          tests/
├── math/        →      ├── math/
│   └── ops/     →      │   └── ops/
└── utils.py     →      └── test_utils.py

tests/math/all.py       # Run all tests in math package
tests/math/ops/all.py   # Run all tests in ops subpackage
tests/all.py            # Run all project tests
```

## Why This Pattern

- Unique names prevent collisions across packages
- Directory mirroring makes tests easy to find
- Full path in filename supports tooling (IDE jumps, auto-generation)
