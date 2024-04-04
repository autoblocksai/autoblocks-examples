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

### Install Autoblocks CLI

See [Autoblocks CLI documentation](https://docs.autoblocks.ai/cli/setup)

### Install dependencies

```
npm install
```

## Run Autoblocks tests

### Set your Autoblocks API key

Retrieve your **local testing API key** from the [settings page](https://app.autoblocks.ai/settings/api-keys) and set it as an environment variable:

```bash
export AUTOBLOCKS_API_KEY=...
```

### Set your OpenAI API key

```bash
export OPENAI_API_KEY=...
```

### Run the tests

```bash
npx autoblocks testing exec -m "my first run" -- npm run start
```

You should see something like:

<img width="1107" alt="Screenshot 2024-03-01 at 5 53 27 PM" src="https://github.com/autoblocksai/autoblocks-examples/assets/7498009/92d50df8-7e9e-43dd-848c-f0711f20ce4b">

You can click on the links next to each test name to dig into more details.
You can also find all of your tests on the testing homepage in the [Autoblocks application](https://app.autoblocks.ai/testing/local).

### Managed test cases

After you have ran your first test following the instructions above, you will see a test suite created called **flashcard-generator-managed** in the UI. Visit the [Test Cases Page](https://app.autoblocks.ai/test-cases) and click on this test suite.

Create a new test case with the following JSON body.

```json
{
  "notes": "The Industrial Revolution, which began in Britain in the late 18th century, brought about significant changes in society, economy, and technology, leading to the transition from agrarian to industrial economies."
}
```

[Learn how to manage test cases](https://docs.autoblocks.ai/testing/test-case-management).

### Running tests with managed test cases

After adding test cases in the UI, uncomment where test cases are being fetched using our API client in `/src/test-suites/flashcard-generator-managed/index.ts`. Comment the existing hardcoded test.

Relevant code:

```typescript
const client = new AutoblocksAPIClient();

const { testCases: managedTestCases } = await client.getTestCases<TestCase>({
  testSuiteId: 'flashcard-generator-managed',
});

const testCases: TestCase[] = managedTestCases.map((testCase) => testCase.body);
```

Once updated, run the testing command again.

```bash
npx autoblocks testing exec -m "my second run" -- npm run start
```

You will now see test results for **flashcard-generator-managed** with the test cases you just setup in the UI.

## GitHub Actions setup

A starter workflow was added in [`.github/workflows/autoblocks-testing.yml`](./.github/workflows/autoblocks-testing.yml).
This workflow runs the tests on every push to the repository and also
on a daily schedule.

## Repo structure

```
src/
  run.ts <-- imports all tests from test-suites/ and runs them
  evaluators/ <-- all common evaluators are implemented here
    some-shared-evaluator1.ts
    some-shared-evaluator2.ts
  tasks/ <-- all "tasks" are implemented here
    task1.ts
    task2.ts
  test-suites/ <-- tests for each task
    task1/
      index.ts <-- implements the runner for task1
      evaluators.ts  <-- evaluators used only for task1
      test-cases.ts <-- contains test cases for task1
    task2/
      index.ts <-- implements the runner for task2
      evaluators.ts  <-- evaluators used only for task2
      test-cases.ts <-- contains test cases for task2
```

## Futher Reading

- [Autoblocks Testing documentation](https://docs.autoblocks.ai/testing/sdks)
