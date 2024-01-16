from datetime import datetime

import dotenv
from autoblocks.vendor.langchain import AutoblocksCallbackHandler
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.chains import LLMMathChain
from langchain.llms import OpenAI
from langchain.tools import Tool
from langchain.tools import tool

dotenv.load_dotenv("../.env")


@tool
def todays_date(args) -> int:
    """Returns today's date"""
    return datetime.now().day


if __name__ == "__main__":
    llm = OpenAI(temperature=0)
    llm_math_chain = LLMMathChain.from_llm(llm)
    tools = [
        Tool.from_function(
            func=llm_math_chain.run,
            name="Calculator",
            description="useful for when you need to answer questions about math",
        ),
        todays_date,
    ]
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    handler = AutoblocksCallbackHandler()
    output = agent.run(
        "What is today's date? What is that date divided by 2?",
        callbacks=[handler],
    )

    print(f"Output: {output}")
    print()
    print("View your trace: https://app.autoblocks.ai/explore")
