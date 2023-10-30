const { run } = require('./run');

// Simulate running the `run` function in a production setting,
// i.e. without passing in a traceId from a test case (one will
// be auto-generated).
async function main() {
  await run({ input: 'How do I sign up?' });
}

main();
