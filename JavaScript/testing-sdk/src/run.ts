import * as flashcardGenerator from './test-suites/flashcard-generator';
import * as studyGuideOutline from './test-suites/study-guide-outline';

(async () => {
  await Promise.all([flashcardGenerator.run(), studyGuideOutline.run()]);
})();
