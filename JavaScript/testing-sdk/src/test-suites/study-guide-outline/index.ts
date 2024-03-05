import { runTestSuite } from '@autoblocks/client/testing';
import { genTestCases, type TestCase } from './test-cases';
import { Formatting, NumCategories, HasSubstrings } from './evaluators';
import { genStudyGuideOutline } from '../../tasks/study-guide-outline';

export async function run() {
  await runTestSuite<TestCase, string>({
    id: 'study-guide-outline',
    testCases: genTestCases(),
    testCaseHash: ['topic'],
    evaluators: [new Formatting(), new NumCategories(), new HasSubstrings()],
    fn: (args: { testCase: TestCase }) =>
      genStudyGuideOutline(args.testCase.topic),
    maxTestCaseConcurrency: 5,
  });
}
