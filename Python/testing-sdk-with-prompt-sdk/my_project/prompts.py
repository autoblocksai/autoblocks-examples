############################################################################
# This file was generated automatically by Autoblocks. Do not edit directly.
############################################################################

from typing import Any  # noqa: F401
from typing import Dict  # noqa: F401
from typing import Union  # noqa: F401

import pydantic  # noqa: F401

from autoblocks.prompts.context import PromptExecutionContext
from autoblocks.prompts.manager import AutoblocksPromptManager
from autoblocks.prompts.models import FrozenModel
from autoblocks.prompts.renderer import TemplateRenderer
from autoblocks.prompts.renderer import ToolRenderer


class FlashcardGeneratorParams(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    model: str = pydantic.Field(..., alias="model")


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


class FlashcardGeneratorToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class FlashcardGeneratorExecutionContext(
    PromptExecutionContext[
        FlashcardGeneratorParams,
        FlashcardGeneratorTemplateRenderer,
        FlashcardGeneratorToolRenderer,
    ],
):
    __params_class__ = FlashcardGeneratorParams
    __template_renderer_class__ = FlashcardGeneratorTemplateRenderer
    __tool_renderer_class__ = FlashcardGeneratorToolRenderer


class FlashcardGeneratorPromptManager(
    AutoblocksPromptManager[FlashcardGeneratorExecutionContext],
):
    __prompt_id__ = "flashcard-generator"
    __prompt_major_version__ = "1"
    __execution_context_class__ = FlashcardGeneratorExecutionContext


class IsProfessionalToneEvalParams(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    model: str = pydantic.Field(..., alias="model")


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


class IsProfessionalToneEvalToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class IsProfessionalToneEvalExecutionContext(
    PromptExecutionContext[
        IsProfessionalToneEvalParams,
        IsProfessionalToneEvalTemplateRenderer,
        IsProfessionalToneEvalToolRenderer,
    ],
):
    __params_class__ = IsProfessionalToneEvalParams
    __template_renderer_class__ = IsProfessionalToneEvalTemplateRenderer
    __tool_renderer_class__ = IsProfessionalToneEvalToolRenderer


class IsProfessionalToneEvalPromptManager(
    AutoblocksPromptManager[IsProfessionalToneEvalExecutionContext],
):
    __prompt_id__ = "is-professional-tone-eval"
    __prompt_major_version__ = "1"
    __execution_context_class__ = IsProfessionalToneEvalExecutionContext


class IsSupportedByNotesEvalParams(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    model: str = pydantic.Field(..., alias="model")


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


class IsSupportedByNotesEvalToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class IsSupportedByNotesEvalExecutionContext(
    PromptExecutionContext[
        IsSupportedByNotesEvalParams,
        IsSupportedByNotesEvalTemplateRenderer,
        IsSupportedByNotesEvalToolRenderer,
    ],
):
    __params_class__ = IsSupportedByNotesEvalParams
    __template_renderer_class__ = IsSupportedByNotesEvalTemplateRenderer
    __tool_renderer_class__ = IsSupportedByNotesEvalToolRenderer


class IsSupportedByNotesEvalPromptManager(
    AutoblocksPromptManager[IsSupportedByNotesEvalExecutionContext],
):
    __prompt_id__ = "is-supported-by-notes-eval"
    __prompt_major_version__ = "1"
    __execution_context_class__ = IsSupportedByNotesEvalExecutionContext


class StudyGuideOutlineParams(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    model: str = pydantic.Field(..., alias="model")


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


class StudyGuideOutlineToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class StudyGuideOutlineExecutionContext(
    PromptExecutionContext[
        StudyGuideOutlineParams,
        StudyGuideOutlineTemplateRenderer,
        StudyGuideOutlineToolRenderer,
    ],
):
    __params_class__ = StudyGuideOutlineParams
    __template_renderer_class__ = StudyGuideOutlineTemplateRenderer
    __tool_renderer_class__ = StudyGuideOutlineToolRenderer


class StudyGuideOutlinePromptManager(
    AutoblocksPromptManager[StudyGuideOutlineExecutionContext],
):
    __prompt_id__ = "study-guide-outline"
    __prompt_major_version__ = "1"
    __execution_context_class__ = StudyGuideOutlineExecutionContext
