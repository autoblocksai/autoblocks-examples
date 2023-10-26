import dotenv

# Environment variables need to be loaded before we import
# trace_openai and openai
dotenv.load_dotenv(".env")

from autoblocks.vendor.openai import trace_openai
import openai


def main():
    # Call at the entrypoint to your application
    trace_openai()
    print("Automatically tracing all calls to OpenAI...")

    print("Calling OpenAI...")
    openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You answer questions about a software product named Acme."
            },
            {
                "role": "user",
                "content": "How do I sign up?"
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.7,
    )
    print("Finished calling OpenAI")
    print("View the trace at https://app.autoblocks.ai/explore")


if __name__ == "__main__":
    main()
