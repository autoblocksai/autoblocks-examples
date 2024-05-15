import os
import uuid
import dspy
from autoblocks.tracer import AutoblocksTracer


tracer = AutoblocksTracer(
    os.environ["AUTOBLOCKS_INGESTION_KEY"],
)


class LoggingOpenAI(dspy.OpenAI):
    """Extend the OpenAI class from DSPy to log requests and responses to Autoblocks."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def basic_request(self, prompt: str, **kwargs):
        trace_id = str(uuid.uuid4())
        tracer.send_event(
            "ai.request",
            trace_id=trace_id,
            properties={
                "prompt": prompt,
                **self.kwargs,
                **kwargs,
            },
        )
        response = super().basic_request(prompt=prompt, **kwargs)
        tracer.send_event("ai.response", trace_id=trace_id, properties=response)
        return response


class CoT(dspy.Module):
    def __init__(self):
        super().__init__()
        self.prog = dspy.ChainOfThought("question -> answer")

    def forward(self, question):
        return self.prog(question=question)
