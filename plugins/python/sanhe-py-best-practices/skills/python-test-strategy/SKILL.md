---
name: python-test-strategy
description: Python testing patterns with organized test file structure, coverage goals, and public API testing
---

# python-test-strategy

Organized testing strategy for Python projects: test file naming, coverage goals (95%+), and public API testing.

## Quick Start

**Find test location for any source file:**
```bash
python scripts/locate_test_file.py /path/to/source/file.py
```

**Run tests:**
- Individual file: `.venv/bin/python tests/subpackage/test_*.py`
- Package: `.venv/bin/python tests/subpackage/all.py`
- All: `.venv/bin/python tests/all.py`

## Key Patterns

- **Test files mirror source**: `source/<pkg>/<module>.py` → `tests/<pkg>/test_<pkg>_<module>.py`
- **Coverage goal**: 95%+ for all implementation files
- **Public API**: Export all public interfaces in `api.py`, test in `tests/test_api.py`

## References

- 🎯 [Naming & File Location](./reference/naming.md)
- 📊 [Coverage Setup](./reference/coverage.md)
- 🔌 [Public API Testing](./reference/public-api.md)
