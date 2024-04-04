import * as flashcardGenerator from './test-suites/flashcard-generator';
import * as studyGuideOutline from './test-suites/study-guide-outline';

(async () => {
  await Promise.all([
    flashcardGenerator.run(),
    studyGuideOutline.run(),
    // Uncomment after setting up managed test cases
    // for flashcard-generator
    // flashcardGenerator.runWithManagedTestCases(),
  ]);
})();
