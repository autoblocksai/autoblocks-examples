import uuid
from flask import g
from autoblocks.tracer import AutoblocksTracer


def tracer():
    """
    `g` is a request-level global. If the tracer doesn't already exist,
    create a new one with a random trace ID.

    https://flask.palletsprojects.com/en/3.0.x/appcontext/#storing-data
    """
    if "tracer" not in g:
        g.tracer = AutoblocksTracer(trace_id=str(uuid.uuid4()))
    return g.tracer
