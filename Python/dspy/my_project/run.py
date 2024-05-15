import dspy
from dspy.teleprompt import BootstrapFewShot
from my_project.config import config
from my_project.datasets import trainset
from my_project.datasets import metric
from my_project.models import LoggingOpenAI
from my_project.models import CoT


def run(question: str) -> dspy.Prediction:
    # Set up the LM
    turbo = LoggingOpenAI(model=config.value.model, max_tokens=250)
    dspy.settings.configure(lm=turbo)

    # Optimize! Use the `gsm8k_metric` here. In general, the metric is going to tell the optimizer how well it's doing.
    # In a production app, you would do the optimization ahead of time
    # and switch between optimized models depending on the configuration.
    teleprompter = BootstrapFewShot(
        metric=metric,
        max_bootstrapped_demos=config.value.max_bootstrapped_demos,
        max_labeled_demos=config.value.max_labeled_demos,
        max_rounds=config.value.max_rounds,
        max_errors=config.value.max_errors,
    )
    optimized_cot = teleprompter.compile(CoT(), trainset=trainset)
    # Run the question through the optimized model
    return optimized_cot(question=question)
