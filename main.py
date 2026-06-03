from dotenv import load_dotenv
load_dotenv()


from langchain_core import __version__ as core_version
from importlib.metadata import version
lg_version = version("langgraph")
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic



def main():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = llm.invoke("What is the meaning of life?")
    print(f"Response from OpenAI: {response}")

    llm = ChatAnthropic(model="claude-sonnet-4-6", temperature=0)
    response = llm.invoke("Say setup is complete in one word")
    print(f"Response from Anthropic: {response}")


if __name__ == "__main__":
    main()
