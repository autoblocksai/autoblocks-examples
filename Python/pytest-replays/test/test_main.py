import pytest

from src.main import run

test_cases = [
    "Where can I find your privacy policy?",
    "Are you SOC2 compliant?",
    "How many users do you have?",
]


@pytest.mark.parametrize("content", test_cases)
def test_main(content: str):
    # Use the input as the trace_id; this will make it so
    # we can compare the runs against each other across replays.
    # If the input is too long to use as an identifier, we could
    # also update test_cases to be a list of dictionaries where one
    # field is the name of the test case and the other is the input.
    run(content=content, trace_id=content)
