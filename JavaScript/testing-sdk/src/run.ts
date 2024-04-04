import * as flashcardGenerator from './test-suites/flashcard-generator';
import * as studyGuideOutline from './test-suites/study-guide-outline';
import * as flashcardGeneratorManaged from './test-suites/flashcard-generator-managed';

(async () => {
  await Promise.all([
    flashcardGenerator.run(),
    studyGuideOutline.run(),
    flashcardGenerator.run(),
  ]);
})();
