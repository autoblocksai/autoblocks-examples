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

export async function run() {
  // Uncomment following block to start using managed test cases
  /* const client = new AutoblocksAPIClient();

  const { testCases: managedTestCases } = await client.getTestCases<TestCase>({
    testSuiteId: 'flashcard-generator-managed',
  });

  const testCases: TestCase[] = managedTestCases.map(
    (testCase) => testCase.body,
  ); */

  // Comment this line once you have created test cases for
  // this test suite
  const testCases = [{ notes: 'Initial test case' }];

  await runTestSuite<TestCase, Flashcard[]>({
    id: 'flashcard-generator-managed',
    testCases,
    testCaseHash: ['notes'],
    evaluators: [new IsProfessionalTone(), new IsSupportedByNotes()],
    fn: (args: { testCase: TestCase }) =>
      genFlashcardsFromNotes(args.testCase.notes),
    maxTestCaseConcurrency: 5,
  });
}
