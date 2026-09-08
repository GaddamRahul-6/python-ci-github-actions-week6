# Week 6 - Continuous Integration for a Python Project

This project integrates GitHub Actions CI into a Python gradebook module.
Every push and pull request runs automated linting, tests, and test-report generation.

## Structure
```text
week6_ci_python_project/
├── .github/workflows/python-ci.yml
├── gradebook.py
├── tests/test_gradebook.py
├── requirements.txt
├── ci_setup.md
├── TESTING.md
└── README.md
```

## Local setup
```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

## Run checks locally
```bash
flake8 gradebook.py tests
pytest -q --junitxml=test-results.xml
```

## CI behavior
GitHub Actions runs on every push and pull request. A lint or test failure returns a
non-zero exit code and fails the job. The JUnit XML file is uploaded as an artifact so
results can be downloaded from the workflow run.

## View CI logs
Open GitHub -> Actions -> Python CI -> choose a run -> open the job. The artifact
named `junit-test-report` contains the XML test report.

## Verification
Push a small harmless commit and check that a new workflow run starts automatically.
