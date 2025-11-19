# Unit Test File Organization

Each Python file in your project's source directory has a corresponding unit test file in the `tests/` directory.

## Test File Naming Convention

The test file name includes the full relative path to the source file to prevent naming collisions.

**Pattern:**
```
Source: <project>/<subpackage>/<module>.py
Test:   tests/<subpackage>/test_<subpackage>_<module>.py
```

**Example:**

| Source File | Test File |
|-------------|-----------|
| `learn_claude_code/math/operations/calculator.py` | `tests/math/operations/test_math_operations_calculator.py` |
| `learn_claude_code/utils/helpers.py` | `tests/utils/test_utils_helpers.py` |
| `learn_claude_code/core/engine.py` | `tests/core/test_core_engine.py` |

## Directory Matching

The directory structure in `tests/` should mirror the structure in your source directory. If you have:

```
learn_claude_code/
├── math/
│   └── operations/
│       └── calculator.py
├── utils/
│   └── helpers.py
└── core/
    └── engine.py
```

Your test directory should be:

```
tests/
├── math/
│   └── operations/
│       └── test_math_operations_calculator.py
├── utils/
│   └── test_utils_helpers.py
└── core/
    └── test_core_engine.py
```

## Benefits of This Approach

1. **Prevents naming collisions**: Full path in test name prevents conflicts when modules have the same name in different packages
2. **Mirrors source structure**: Easy to find the corresponding test for any source file
3. **Scalable**: Works regardless of project depth or complexity
4. **Maintainable**: Clear naming convention requires no additional documentation
