# Testing Documentation

The test suite uses `unittest` assertions and is executed by pytest in CI.

Coverage includes:
- 0 and 100 boundary marks
- negative, above-100, and non-numeric marks
- average calculation
- empty input
- A/B/C/D/F grade boundaries
- student creation and whitespace normalization
- empty-name validation

Commands:
```bash
flake8 gradebook.py tests
pytest -q --junitxml=test-results.xml
```
