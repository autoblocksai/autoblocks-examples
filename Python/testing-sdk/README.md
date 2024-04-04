<!-- banner start -->
<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="300px">
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
  🏠
  <a href="https://www.autoblocks.ai/">Home</a>
</p>
<!-- banner end -->

## Setup

### Install [`poetry`](https://python-poetry.org/)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Install Autoblocks CLI

See [Autoblocks CLI documentation](https://docs.autoblocks.ai/cli/setup)

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

### Managed test cases

After you have ran your first test following the instructions above, you will see a test suite created called **flashcard-generator-managed** in the UI. Visit the [Test Cases Page](https://app.autoblocks.ai/test-cases) and click on this test suite.

Create a new test case with the following JSON body. [Click here to learn how to manage test cases](https://docs.autoblocks.ai/testing/test-case-management).

```json
{
  "notes": "The Industrial Revolution, which began in Britain in the late 18th century, brought about significant changes in society, economy, and technology, leading to the transition from agrarian to industrial economies."
}
```

Once updated, run the testing command again.

```bash
npx autoblocks testing exec -m "my second run" -- poetry run start
```

You will now see test results for **flashcard-generator-managed** with the test cases you just setup in the UI.

## GitHub Actions setup

A starter workflow was added in [`.github/workflows/autoblocks-testing.yml`](./.github/workflows/autoblocks-testing.yml).
This workflow runs the tests on every push to the repository and also
on a daily schedule.

## Repo structure

```
my_project/
  run.py <-- imports all tests from test_suites/ and runs them
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

## Futher Reading

- [Autoblocks Testing documentation](https://docs.autoblocks.ai/testing/sdks)
