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

### Set your Autoblocks API key

Retrieve your **local testing API key** from the [settings page](https://app.autoblocks.ai/settings/api-keys) and set it as an environment variable:

```bash
export AUTOBLOCKS_API_KEY=...
```

### Create your prompts

```bash
poetry run create-prompts
```

### Create the `.autoblocks.yml` file

This file instructs the CLI which prompts and which of their versions
to autogenerate code for. One has already been created for you in [`./.autoblocks.yml`](./.autoblocks.yml).

### Autogenerate prompt classes

This CLI will autogenerate classes for you to use to interact with the prompts you've created in the UI.

```
poetry run prompts generate
```

### Create config

On the [configs page](https://app.autoblocks.ai/configs) create a new config with the following parameters:

- **Name**: `health-copilot-retrieval`
- **top_k**: `number` (default: `1`)
- **similarity_metric**: `enum` (default: `euclidean`) (options: `euclidean`, `cosine`, `dot_product`)

### Set your Pinecone API key

```bash
export PINECONE_API_KEY=...
```

### Load Pinecone data

```bash
poetry run load-data
```

## Run Autoblocks tests

### Set your OpenAI API key

```bash
export OPENAI_API_KEY=...
```

### Run the tests

```bash
npx autoblocks testing exec -m "my first run" -- poetry run test
```
