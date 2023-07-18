from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import chainlit as cl

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=ChatOpenAI(temperature=0, streaming=True), verbose=True)

    return llm_chain