<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="300px">
</p>

# Novel Autoblocks Example

Example Next.js application using [Novel](https://github.com/steven-tey/novel) and [Autoblocks](https://www.autoblocks.ai).

Based on [novella](https://github.com/steven-tey/novella).

## Quick Start

### Install Dependencies

```
npm install
```

### Sign up for Autoblocks

Sign up for an Autoblocks account at https://app.autoblocks.ai and grab your ingestion key from [settings](https://app.autoblocks.ai/settings/api-keys).

### Set environment variables

Create a `.env.local` file in the root directory of the project with the following environment variables:

```
OPENAI_API_KEY=<your-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
```

### Run the app

```
npm run dev
```

Visit http://localhost:3000 to see the app.

### View logs in Autoblocks

As you interact with the app, you will see traces appear in the Autoblocks explore page.

![Autoblocks Explore](https://github.com/autoblocksai/novel-autoblocks-example/blob/main/novel-autoblocks-example.png?raw=true)

## More Information

For more information on how to use Autoblocks, visit the [Autoblocks documentation](https://docs.autoblocks.ai/).

For more information on how to use Novel, visit the [Novel repository](https://github.com/steven-tey/novel).
