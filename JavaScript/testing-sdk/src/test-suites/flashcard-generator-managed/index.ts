import { runTestSuite } from '@autoblocks/client/testing';
import { type TestCase } from '../flashcard-generator/test-cases';
import {
  IsProfessionalTone,
  IsSupportedByNotes,
} from '../flashcard-generator/evaluators';
import {
  genFlashcardsFromNotes,
  type Flashcard,
} from '../../tasks/flashcard-generator';
import { AutoblocksAPIClient } from '@autoblocks/client';

const TEST_SUITE_ID = 'flashcard-generator-managed';

export async function run() {
  const inCodeTestCases = [{ notes: 'Initial test case' }];
  let managedTestCases: TestCase[] = [];

  try {
    const client = new AutoblocksAPIClient();

    const response = await client.getTestCases<TestCase>({
      testSuiteId: TEST_SUITE_ID,
    });
    managedTestCases = response.testCases.map((testCase) => testCase.body);
  } catch {
    console.warn('Test suite does not exist yet,');
  }

  await runTestSuite<TestCase, Flashcard[]>({
    id: TEST_SUITE_ID,
    testCases: [...managedTestCases, ...inCodeTestCases],
    testCaseHash: ['notes'],
    evaluators: [new IsProfessionalTone(), new IsSupportedByNotes()],
    fn: (args: { testCase: TestCase }) =>
      genFlashcardsFromNotes(args.testCase.notes),
    maxTestCaseConcurrency: 5,
  });
}
