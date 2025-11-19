# Public API and Testing

This guide covers how to organize and test your project's public API.

## Public API Pattern

The package includes an `api.py` file that exposes all public APIs for package users. Each line in this file defines a single Python class, function, or variable.

**Location:**
```
<project>/api.py
```

**Example for `learn_claude_code` project:**
```python
# In learn_claude_code/api.py
from .math.operations import add_numbers
from .math.operations import subtract_numbers
from .utils.helpers import format_output
from .core.engine import create_engine
```

## Import Pattern: One Per Line

**Recommended (one import per line):**
```python
from .my_module import my_func_1
from .my_module import my_func_2
from .my_module import MyClass
```

**NOT recommended (multiple imports per line):**
```python
from .my_module import my_func_1, my_func_2, MyClass
```

**Why?**
- Easier to read and navigate
- Clearer in git diffs (one line = one export)
- Simpler to add/remove exports
- Better for documentation generation

## Public API Test File

Test your public API in `tests/test_api.py`. This test establishes a baseline for all public API exports, ensuring that any changes to `api.py` are caught by unit tests.

**Location:**
```
tests/test_api.py
```

**Purpose:**
- Verify all public API objects are importable
- Catch accidental removal of public exports
- Document what constitutes the public interface
- Prevent breaking changes to the public API

## Example `tests/test_api.py`

For a project named `learn_claude_code`:

```python
from learn_claude_code import api

def test():
    """Test that all public APIs are accessible."""
    _ = api
    _ = api.add_numbers
    _ = api.subtract_numbers
    _ = api.format_output
    _ = api.create_engine
```

**What this test does:**
1. Imports the `api` module
2. Accesses each public export
3. Ensures no ImportError or AttributeError occurs
4. Fails if any public API is removed or broken

## Best Practices

### 1. Keep API Surface Minimal

Only export functions and classes that are:
- Stable and unlikely to change
- Useful for external users
- Well-documented
- Covered by tests

### 2. Group Related Imports

Organize imports logically:

```python
# Core functionality
from .core.engine import create_engine
from .core.config import Configuration

# Data structures
from .data.loader import DataLoader
from .data.processor import DataProcessor

# Utilities
from .utils.helpers import format_output
from .utils.validators import validate_input
```

### 3. Document Public API

Add a docstring to `api.py` explaining what's exported:

```python
"""
learn_claude_code public API.

This module exports all public interfaces for learn_claude_code users.
"""

from .math.operations import add_numbers
from .math.operations import subtract_numbers
# ... rest of exports
```

### 4. Version Your API

For major version changes, consider separate API modules:

```python
# api.py (current version)
from .core import *

# api_v1.py (deprecated, for backward compatibility)
from .legacy import *
```

### 5. Test API Import Paths

Ensure users can import from the package directly:

```python
# This should work:
from learn_claude_code import add_numbers, create_engine

# Both of these patterns should be valid:
from learn_claude_code.api import add_numbers
import learn_claude_code
learn_claude_code.add_numbers
```

## API Documentation Template

Include in your project documentation:

```markdown
# Public API Reference

## Core Functions

- `add_numbers()` - Add two numbers together
- `subtract_numbers()` - Subtract two numbers
- `create_engine()` - Create a processing engine

## Utilities

- `format_output()` - Format output for display
- `validate_input()` - Validate user input

```

## API Stability Guidelines

- **Stable**: Don't break without major version bump
- **Deprecated**: Mark old APIs with deprecation warnings before removal
- **Experimental**: Clearly mark unstable APIs; don't add to public API yet

```python
import warnings

def old_function():
    """Deprecated: Use new_function() instead."""
    warnings.warn(
        "old_function is deprecated, use new_function instead",
        DeprecationWarning,
        stacklevel=2
    )
    return new_function()
```
