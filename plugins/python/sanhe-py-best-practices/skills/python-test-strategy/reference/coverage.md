# Code Coverage Configuration

This guide covers code coverage configuration, goals, and best practices.

## Coverage Configuration File

The `.coveragerc` file in the root directory configures the coverage tool. It specifies which files to exclude from coverage reports in the `omit` section.

**Example `.coveragerc`:**
```ini
[run]
branch = True

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:

omit =
    */tests/*
    */venv/*
    setup.py
```

## Configuration Options

### [run] Section
Controls how coverage is collected:
- `branch = True`: Measure branch coverage (if/else, loops)
- `source = .`: Measure coverage from current directory

### [report] Section
Controls coverage reporting:
- `exclude_lines`: Lines that don't count against coverage (preprocessor directives, debugging code, defensive assertions)
- `omit`: File patterns to exclude from coverage reports

### Common Exclusions

Files typically omitted from coverage:
- Test files: `*/tests/*`
- Virtual environments: `*/venv/*`, `*/env/*`
- Setup files: `setup.py`
- Configuration files: `conftest.py` (unless testing configuration)

## Coverage Goals

**Target Coverage: 95%+** for all implementation files

This means:
- At least 95 out of every 100 lines of code executed in tests
- Covers most code paths and edge cases
- Allows for minimal pragma exclusions

## Marking Code as Non-Testable

Use `# pragma: no cover` for code that cannot or should not be tested:

```python
def platform_specific_function():
    if sys.platform == "win32":
        # Windows-specific code
        # pragma: no cover
        return "windows"
    else:
        # Unix-like systems
        return "unix"
```

**When to use `pragma: no cover`:**
- Platform-specific code (Windows vs Unix)
- Environment-dependent code (when testing on different platforms)
- Defensive code that shouldn't occur in normal operation
- Emergency fallbacks

**When NOT to use:**
- Regular logic paths
- Error handling that can be tested
- Optional features

## Coverage Report Interpretation

### Line Coverage
Shows which lines were executed during tests:
- **Green**: Executed (covered)
- **Red**: Not executed (uncovered)
- **Yellow**: Partial (some branches not executed)

### Branch Coverage
Shows which conditional branches were tested:
```python
if x > 10:           # branch 1: tested
    return True
else:                # branch 2: tested
    return False
```

Both branches should be tested to achieve full coverage.

### Summary Statistics

Coverage reports show:
- **Statements**: Individual lines of code
- **Branches**: Conditional paths
- **Excluded**: Lines marked with `pragma: no cover`
- **Total Coverage %**: Overall coverage percentage

## Best Practices

1. **Aim for 95%+ early**: Don't let coverage debt accumulate
2. **Use coverage as a guide, not a goal**: 95% coverage catches most bugs, but doesn't guarantee correctness
3. **Focus on critical paths first**: Test important business logic before corner cases
4. **Review uncovered lines**: Every red line should have a reason (pragma, impossible path, or needs testing)
5. **Run coverage before commits**: Make it part of your CI/CD pipeline
