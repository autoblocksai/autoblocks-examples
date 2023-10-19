import dotenv
from autoblocks.vendor.langchain import AutoblocksCallbackHandler
from langchain.llms import OpenAI

dotenv.load_dotenv()


if __name__ == "__main__":
    llm = OpenAI()
    handler = AutoblocksCallbackHandler()
    llm.predict("hello, world!", callbacks=[handler])
