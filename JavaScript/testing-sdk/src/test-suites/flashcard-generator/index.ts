import { runTestSuite } from '@autoblocks/client/testing';
import { genTestCases, type TestCase } from './test-cases';
import { IsProfessionalTone, IsSupportedByNotes } from './evaluators';
import {
  genFlashcardsFromNotes,
  type Flashcard,
} from '../../tasks/flashcard-generator';
import { AutoblocksAPIClient } from '@autoblocks/client';

export async function run() {
  await runTestSuite<TestCase, Flashcard[]>({
    id: 'flashcard-generator',
    testCases: genTestCases(),
    testCaseHash: ['notes'],
    evaluators: [new IsProfessionalTone(), new IsSupportedByNotes()],
    fn: (args: { testCase: TestCase }) =>
      genFlashcardsFromNotes(args.testCase.notes),
    maxTestCaseConcurrency: 5,
  });
}

export async function runWithManagedTestCases() {
  const client = new AutoblocksAPIClient();

  const { testCases: managedTestCases } = await client.getTestCases<TestCase>({
    testSuiteId: 'flashcard-generator',
  });

  const testCases: TestCase[] = managedTestCases.map(
    (testCase) => testCase.body,
  );

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
