# CI Setup Documentation

## Tool
GitHub Actions was selected because the project is hosted on GitHub and the workflow
can be stored with the source code.

## Pipeline
1. Checkout repository.
2. Install Python 3.12.
3. Install pytest and flake8.
4. Run flake8 linting.
5. Run pytest and generate JUnit XML.
6. Upload the JUnit report as an artifact.

## Triggers
`push` and `pull_request` events trigger the pipeline.

## Failure behavior
The lint and test commands must exit successfully. Any failure stops the job and marks
the workflow as failed.

## Local reproduction
```bash
python -m pip install -r requirements.txt
flake8 gradebook.py tests
pytest -q --junitxml=test-results.xml
```

## Replication
Create the same `.github/workflows/python-ci.yml` file in a GitHub repository, push the
project, and inspect the Actions tab. A harmless commit can be used to verify the push
trigger.
