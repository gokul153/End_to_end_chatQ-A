import streamlit as st
import openai 
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
from dotenv import load_dotenv

load_dotenv()

### langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Simplet chatbot"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant that answers questions please repond as you are my teacher."),
    ("human", "Question:{question}"),
])
def generate_response_new(question, llm, temperature, max_tokens):
    llm=Ollama(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer



def generate_response(question,api_key,llm,temperature,max_tokens):
    # Set the OpenAI API key
    openai.api_key = api_key
    llm=ChatOpenAI(model=llm)
    output_parser = StrOutputParser()
    chain = prompt|llm|output_parser
    answer = chain({"question": question})
    return answer

    
 # Title of the app  
st.title("Simple Q&A Chatbot With OpenAI")
st.write("This is a simple Q&A chatbot using OpenAI's GPT-3.5-turbo model.")
## Select the OpenAI model
llm=st.sidebar.selectbox("Select Open Source model",["mistral","gemma:2b"])

## Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## MAin interface for user input
st.write("Goe ahead and ask any question")
user_input=st.text_input("You:")



if user_input :
    print("user input",user_input,"llm",llm,"temperature",temperature,"max_tokens",max_tokens)
    response=generate_response_new(user_input,llm,temperature,max_tokens)
    print("response",response)
    st.write(response)
else:
    st.write("Please provide the user input")


    