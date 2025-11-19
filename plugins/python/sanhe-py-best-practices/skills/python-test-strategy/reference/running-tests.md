# Running Tests

This guide covers how to run tests at different levels of your Python project.

## Running Tests for Individual Files (Most Important Workflow)

The most common development workflow: edit a single source file, run its corresponding test to meet coverage goals.

**Command:**
```bash
.venv/bin/python tests/<subpackage>/test_<subpackage>_<module>.py
```

**Example:**
```bash
.venv/bin/python tests/math/operations/test_math_operations_calculator.py
```

**Output:**
1. Runs all unit tests for the specific module
2. Generates a code coverage HTML report at `htmlcov/${random_hash}_<module>_py.html`
3. Shows covered and uncovered lines in the HTML report

**Why This Matters**: 90% of development involves editing a single source file and running its test file to meet coverage goals.

## Running Tests for Entire Packages

Run coverage tests for a specific package or the entire Python project.

**Run all tests in project:**
```bash
.venv/bin/python tests/all.py
```

**Run tests for specific package:**
```bash
.venv/bin/python tests/<package_name>/all.py
```

**Examples:**
```bash
# Run all tests in the learn_claude_code package
.venv/bin/python tests/learn_claude_code/all.py

# Run all tests in math subpackage
.venv/bin/python tests/math/all.py

# Run all tests in entire project
.venv/bin/python tests/all.py
```

**Output:**
- Coverage reports for all modules in that package
- Aggregated coverage statistics
- HTML reports in `htmlcov/` directory

## Understanding Test Output

### HTML Coverage Reports

After running tests, open the generated HTML file to see:

- **Green lines**: Code executed during tests (covered)
- **Red lines**: Code not covered by tests (uncovered)
- **Line-by-line coverage details**: Click on files to see coverage breakdown

### Coverage Percentages

Each report shows:
- Statement coverage: Percentage of lines executed
- Branch coverage: Percentage of conditional branches executed
- Line count: Total lines and covered lines for each file

## Typical Development Workflow

1. **Edit source file** (e.g., `learn_claude_code/math/operations/calculator.py`)
2. **Run individual test** (e.g., `.venv/bin/python tests/math/operations/test_math_operations_calculator.py`)
3. **Check HTML report** for uncovered lines
4. **Add more tests** until coverage reaches 95%+
5. **Before committing**: Run full test suite (`.venv/bin/python tests/all.py`)

## Test Organization Tips

- Keep test files small and focused on single modules
- Run individual tests frequently during development
- Run package tests (`all.py`) before submitting pull requests
- Use the HTML reports to identify missing test cases
