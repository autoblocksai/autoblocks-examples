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

## Install dependencies

```
npm install
```

## Start the template watcher

```
npm run gen:watch
```

## Run the script

```
npm run start
```

## View the prompts in Autoblocks

You should see the prompt tracking ID (`feature-a`) at https://app.autoblocks.ai/prompts.
Click on the tracking ID to view its history.
At this point it should only have one version.

## Make a change to one of the templates

Make a change to one of the templates in the [`prompt-templates`](./prompt-templates/) folder.
For example, update [`common/language`](./prompt-templates/common/language) to say:

```
ALWAYS respond in {{ language }}.
```

## Run the script

Run the script again:

```
npm run start
```

After running the script, you should see a new version at https://app.autoblocks.ai/prompts/feature-a.

![new-version](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/9c3a3c0b-1984-4cf6-8461-32ab9d2f18b6)
