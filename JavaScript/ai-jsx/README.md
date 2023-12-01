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

## Run the script

```
npm run start
```

## View the tracked prompts in Autoblocks

At https://app.autoblocks.ai/prompts, you should see an entry for each `autoblocks-tracker-id` in the example script:

```tsx
<ChatCompletion
  temperature={0}
  model="gpt-3.5-turbo"
  autoblocks-tracker-id="get-thing-color"
>
```

and:

```tsx
<ChatCompletion
  temperature={0}
  model="gpt-3.5-turbo"
  autoblocks-tracker-id="determine-color-combination"
>
```

Click on View History to view a tracking ID's history. At this point it should only have one version.

<img width="1454" alt="tracking-ids" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/89810160-b89e-43d6-9d96-aad329bfa496">

## View the traces in Autoblocks

Click on the search icon to the left of the View History button to view traces belonging to the given tracking ID.

<img width="794" alt="filtered-traces" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/335784e2-9f45-4ea8-ac1d-e4bc3fea91dc">

Click on the trace to view the trace tree.

<img width="759" alt="trace-tree-1" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/81d3cc28-ec37-4c56-ad0f-cc1d354facfb">
<img width="756" alt="trace-tree-2" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/9232718f-aa26-48a8-89f0-62c4a553c26e">

## Make a change to one of the prompts

Make a change to one of the system or user messages. For example, in the `GetThingColor` component, change this:

```tsx
<SystemMessage>
  You are a helpful assistant. Always respond with one word in all lowercase
  letters and no punctuation.
</SystemMessage>
```

To this:

```tsx
<SystemMessage>
  You are a helpful assistant. ALWAYS respond with one word in all lowercase
  letters and no punctuation.
</SystemMessage>
```

## Run the script

Run the script again:

```
npm run start
```

After running the script, you should see a new version at https://app.autoblocks.ai/prompts/get-thing-color
since one of the templates changed:

<img width="1467" alt="get-thing-color-v2" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/655d651f-d4af-4473-893c-289b3723a9a4">

These automated versions are also attached to your traces as the property `promptTracking.version`, so you can use this property to create charts and tables to track the performance of your prompts over time.

<img width="1476" alt="chart" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/4bfa3dfc-0d45-44f5-9dc7-7bb02f54eb0e">
