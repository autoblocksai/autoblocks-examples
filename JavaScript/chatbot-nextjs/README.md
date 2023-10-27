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

# Chatbot Example

This is a Next.js app that uses openai and Autoblocks to power and monitor a chatbot.

View the deployed application at https://chatbot-example.autoblocks.ai

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
npm install
```

## Run the app

```bash
npm run dev
```

Visit http://localhost:3000 to see the app.

## View logs in Autoblocks

As you interact with the app, you will see traces appear in the Autoblocks [explore page](https://app.autoblocks.ai/explore).

![Autoblocks Explore](https://github.com/autoblocksai/novel-autoblocks-example/blob/main/novel-autoblocks-example.png?raw=true)
