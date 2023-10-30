import pytest

from main import run

test_cases = [
    "How do I sign up?",
    "How many pricing plans do you have?",
    "What is your refund policy?",
]


@pytest.mark.parametrize("content", test_cases)
def test_main(content: str):
    run(content=content, trace_id=content)
