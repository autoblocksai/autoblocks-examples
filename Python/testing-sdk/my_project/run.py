from my_project.test_suites import flashcard_generator
from my_project.test_suites import study_guide_outline
from my_project.test_suites import flashcard_generator_managed


def run() -> None:
    # Autoblocks handles running these tests asynchronously behind the scenes
    # in a dedicated event loop, so no need to attempt to add any concurrency
    # here or use asyncio.run() or similar. Just simply call each test suite's
    # run() function and Autoblocks will handle the rest.
    flashcard_generator.run()
    study_guide_outline.run()
    # flashcard_generator_managed.run()
