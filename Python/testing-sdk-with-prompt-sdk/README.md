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

## Setup

### Install [`poetry`](https://python-poetry.org/)

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### Install Autoblocks CLI

See [Autoblocks CLI docs](https://docs.autoblocks.ai/cli/setup)

### Install dependencies

```
poetry install
```

## Create your prompts

### Create study-guide-outline prompt

Go to https://app.autoblocks.ai/prompts and click on Create Prompt.

Name the prompt `study-guide-outline`.

> **_NOTE:_** This matches the name in [`./.autoblocks.yml`](./.autoblocks.yml).

Add parameters and select `gpt-3.5-turbo` as the model and set Max Tokens to at least `1000`. Feel free to modify any of the other parameters as well..

> **_NOTE:_** You can experiment with different models and params.

Add a template named `system` and add the following text:

```
Generate a study guide outline for a given topic.
It should be a bulleted list with just the title of each category.
The top level bullets should be stars: *
The second level bullets should be dashes: -
The second level dashes should have two spaces before them.
The study guide should be no more than two levels deep.
There should be between five and ten top-level categories.
```

Add a template named `user` and add the following text:

```
Topic: {{ topic }}
```

Deploy your prompt.

### Create flashcard-generator prompt

Go to https://app.autoblocks.ai/prompts and click on Create Prompt.

Name the prompt `flashcard-generator`.

> **_NOTE:_** This matches the name in [`./.autoblocks.yml`](./.autoblocks.yml).

Add parameters and select `gpt-3.5-turbo` as the model and set Max Tokens to at least `1000`. Feel free to modify any of the other parameters as well.

> **_NOTE:_** You can experiment with different models and params.

Add a template named `system` and add the following text:

```
Given a user's notes, generate flashcards that will allow the user to study those notes.

Your first task is to identify the facts or key points in the notes.
Then, create a flashcard for each fact or key point.
The front of the flashcard should be a question, and the back of the flashcard should be the answer to that question.
Each flashcard should be supported by content from the notes.
Ignore the tone of the notes and always make the flashcards in a professional tone.
Ignore any subjective commentary in the notes and only focus on the facts or key points.
Return the results as JSON in the below format:

'''
{
  "cards": [
    {
      "front": "What is the capital of France?",
      "back": "Paris"
    },
    {
      "front": "Who painted the Mona Lisa?",
      "back": "Leonardo da Vinci"
    }
  ]
}
'''

Only return JSON in your response, nothing else. Do not include the backticks.

Example:

Notes:

'''
Am. History Notes 🇺🇸
Beginnings & Stuff
Columbus 1492, "found" America but actually not the first.
Native Americans were here first, tons of diff cultures.
Colonies & Things
13 Colonies cuz Brits wanted $ and land.
Taxation w/o Representation = Colonists mad at British taxes, no say in gov.
Boston Tea Party = Tea in the harbor, major protest.
Revolution Time
Declaration of Independence, 1776, basically "we're breaking up with you, Britain".
George Washington = First pres, war hero.
Moving West
Manifest Destiny = Idea that the US was supposed to own all land coast to coast.
Louisiana Purchase, 1803, Thomas Jefferson bought a ton of land from France.
'''

Flashcards:

{
  "cards": [
    {
      "front": "Who was the first president of the United States?",
      "back": "George Washington"
    },
    {
      "front": "What was the idea that the US was supposed to own all land coast to coast?",
      "back": "Manifest Destiny"
    },
    {
      "front": "What was the year of the Louisiana Purchase?",
      "back": "1803"
    }
  ]
}
```

Add a template named `user` and add the following text:

```
Notes:

'''
{{ notes }}
'''

Flashcards:
```

Deploy your prompt.

### Create is-supported-by-notes-eval prompt

Go to https://app.autoblocks.ai/prompts and click on Create Prompt.

Name the prompt `is-supported-by-notes-eval`.

> **_NOTE:_** This matches the name in [`./.autoblocks.yml`](./.autoblocks.yml).

Add parameters and select `gpt-3.5-turbo` as the model.

> **_NOTE:_** You can experiment with different models and params.

Add a template named `system` and add the following text:

```
Given some notes by a student and a flashcard in the form of a question and answer, evaluate whether the flashcard's question and answer are supported by the notes.
It's possible the question and answer aren't in the notes verbatim.
If the notes provide enough context or information to support the question and answer, consider that sufficient support.
Based on these criteria, provide a binary response where:
0 indicates the flashcard's question and answer are not supported by the notes.
1 indicates the flashcard's question and answer are supported by the notes.
No further explanation or summary is required; just provide the number that represents your assessment.
```

Add a template named `user` and add the following text:

```
Notes:

'''
{{ notes }}
'''

Flashcard:

Question: {{ question }}
Answer: {{ answer }}
```

Deploy your prompt.

### Create is-professional-tone-eval prompt

Go to https://app.autoblocks.ai/prompts and click on Create Prompt.

Name the prompt `is-professional-tone-eval`.

> **_NOTE:_** This matches the name in [`./.autoblocks.yml`](./.autoblocks.yml).

Add parameters and select `gpt-3.5-turbo` as the model.

> **_NOTE:_** You can experiment with different models and params.

Add a template named `system` and add the following text:

```
Please evaluate the provided text for its professionalism in the context of formal communication.
Consider the following criteria in your assessment:

Language Use: Formality, clarity, and precision of language without slang or casual expressions.
Sentence Structure: Logical and well-formed sentence construction without run-ons or fragments.
Tone and Style: Respectful, objective, and appropriately formal tone without bias or excessive emotionality.
Grammar and Punctuation: Correct grammar, punctuation, and capitalization.
Based on these criteria, provide a binary response where:

0 indicates the text does not maintain a professional tone.
1 indicates the text maintains a professional tone.
No further explanation or summary is required; just provide the number that represents your assessment.
```

Add a template named `user` and add the following text:

```
{{ output }}
```

Deploy your prompt.

### Create your `.autoblocks.yml` file

This file instructs the CLI which prompts and which of their versions
to autogenerate code for. One has already been created for you in [`./.autoblocks.yml`](./.autoblocks.yml).

### Set your Autoblocks API key

Retrieve your **local testing API key** from the [settings page](https://app.autoblocks.ai/settings/api-keys) and set it as an environment variable:

```bash
export AUTOBLOCKS_API_KEY=...
```

### Autogenerate prompt classes

This CLI will autogenerate classes for you to use to interact with the prompts you've created in the UI.

```
poetry run prompts generate
```

## Run Autoblocks tests

### Set your OpenAI API key

```bash
export OPENAI_API_KEY=...
```

### Run the tests

```bash
npx autoblocks testing exec -m "my first run" -- poetry run start
```

You should see something like:

<img width="1668" alt="Screenshot 2024-02-22 at 1 23 50 PM" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/ded25aa8-1439-432d-86a6-7254b27b970b">

You can click on the links next to each test name to dig into more details.
You can also find all of your tests on the testing homepage in the [Autoblocks application](https://app.autoblocks.ai/testing/local).

## GitHub Actions setup

A starter workflow was added in [`.github/workflows/autoblocks-testing.yml`](./.github/workflows/autoblocks-testing.yml).
This workflow runs the tests on every push to the repository and also
on a daily schedule.

## Repo structure

```
my_project/
  run.py <-- imports all tests from test_suites/ and runs them
  evaluators/ <-- all common evaluators are implemented here
    some_shared_evaluator1.py
    some_shared_evaluator2.py
  tasks/ <-- all "tasks" are implemented here
    task1.py
    task2.py
  test_suites/ <-- tests for each task
    task1/
      __init__.py <-- implements the runner for task1
      evaluators.py  <-- evaluators used only for task1
      test_cases.py <-- contains test cases for task1
    task2/
      __init__.py <-- implements the runner for task2
      evaluators.py  <-- evaluators used only for task2
      test_cases.py <-- contains test cases for task2
```

## Futher Reading

- [Autoblocks Testing documentation](https://docs.autoblocks.ai/testing/sdks)
