# actions-demo
Example repository for working with github actions

## Github Actions

## ...

Github Actions are software scripts triggered by Github events

## Github Events

- schedule
- workflow_dispatch
- repository_dispatch
- check_run
- create
- delete
- deployment
- fork
- issue_comment
- issues
- page_build
- project
- project_card
- public
- pull_request
- pull_request_review
- pull_request_review_comment
- pull_request_target
- push
- registry_package
- release
- status
- watch
- workflow_run
- etc

## Github Event - push

```
name: unittest
on:
  push:
    branches:
      - master
  pull_request:
    branches:
      - master

jobs:
  unittest:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version : '3.9'
      - name: Run unittests
        run:  python -m unittest discover -v
```

## Github Event - pull_request


