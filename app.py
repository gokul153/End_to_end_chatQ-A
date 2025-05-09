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

    # # Create a ChatOpenAI instance with the specified parameters
    # chat = ChatOpenAI(
    #     model="gpt-3.5-turbo",
    #     temperature=temperature,
    #     max_tokens=max_tokens,
    #     openai_api_key=api_key,
    # )

    # # Create a prompt template and format it with the question
    # formatted_prompt = prompt.format_messages(question=question)

    # # Generate a response using the LLM
    # response = llm(formatted_prompt)
    
    # return response

st.title("Enhanced Q & A Chat bot with OpenAI")

## Sidebar for settings 
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter you open AI key")


llm = st.sidebar.selectbox("Select a model",["gpt-4o,gpt-4-turbo","gpt-4"])

## adjust the parameter 
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_token = st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

## main inteface for user input 
st.write("Go ahead  and ask any question")
user_input = st.text_input("You :")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_token)
    st.write(response)
else:
    st.write("please provide the query")    



    