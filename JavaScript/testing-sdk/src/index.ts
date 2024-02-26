import {
  runTestSuite,
  BaseTestEvaluator,
  Evaluation,
} from '@autoblocks/client/testing';

interface MyTestCase {
  x: number;
  y: number;
}

class MyTestEvaluator extends BaseTestEvaluator<MyTestCase, number> {
  id = 'my-test-evaluator';

  evaluateTestCase(testCase: MyTestCase, output: number): Evaluation {
    return {
      score: testCase.x + output,
      threshold: {
        gte: 0.3,
      },
    };
  }
}

const fn = (testCase: MyTestCase) => {
  return new Promise<number>((resolve) => {
    setTimeout(() => {
      resolve(testCase.y);
    }, 1_000);
  });
};

async function main() {
  await runTestSuite<MyTestCase, number>({
    id: 'my-test-suite',
    testCases: [
      { x: 0.1, y: 0.1 },
      { x: 0.2, y: 0.1 },
    ],
    testCaseHash: 'x',
    fn,
    evaluators: [new MyTestEvaluator()],
  });
}

main();
