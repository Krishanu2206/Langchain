import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", json={'input' : {'topic' : input_text}})
    print(response.json())
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", json={'input' : {'topic' : input_text}})
    print(response.json())
    return response.json()['output']

##streamlit framework
st.title("Langchain Chatbot")
input_text_essay = st.text_area("Enter your topic for essay")
input_text_poem = st.text_area("Enter your topic for poem")

if input_text_essay:
    st.write(get_openai_response(input_text_essay))

if input_text_poem:
    st.write(get_ollama_response(input_text_poem))