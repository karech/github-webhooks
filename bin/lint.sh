#!/usr/bin/env sh
. .venv/bin/activate

echo "Running lint checks"

echo "Running pylint"
pylint github_webhooks
pylint example

echo "Running isort"
isort --check github_webhooks
isort --check example

echo "Running black"
black --check github_webhooks
black --check example

echo "Running pflake8"
pflake8 github_webhooks
pflake8 example

echo "Running mypy"
mypy github_webhooks
mypy example
