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

`.env`
```
OPENAI_API_KEY=<your-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
```
<!-- getting started end -->

## Install dependencies

```
npm install
```

## Run the script

```
npm run start
```

## View the trace in Autoblocks

Go to the [explore page](https://app.autoblocks.ai/explore). When you find the trace, switch to the Trace Tree view to
see a tree of all the spans in the trace.

The first span that is selected will show you the overall question and answer of the LangChain pipeline, but you can also
drill into individual spans by clicking on them to understand how LangChain is working under the hood.

![explore-trace-top-level-span](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/590e232a-eeaf-46a1-b9e3-3c0a8648234b)

![explore-trace-nested-span](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/b32d7776-8378-49cc-a866-7ba6bd08f5e5)
