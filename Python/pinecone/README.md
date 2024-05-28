# autoblocks-pinecone

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

### Generate prompts

```
poetry run prompts generate
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

### Set your Pinecone API key

```bash
export PINECONE_API_KEY=...
```

### Run the tests

```bash
npx autoblocks testing exec -m "my first run" -- poetry run test
```
