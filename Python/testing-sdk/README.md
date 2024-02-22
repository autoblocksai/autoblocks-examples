<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="150px">
</p>
<p align="center">
  📚
  <a href="https://docs.autoblocks.ai/">Documentation</a>
  &nbsp;
  •
  &nbsp;
  🖥️
  <a href="https://app.autoblocks.ai/">Application</a>
  &nbsp;
  •
  &nbsp;
  ☎️
  <a href="https://cal.frontapp.com/autoblocks/adam/autoblocks-engineering/">Meet with Autoblocks Engineering</a>
</p>

## Setup

### Install [`poetry`](https://python-poetry.org/)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Install [`npm`](https://docs.npmjs.com/about-npm)

> **_NOTE:_** You might already have this installed. Check with `npm -v`.

If you don't have `node` or `npm` installed, we recommend you use `nvm` to do so:

#### Install [`nvm`](https://github.com/nvm-sh/nvm)

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```

#### Install `node` and `npm`

```bash
nvm install node
```

#### Set the default version when starting a new shell

```bash
nvm alias default node
```

### Install dependencies

```
poetry install
```

## Run Autoblocks tests

### Set your Autoblocks API key

Retrieve your **local testing API key** from the [settings page](https://app.autoblocks.ai/settings/api-keys) and set it as an environment variable:

```bash
export AUTOBLOCKS_API_KEY=...
```

### Set your OpenAI API key

```bash
export OPENAI_API_KEY=...
```

### Run the tests

```bash
npx autoblocks testing exec -m "my first run" -- poetry run start
```

You should see something like:

<img width="1668" alt="Screenshot 2024-02-22 at 1 23 50 PM" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/ded25aa8-1439-432d-86a6-7254b27b970b">

You can click on the links next to each test name to dig into more details.
You can also find all of your tests on the testing homepage in the [Autoblocks application](https://app.autoblocks.ai/testing/local).

## GitHub Actions setup

A starter workflow was added in [`.github/workflows/autoblocks-testing.yml`](./.github/workflows/autoblocks-testing.yml).
This workflow runs the tests on every push to the repository and also
on a daily schedule.

## Repo structure

```
my_project/
  run.py <-- imports all tests from tests/ and runs them
  evaluators/ <-- all common evaluators are implemented here
    some_shared_evaluator1.py
    some_shared_evaluator2.py
  tasks/ <-- all "tasks" are implemented here
    task1.py
    task2.py
  test_suites/ <-- tests for each task
    task1/
      __init__.py <-- implements the runner for task1
      evaluators.py  <-- evaluators used only for task1
      test_cases.py <-- contains test cases for task1
    task2/
      __init__.py <-- implements the runner for task2
      evaluators.py  <-- evaluators used only for task2
      test_cases.py <-- contains test cases for task2
```
