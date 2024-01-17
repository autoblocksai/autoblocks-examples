############################################################################
# This file was generated automatically by Autoblocks. Do not edit directly.
############################################################################

from enum import Enum
from typing import List  # noqa: F401

import pydantic

from autoblocks.prompts.context import PromptExecutionContext
from autoblocks.prompts.manager import AutoblocksPromptManager
from autoblocks.prompts.models import FrozenModel
from autoblocks.prompts.renderer import TemplateRenderer


class TextSummarizationParams(FrozenModel):
    top_p: float = pydantic.Field(..., alias="topP")
    model: str = pydantic.Field(..., alias="model")
    max_tokens: float = pydantic.Field(..., alias="maxTokens")
    temperature: float = pydantic.Field(..., alias="temperature")
    presence_penalty: float = pydantic.Field(..., alias="presencePenalty")
    frequency_penalty: float = pydantic.Field(..., alias="frequencyPenalty")


class TextSummarizationTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "document": "document",
        "language": "language",
        "languageRequirement": "language_requirement",
        "tone": "tone",
        "toneRequirement": "tone_requirement",
    }

    def system(
        self,
        *,
        language_requirement: str,
        tone_requirement: str,
    ) -> str:
        return self._render(
            "system",
            language_requirement=language_requirement,
            tone_requirement=tone_requirement,
        )

    def user(
        self,
        *,
        document: str,
    ) -> str:
        return self._render(
            "user",
            document=document,
        )

    def util_language(
        self,
        *,
        language: str,
    ) -> str:
        return self._render(
            "util/language",
            language=language,
        )

    def util_tone(
        self,
        *,
        tone: str,
    ) -> str:
        return self._render(
            "util/tone",
            tone=tone,
        )


class TextSummarizationExecutionContext(
    PromptExecutionContext[
        TextSummarizationParams,
        TextSummarizationTemplateRenderer,
    ],
):
    __params_class__ = TextSummarizationParams
    __template_renderer_class__ = TextSummarizationTemplateRenderer


class TextSummarizationMinorVersion(Enum):
    v0 = "0"
    v1 = "1"
    LATEST = "latest"


class TextSummarizationPromptManager(
    AutoblocksPromptManager[
        TextSummarizationExecutionContext,
        TextSummarizationMinorVersion,
    ],
):
    __prompt_id__ = "text-summarization"
    __prompt_major_version__ = "1"
    __execution_context_class__ = TextSummarizationExecutionContext
