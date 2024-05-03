from my_project.prompts import FlashcardGeneratorPromptManager
from my_project.prompts import IsProfessionalToneEvalPromptManager
from my_project.prompts import IsSupportedByNotesEvalPromptManager
from my_project.prompts import StudyGuideOutlinePromptManager

flashcard_generator = FlashcardGeneratorPromptManager(
    minor_version="latest",
)

study_guide_outline = StudyGuideOutlinePromptManager(
    minor_version="latest",
)

is_professional_tone = IsProfessionalToneEvalPromptManager(
    minor_version="latest",
)

is_supported_by_notes = IsSupportedByNotesEvalPromptManager(
    minor_version="latest",
)
