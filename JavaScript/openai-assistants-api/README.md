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
- Grab your Autoblocks api key from https://app.autoblocks.ai/settings/api-keys
- Grab your OpenAI API key from https://platform.openai.com/account/api-keys
- Create a file named `.env` in this folder and include the following environment variables:

```
OPENAI_API_KEY=<your-openai-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-autoblocks-ingestion-key>
AUTOBLOCKS_API_KEY=<your-autoblocks-api-key>
```

<!-- getting started end -->

## Create a prompt

Go to https://app.autoblocks.ai/prompts and click on Create Prompt.

![example-prompt](https://github.com/autoblocksai/autoblocks-examples/assets/15793238/f3c148de-87b4-4b6c-ad61-6638544882a5)

Create a prompt like this and deploy it.

## Install Dependencies

```
npm install
```

## Run the script

Without Prompt SDK:

```
npm run start
```

With Prompt SDK:

```
export AUTOBLOCKS_API_KEY=npm run start-with-prompt-sdk
```

More info on Prompt SDK can be found [here](https://docs.autoblocks.ai/prompt-sdks/javascript).

## View logs in Autoblocks

After you run the script, you will see a link to view the trace in your console. You can also navigate directly to the [explore page](https://app.autoblocks.ai/explore) to see the trace.
