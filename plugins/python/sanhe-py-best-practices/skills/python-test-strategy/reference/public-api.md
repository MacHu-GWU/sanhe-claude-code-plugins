# Public API Testing

## API Module

Create `api.py` that exports all public interfaces (one import per line):

```python
# project/api.py
from .math.operations import add_numbers
from .math.operations import subtract_numbers
from .utils.helpers import format_output
from .core.engine import create_engine
```

One import per line makes changes clear in diffs and easier to maintain.

## Test Public API

Test file at `tests/test_api.py` verifies all exports are accessible:

```python
from project import api

def test_api():
    """Verify all public APIs are importable."""
    _ = api.add_numbers
    _ = api.subtract_numbers
    _ = api.format_output
    _ = api.create_engine
```

## Purpose

- Catch accidental removal of public exports
- Prevent breaking changes to API
- Document what users can import
- Fail tests if API changes unexpectedly

## Best Practices

1. **Export only stable APIs** - Functions and classes that are unlikely to change
2. **Keep minimal** - Don't export internal utilities
3. **Document** - Add docstring to `api.py` explaining what's exported
4. **Group logically** - Organize imports by functional area

## Deprecation

Mark deprecated APIs before removal:

```python
import warnings

def old_function():
    """Deprecated: Use new_function() instead."""
    warnings.warn("Use new_function instead", DeprecationWarning, stacklevel=2)
    return new_function()
```
