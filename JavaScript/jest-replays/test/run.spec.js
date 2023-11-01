const { run } = require('../src/run');

jest.setTimeout(60000);

const testCases = [
  'How do I sign up?',
  'How many pricing plans do you have?',
  'What is your refund policy?',
];

describe('run', () => {
  afterAll(() => {
    if (process.env.CI) {
      console.log(`View your replay at https://app.autoblocks.ai/replays`);
    } else {
      console.log(
        `View your replay at https://app.autoblocks.ai/replays/local/run/${process.env.AUTOBLOCKS_REPLAY_ID}`,
      );
    }
  });

  testCases.map((input) => {
    it(`should return a response for "${input}"`, async () => {
      // Use the input as the traceId; this will make it so
      // we can compare the runs against each other across replays.
      // If the input is too long to use as an identifier, we could
      // also update testCases to be a list of objects where one
      // field is the name of the test case and the other is the input.

      // Also prefix the traceId with 'jest -' since we're running pytest
      // replays on the same branch and need to avoid conflicts in traceIds.
      await run({ input, traceId: `jest - ${input}` });
    });
  });
});
