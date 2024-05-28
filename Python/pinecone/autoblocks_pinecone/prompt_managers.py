from autoblocks_pinecone.prompts import EvalComprehensivenessPromptManager
from autoblocks_pinecone.prompts import EvalFaithfulnessPromptManager
from autoblocks_pinecone.prompts import GenPersonalizedTreatmentPlanPromptManager
from autoblocks_pinecone.prompts import GenTreatmentPlanPromptManager
from autoblocks_pinecone.prompts import EvalCorrectnessPromptManager
from autoblocks_pinecone.prompts import EvalRelevancyPromptManager

eval_comprehensiveness = EvalComprehensivenessPromptManager(minor_version="latest")

eval_faithfulness = EvalFaithfulnessPromptManager(minor_version="latest")

eval_correctness = EvalCorrectnessPromptManager(minor_version="latest")

eval_relevancy = EvalRelevancyPromptManager(minor_version="latest")

gen_treatment_plan = GenTreatmentPlanPromptManager(minor_version="latest")

gen_personalized_treatment_plan = GenPersonalizedTreatmentPlanPromptManager(
    minor_version="latest"
)
