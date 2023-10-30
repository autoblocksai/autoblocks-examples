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

<!-- getting started start -->

## Getting started

- Sign up for an Autoblocks account at https://app.autoblocks.ai
- Grab your Autoblocks ingestion key from https://app.autoblocks.ai/settings/api-keys
- Grab your OpenAI API key from https://platform.openai.com/account/api-keys
- Create a file named `.env` in this folder and include the following environment variables:

```
OPENAI_API_KEY=<your-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
```

<!-- getting started end -->

## Replays

This project shows how you can run Autoblocks Replays via your [pytest](https://docs.pytest.org/en/7.4.x/) test suite. Follow the steps below to get started.

### 1. Use your replay key

Replace the value for `AUTOBLOCKS_INGESTION_KEY` in the `.env` file with your replay key. Your replay key is in the same place as your
ingestion key: https://app.autoblocks.ai/settings/api-keys

> **_NOTE:_** This means you need to make very few code changes to your production code to get started with Autoblocks Replays. You simply need to swap out an environment variable.

### 2. Run the tests

First install the dependencies:

```
poetry install
```

Then run the test suite with Autoblocks Replays enabled:

```
poetry run pytest --autoblocks
```

Within the test suite, you should see a link printed to the console that will take you to the replay in the Autoblocks UI:

```
➜  poetry run pytest --autoblocks
=========================================== test session starts ============================================
platform darwin -- Python 3.11.4, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/nicole/autoblocks/autoblocks-examples/Python/pytest-replays
plugins: anyio-4.0.0, autoblocksai-0.0.11
collected 3 items

test_main.py ...                                                                                     [100%]

======================================== Autoblocks Replay Results =========================================
View your replay: https://app.autoblocks.ai/replays/local/run/nicole-pytest-20231030-122752
============================================================================================================
============================================ 3 passed in 16.65s ============================================
```

Run the tests a few times so that you generate multiple replays (your first replay won't have any baseline to compare against!).

### 3. View the replays in the Autoblocks UI

The link will take you to the replay UI where you can see at-a-glance differences between the replay runs over the three test cases. There are four main columns:

- **Message**: The name of the Autoblocks event sent
  - a gray icon indicates no changes
  - a yellow icon indicates changes
  - a red icon indicates the event was there before but not now
  - a green icon indicates the event was not there before but is now
- **Changes**: The number of word changes between the event properties of the replay run and the baseline run
- **Difference Scores**: For properties that we've detected to be LLM outputs, this column will show you a difference score between the value from the baseline run and the current run
- **Evals**: The results of your [Autoblocks Evaluators](https://docs.autoblocks.ai/features/evaluators)

In one of my runs, I could see that the difference score was pretty high for the `"What is your refund policy?"` test case:

![replay-summary](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/cb99858a-8f94-4bd9-b8b4-893e32097642)

Clicking into **View Differences**, I could see that the response now included an apology about not being able to answer questions about refunds, even though it did previously:

![replay-differences](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/53b33ed5-fe8e-44cf-ac07-c2f315ecb4b9)

This kind of snapshot / stability testing is important to run over LLM outputs on every pull request so that you can catch regressions before they go to production.

### 4. Run the replays in GitHub Actions

See the [Autoblocks Replays GitHub Action](/.github/workflows/autoblocks-replays.yml) workflow; this workflow runs replays on every pull request and also on a schedule. The results of these replays will be under the GitHub tab on the [replays](https://app.autoblocks.ai/replays) page.