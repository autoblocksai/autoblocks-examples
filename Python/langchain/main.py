import dotenv
from autoblocks.vendor.langchain import AutoblocksCallbackHandler
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

dotenv.load_dotenv("../../.env")


if __name__ == "__main__":
    # This is an LLMChain to write a synopsis given a title of a play.
    synopsis_llm = OpenAI(temperature=0.7)
    synopsis_template = """You are a playwright. Given the title of a play, it is your job to write a synopsis for that title.

Title: {title}
Playwright: This is a synopsis for the above play:"""
    synopsis_prompt_template = PromptTemplate(input_variables=["title"], template=synopsis_template)
    synopsis_chain = LLMChain(llm=synopsis_llm, prompt=synopsis_prompt_template)

    # This is an LLMChain to write a review of a play given a synopsis.
    review_llm = OpenAI(temperature=0.7)
    review_template = """You are a play critic from the New York Times. Given the synopsis of a play, it is your job to write a review for that play.

Play Synopsis:
{synopsis}
Review from a New York Times play critic of the above play:"""
    review_prompt_template = PromptTemplate(input_variables=["synopsis"], template=review_template)
    review_chain = LLMChain(llm=review_llm, prompt=review_prompt_template)

    # This is the overall chain where we run these two chains in sequence.
    overall_chain = SimpleSequentialChain(chains=[synopsis_chain, review_chain])

    # Run the chain
    handler = AutoblocksCallbackHandler()
    review = overall_chain.run("Tragedy at sunset on the beach", callbacks=[handler])

    print("Review:")
    print(review)
