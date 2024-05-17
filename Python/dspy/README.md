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

## Create your config in Autoblocks

1. Visit the [configs](https://app.autoblocks.ai/configs) page in Autoblocks
2. Click on the **Create Config** button
3. Name your config **dspy**
4. Add the following properties:

| Parameter Name         | Type   | Default | Values                                   |
| ---------------------- | ------ | ------- | ---------------------------------------- |
| model                  | enum   | gpt-4o  | "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo" |
| max_bootstrapped_demos | number | 4       | -                                        |
| max_labeled_demos      | number | 4       | -                                        |
| max_rounds             | number | 1       | -                                        |
| max_errors             | number | 5       | -                                        |

## Run the example

### Set your Autoblocks Ingestion Key

Retrieve your **Ingestion key** from the [settings page](https://app.autoblocks.ai/settings/api-keys) and set it as an environment variable:

```bash
export AUTOBLOCKS_INGESTION_KEY=...
```

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

![image](https://github.com/autoblocksai/autoblocks-examples/assets/15793238/eff0e0da-4625-4764-9b53-d208f152f601)

You can click on the links next to each test name to dig into more details.
You can also find all of your tests on the testing homepage in the [Autoblocks application](https://app.autoblocks.ai/testing/local).

### Edit the config

Edit your config in the Autoblocks UI and save as a new revision.

### Run the tests with the new config

```bash
npx autoblocks testing exec -m "my second run" -- poetry run start
```

## Futher Reading

- [Autoblocks Testing documentation](https://docs.autoblocks.ai/testing/sdks)
- [Autoblocks Config documentation](https://docs.autoblocks.ai/manage/config-sdks/python/quick-start)
