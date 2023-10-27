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

```bash
poetry install
```

## Run the script

```bash
poetry run python main.py
```

## View the trace in Autoblocks

Go to the [explore page](https://app.autoblocks.ai/explore). When you find the trace, switch to the Trace Tree view to
see a tree of all the spans in the trace.

The first span that is selected will show you the overall question and answer of the LangChain pipeline, but you can also
drill into individual spans by clicking on them to understand how LangChain is working under the hood.

![screencapture-localhost-3000-explore-trace-a8bffa3c-e1f2-4d3d-b548-aedca7be7055-2023-10-26-10_28_59](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/941c09b7-86e9-4e0b-9df4-2a9be0b32771)

![screencapture-localhost-3000-explore-trace-a8bffa3c-e1f2-4d3d-b548-aedca7be7055-2023-10-26-10_29_14](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/99f02ba9-c3ea-4645-aa9d-17f6d83be790)
