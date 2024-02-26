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


class OpenaiAssistantsExampleTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "account_level": "account_level",
        "name": "name",
        "question": "question",
    }

    def base_instructions(
        self,
    ) -> str:
        return self._render(
            "base-instructions",
        )

    def response_instructions(
        self,
        *,
        account_level: str,
        name: str,
    ) -> str:
        return self._render(
            "response-instructions",
            account_level=account_level,
            name=name,
        )

    def user(
        self,
        *,
        question: str,
    ) -> str:
        return self._render(
            "user",
            question=question,
        )


class OpenaiAssistantsExampleExecutionContext(
    PromptExecutionContext[
        None,
        OpenaiAssistantsExampleTemplateRenderer,
    ],
):
    __params_class__ = None
    __template_renderer_class__ = OpenaiAssistantsExampleTemplateRenderer

    @property
    def params(self) -> None:
        return None


class OpenaiAssistantsExampleMinorVersion(Enum):
    v0 = "0"
    LATEST = "latest"


class OpenaiAssistantsExamplePromptManager(
    AutoblocksPromptManager[
        OpenaiAssistantsExampleExecutionContext,
        OpenaiAssistantsExampleMinorVersion,
    ],
):
    __prompt_id__ = "openai-assistants-example"
    __prompt_major_version__ = "2"
    __execution_context_class__ = OpenaiAssistantsExampleExecutionContext
