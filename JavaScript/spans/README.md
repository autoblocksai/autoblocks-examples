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

## Getting started

- Sign up for an Autoblocks account at https://app.autoblocks.ai
- Grab your Autoblocks ingestion key from https://app.autoblocks.ai/settings/api-keys
- Create a file named `.env` in this folder and include the following environment variables:

```
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
```

## Creating spans

This example shows how you can establish parent / child relationships between your events by sending the `spanId` and `parentSpanId` properties.

## Install dependencies

```
npm install
```

## Run the script

```
npm run start
```

## View the trace tree

Go to the [explore page](https://app.autoblocks.ai/explore) and find the trace, then switch to the Trace Tree view. You should see something like this:

![rag-span](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/e5a0f0d9-8460-49a6-a8aa-d707d14323a6)

Within the RAG span, we made two embeddings calls: these are both children of the RAG span.

![embedding-span](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/7f9c4b4a-8704-4f7c-97b0-fd9acfc01932)

Then there is the LLM span at the end, which is not a child of the RAG span because we ended the RAG span before starting the LLM span:

![llm-span](https://github.com/autoblocksai/autoblocks-examples/assets/7498009/682d5d57-b343-4d5a-851a-e4aa9acef867)
