const { run } = require('../src/index');

jest.setTimeout(60000);

const testInputs = [
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

  testInputs.map((input) => {
    it(`should return a response for "${input}"`, async () => {
      // Use the input as the traceId; this will make it so
      // we can compare the test runs against each other across
      // replay runs
      const traceId = input;

      await run({ input, traceId });
    });
  });
});
