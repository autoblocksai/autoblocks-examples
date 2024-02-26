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
OPENAI_API_KEY=<your-openai-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-autoblocks-ingestion-key>
```

<!-- getting started end -->

## Create a prompt

Go to https://app.autoblocks.ai/prompts and click on Create Prompt.

![example-prompt](https://github.com/autoblocksai/autoblocks-examples/assets/15793238/f3c148de-87b4-4b6c-ad61-6638544882a5)

Create a prompt like this and deploy it.

## Set your API key

Then, get your API key from [here](https://app.autoblocks.ai/settings/api-keys) and set it as an environment variable:

```bash
export AUTOBLOCKS_API_KEY=...
```

## Create your `.autoblocks.yml` file

This file instructs the CLI which prompts and which of their versions
to autogenerate code for. One has already been created for you in [`./.autoblocks.yml`](./.autoblocks.yml).

## Install dependencies

```bash
poetry install
```

## Autogenerate classes

This CLI will autogenerate classes for you to use to interact with the prompts you've created in the UI.

```
poetry run autoblocks prompts generate
```

## Run the script

Without Prompt SDK:

```bash
poetry run start
```

With Prompt SDK:

```bash
poetry run start-with-prompt-sdk
```
