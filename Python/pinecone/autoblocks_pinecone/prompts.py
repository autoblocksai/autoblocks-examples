############################################################################
# This file was generated automatically by Autoblocks. Do not edit directly.
############################################################################

from typing import Union  # noqa: F401

import pydantic  # noqa: F401

from autoblocks.prompts.context import PromptExecutionContext
from autoblocks.prompts.manager import AutoblocksPromptManager
from autoblocks.prompts.models import FrozenModel
from autoblocks.prompts.renderer import TemplateRenderer


class EvalComprehensivenessParams(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class EvalComprehensivenessTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "existing_treatment_plan": "existing_treatment_plan",
        "generated_plan": "generated_plan",
        "medical_records": "medical_records",
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
        existing_treatment_plan: str,
        generated_plan: str,
        medical_records: str,
    ) -> str:
        return self._render(
            "user",
            existing_treatment_plan=existing_treatment_plan,
            generated_plan=generated_plan,
            medical_records=medical_records,
        )


class EvalComprehensivenessExecutionContext(
    PromptExecutionContext[
        EvalComprehensivenessParams,
        EvalComprehensivenessTemplateRenderer,
    ],
):
    __params_class__ = EvalComprehensivenessParams
    __template_renderer_class__ = EvalComprehensivenessTemplateRenderer


class EvalComprehensivenessPromptManager(
    AutoblocksPromptManager[EvalComprehensivenessExecutionContext],
):
    __prompt_id__ = "eval-comprehensiveness"
    __prompt_major_version__ = "1"
    __execution_context_class__ = EvalComprehensivenessExecutionContext


class EvalCorrectnessParams(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class EvalCorrectnessTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "transcript": "transcript",
        "treatment_plan": "treatment_plan",
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
        transcript: str,
        treatment_plan: str,
    ) -> str:
        return self._render(
            "user",
            transcript=transcript,
            treatment_plan=treatment_plan,
        )


class EvalCorrectnessExecutionContext(
    PromptExecutionContext[
        EvalCorrectnessParams,
        EvalCorrectnessTemplateRenderer,
    ],
):
    __params_class__ = EvalCorrectnessParams
    __template_renderer_class__ = EvalCorrectnessTemplateRenderer


class EvalCorrectnessPromptManager(
    AutoblocksPromptManager[EvalCorrectnessExecutionContext],
):
    __prompt_id__ = "eval-correctness"
    __prompt_major_version__ = "1"
    __execution_context_class__ = EvalCorrectnessExecutionContext


class EvalFaithfulnessParams(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class EvalFaithfulnessTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "existing_treatment_plan": "existing_treatment_plan",
        "generated_plan": "generated_plan",
        "medical_records": "medical_records",
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
        existing_treatment_plan: str,
        generated_plan: str,
        medical_records: str,
    ) -> str:
        return self._render(
            "user",
            existing_treatment_plan=existing_treatment_plan,
            generated_plan=generated_plan,
            medical_records=medical_records,
        )


class EvalFaithfulnessExecutionContext(
    PromptExecutionContext[
        EvalFaithfulnessParams,
        EvalFaithfulnessTemplateRenderer,
    ],
):
    __params_class__ = EvalFaithfulnessParams
    __template_renderer_class__ = EvalFaithfulnessTemplateRenderer


class EvalFaithfulnessPromptManager(
    AutoblocksPromptManager[EvalFaithfulnessExecutionContext],
):
    __prompt_id__ = "eval-faithfulness"
    __prompt_major_version__ = "1"
    __execution_context_class__ = EvalFaithfulnessExecutionContext


class EvalRelevancyParams(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class EvalRelevancyTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "medical_record": "medical_record",
        "treatment_plan": "treatment_plan",
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
        medical_record: str,
        treatment_plan: str,
    ) -> str:
        return self._render(
            "user",
            medical_record=medical_record,
            treatment_plan=treatment_plan,
        )


class EvalRelevancyExecutionContext(
    PromptExecutionContext[
        EvalRelevancyParams,
        EvalRelevancyTemplateRenderer,
    ],
):
    __params_class__ = EvalRelevancyParams
    __template_renderer_class__ = EvalRelevancyTemplateRenderer


class EvalRelevancyPromptManager(
    AutoblocksPromptManager[EvalRelevancyExecutionContext],
):
    __prompt_id__ = "eval-relevancy"
    __prompt_major_version__ = "1"
    __execution_context_class__ = EvalRelevancyExecutionContext


class GenPersonalizedTreatmentPlanParams(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class GenPersonalizedTreatmentPlanTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "existing_treatment_plan": "existing_treatment_plan",
        "medical_records": "medical_records",
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
        existing_treatment_plan: str,
        medical_records: str,
    ) -> str:
        return self._render(
            "user",
            existing_treatment_plan=existing_treatment_plan,
            medical_records=medical_records,
        )


class GenPersonalizedTreatmentPlanExecutionContext(
    PromptExecutionContext[
        GenPersonalizedTreatmentPlanParams,
        GenPersonalizedTreatmentPlanTemplateRenderer,
    ],
):
    __params_class__ = GenPersonalizedTreatmentPlanParams
    __template_renderer_class__ = GenPersonalizedTreatmentPlanTemplateRenderer


class GenPersonalizedTreatmentPlanPromptManager(
    AutoblocksPromptManager[GenPersonalizedTreatmentPlanExecutionContext],
):
    __prompt_id__ = "gen-personalized-treatment-plan"
    __prompt_major_version__ = "1"
    __execution_context_class__ = GenPersonalizedTreatmentPlanExecutionContext


class GenTreatmentPlanParams(FrozenModel):
    model: str = pydantic.Field(..., alias="model")


class GenTreatmentPlanTemplateRenderer(TemplateRenderer):
    __name_mapper__ = {
        "transcript": "transcript",
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
        transcript: str,
    ) -> str:
        return self._render(
            "user",
            transcript=transcript,
        )


class GenTreatmentPlanExecutionContext(
    PromptExecutionContext[
        GenTreatmentPlanParams,
        GenTreatmentPlanTemplateRenderer,
    ],
):
    __params_class__ = GenTreatmentPlanParams
    __template_renderer_class__ = GenTreatmentPlanTemplateRenderer


class GenTreatmentPlanPromptManager(
    AutoblocksPromptManager[GenTreatmentPlanExecutionContext],
):
    __prompt_id__ = "gen-treatment-plan"
    __prompt_major_version__ = "1"
    __execution_context_class__ = GenTreatmentPlanExecutionContext
