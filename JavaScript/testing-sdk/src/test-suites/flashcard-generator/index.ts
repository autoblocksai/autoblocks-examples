import { runTestSuite } from '@autoblocks/client/testing';
import { genTestCases, type TestCase } from './test-cases';
import { IsProfessionalTone, IsSupportedByNotes } from './evaluators';
import {
  genFlashcardsFromNotes,
  type Flashcard,
} from '../../tasks/flashcard-generator';

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
