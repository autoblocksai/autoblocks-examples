import pytest

from main import run

test_cases = [
    "How do I sign up?",
    "How many pricing plans do you have?",
    "What is your refund policy?",
]


@pytest.mark.parametrize("content", test_cases)
def test_main(content: str):
    # Use the input as the trace_id; this will make it so
    # we can compare the runs against each other across replays.
    # If the input is too long to use as an identifier, we could
    # also update test_cases to be a list of dictionaries where one
    # field is the name of the test case and the other is the input.

    # Also prefix the trace_id with 'pytest -' since we're running jest
    # replays on the same branch and need to avoid conflicts in trace IDs.
    run(content=content, trace_id=f"pytest - {content}")
