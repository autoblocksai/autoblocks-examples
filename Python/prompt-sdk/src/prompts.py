############################################################################
# This file was generated automatically by Autoblocks. Do not edit directly.
############################################################################

from typing import Union  # noqa: F401

import pydantic  # noqa: F401

from autoblocks.prompts.context import PromptExecutionContext
from autoblocks.prompts.manager import AutoblocksPromptManager
from autoblocks.prompts.models import FrozenModel
from autoblocks.prompts.renderer import TemplateRenderer


class TextSummarizationParams(FrozenModel):
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    model: str = pydantic.Field(..., alias="model")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")


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


class TextSummarizationPromptManager(
    AutoblocksPromptManager[TextSummarizationExecutionContext],
):
    __prompt_id__ = "text-summarization"
    __prompt_major_version__ = "1"
    __execution_context_class__ = TextSummarizationExecutionContext
