<p align="center">
  <img src="https://app.autoblocks.ai/images/logo.png" width="300px">
</p>

# Python OpenAI Autoblocks Example

Example Python and OpenAI application using [Autoblocks](https://www.autoblocks.ai).

## Setup

* Install [`pyenv`](https://github.com/pyenv/pyenv)
  * Install python 3.11: `pyenv install 3.11`
* Install [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv)
* Install [`poetry`](https://python-poetry.org/docs/#installation)
* Create a virtualenv: `pyenv virtualenv 3.11 python-openai-autoblocks-example`
  * Activate the virtualenv: `pyenv activate python-openai-autoblocks-example`
* Install dependencies: `poetry install`

## Sign up for Autoblocks

Sign up for an Autoblocks account at https://app.autoblocks.ai and grab your ingestion key from [settings](https://app.autoblocks.ai/settings/api-keys).

## Set environment variables

```
OPENAI_API_KEY=<your-api-key>
AUTOBLOCKS_INGESTION_KEY=<your-ingestion-key>
```

## Run the app

```bash
poetry run python main.py
```

## View logs in Autoblocks

After you run the app, you will see a link to view the trace in your console. You can also navigate directly to the [explore page](https://app.autoblocks.ai/explore) to see the trace.

## More Information

For more information on how to use Autoblocks, visit the [Autoblocks documentation](https://docs.autoblocks.ai/).
