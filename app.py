import streamlit as st
import openai 
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

### langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Simplet chatbot"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions please repond as you are my teacher."),
    ("human", "Question:{question}"),
])

def generate_response(question,api_key,llm,temperature,max_tokens):
    # Set the OpenAI API key
    openai.api_key = api_key
    llm=ChatOpenAI(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain({"question": question})
    return answer

    # Create a ChatOpenAI instance with the specified parameters
    chat = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=api_key,
    )

    # Create a prompt template and format it with the question
    formatted_prompt = prompt.format_messages(question=question)

    # Generate a response using the LLM
    response = llm(formatted_prompt)
    
    return response


    