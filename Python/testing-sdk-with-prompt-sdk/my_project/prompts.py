############################################################################
# This file was generated automatically by Autoblocks. Do not edit directly.
############################################################################

from enum import Enum
from typing import List  # noqa: F401
from typing import Union  # noqa: F401

import pydantic

from autoblocks.prompts.context import PromptExecutionContext
from autoblocks.prompts.manager import AutoblocksPromptManager
from autoblocks.prompts.models import FrozenModel
from autoblocks.prompts.renderer import TemplateRenderer


class FlashcardGeneratorParams(FrozenModel):
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    model: str = pydantic.Field(..., alias="model")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")


class FlashcardGeneratorTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "notes": "notes",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        notes: str,
    ) -> str:
        return self._render(
            "user",
            notes=notes,
        )


class FlashcardGeneratorExecutionContext(
    PromptExecutionContext[
        FlashcardGeneratorParams,
        FlashcardGeneratorTemplateRenderer,
    ],
):
    __params_class__ = FlashcardGeneratorParams
    __template_renderer_class__ = FlashcardGeneratorTemplateRenderer


class FlashcardGeneratorMinorVersion(Enum):
    v0 = "0"
    LATEST = "latest"


class FlashcardGeneratorPromptManager(
    AutoblocksPromptManager[
        FlashcardGeneratorExecutionContext,
        FlashcardGeneratorMinorVersion,
    ],
):
    __prompt_id__ = "flashcard-generator"
    __prompt_major_version__ = "1"
    __execution_context_class__ = FlashcardGeneratorExecutionContext


class IsProfessionalToneEvalParams(FrozenModel):
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    model: str = pydantic.Field(..., alias="model")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")


class IsProfessionalToneEvalTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "output": "output",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        output: str,
    ) -> str:
        return self._render(
            "user",
            output=output,
        )


class IsProfessionalToneEvalExecutionContext(
    PromptExecutionContext[
        IsProfessionalToneEvalParams,
        IsProfessionalToneEvalTemplateRenderer,
    ],
):
    __params_class__ = IsProfessionalToneEvalParams
    __template_renderer_class__ = IsProfessionalToneEvalTemplateRenderer


class IsProfessionalToneEvalMinorVersion(Enum):
    v0 = "0"
    LATEST = "latest"


class IsProfessionalToneEvalPromptManager(
    AutoblocksPromptManager[
        IsProfessionalToneEvalExecutionContext,
        IsProfessionalToneEvalMinorVersion,
    ],
):
    __prompt_id__ = "is-professional-tone-eval"
    __prompt_major_version__ = "1"
    __execution_context_class__ = IsProfessionalToneEvalExecutionContext


class IsSupportedByNotesEvalParams(FrozenModel):
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    model: str = pydantic.Field(..., alias="model")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")


class IsSupportedByNotesEvalTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "answer": "answer",
        "notes": "notes",
        "question": "question",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        answer: str,
        notes: str,
        question: str,
    ) -> str:
        return self._render(
            "user",
            answer=answer,
            notes=notes,
            question=question,
        )


class IsSupportedByNotesEvalExecutionContext(
    PromptExecutionContext[
        IsSupportedByNotesEvalParams,
        IsSupportedByNotesEvalTemplateRenderer,
    ],
):
    __params_class__ = IsSupportedByNotesEvalParams
    __template_renderer_class__ = IsSupportedByNotesEvalTemplateRenderer


class IsSupportedByNotesEvalMinorVersion(Enum):
    v0 = "0"
    v1 = "1"
    LATEST = "latest"


class IsSupportedByNotesEvalPromptManager(
    AutoblocksPromptManager[
        IsSupportedByNotesEvalExecutionContext,
        IsSupportedByNotesEvalMinorVersion,
    ],
):
    __prompt_id__ = "is-supported-by-notes-eval"
    __prompt_major_version__ = "1"
    __execution_context_class__ = IsSupportedByNotesEvalExecutionContext


class StudyGuideOutlineParams(FrozenModel):
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    model: str = pydantic.Field(..., alias="model")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")


class StudyGuideOutlineTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "topic": "topic",
    }

    def system(
        self,
    ) -> str:
        return self._render(
            "system",
        )

    def user(
        self,
        *,
        topic: str,
    ) -> str:
        return self._render(
            "user",
            topic=topic,
        )


class StudyGuideOutlineExecutionContext(
    PromptExecutionContext[
        StudyGuideOutlineParams,
        StudyGuideOutlineTemplateRenderer,
    ],
):
    __params_class__ = StudyGuideOutlineParams
    __template_renderer_class__ = StudyGuideOutlineTemplateRenderer


class StudyGuideOutlineMinorVersion(Enum):
    v0 = "0"
    LATEST = "latest"


class StudyGuideOutlinePromptManager(
    AutoblocksPromptManager[
        StudyGuideOutlineExecutionContext,
        StudyGuideOutlineMinorVersion,
    ],
):
    __prompt_id__ = "study-guide-outline"
    __prompt_major_version__ = "1"
    __execution_context_class__ = StudyGuideOutlineExecutionContext
