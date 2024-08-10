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


class TextSummarizationParams(FrozenModel):
    temperature: Union[float, int] = pydantic.Field(..., alias="temperature")
    top_p: Union[float, int] = pydantic.Field(..., alias="topP")
    frequency_penalty: Union[float, int] = pydantic.Field(..., alias="frequencyPenalty")
    presence_penalty: Union[float, int] = pydantic.Field(..., alias="presencePenalty")
    max_tokens: Union[float, int] = pydantic.Field(..., alias="maxTokens")
    model: str = pydantic.Field(..., alias="model")


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


class TextSummarizationToolRenderer(ToolRenderer):
    __name_mapper__ = {}


class TextSummarizationExecutionContext(
    PromptExecutionContext[
        TextSummarizationParams,
        TextSummarizationTemplateRenderer,
        TextSummarizationToolRenderer,
    ],
):
    __params_class__ = TextSummarizationParams
    __template_renderer_class__ = TextSummarizationTemplateRenderer
    __tool_renderer_class__ = TextSummarizationToolRenderer


class TextSummarizationPromptManager(
    AutoblocksPromptManager[TextSummarizationExecutionContext],
):
    __prompt_id__ = "text-summarization"
    __prompt_major_version__ = "1"
    __execution_context_class__ = TextSummarizationExecutionContext
