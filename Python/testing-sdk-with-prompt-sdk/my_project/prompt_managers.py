from my_project.prompts import FlashcardGeneratorMinorVersion
from my_project.prompts import FlashcardGeneratorPromptManager
from my_project.prompts import IsProfessionalToneEvalMinorVersion
from my_project.prompts import IsProfessionalToneEvalPromptManager
from my_project.prompts import IsSupportedByNotesEvalMinorVersion
from my_project.prompts import IsSupportedByNotesEvalPromptManager
from my_project.prompts import StudyGuideOutlineMinorVersion
from my_project.prompts import StudyGuideOutlinePromptManager

flashcard_generator = FlashcardGeneratorPromptManager(
    minor_version=FlashcardGeneratorMinorVersion.LATEST,
)

study_guide_outline = StudyGuideOutlinePromptManager(
    minor_version=StudyGuideOutlineMinorVersion.LATEST,
)

is_professional_tone = IsProfessionalToneEvalPromptManager(
    minor_version=IsProfessionalToneEvalMinorVersion.LATEST,
)

is_supported_by_notes = IsSupportedByNotesEvalPromptManager(
    minor_version=IsSupportedByNotesEvalMinorVersion.LATEST,
)
