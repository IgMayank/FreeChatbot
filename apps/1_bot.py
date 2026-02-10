import streamlit as st
import os 
import sys
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = os.getenv("OPENROUTER_API_KEY"))

query = st.chat_input("Ask Anything")



def invoke(query):
    response = client.chat.completions.create(
    model="google/gemma-3-4b-it:free",
    messages=[{
        "role":"user" , "content": query
    }
    ]
)
    return response.choices[0].message.content

st.title("This is Your Chat buddy ")
st.markdown("Basic chatbot that have updated data till november 23 2023")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role =  message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = invoke(query)
    st.chat_message("ai").markdown(res)
    st.session_state.messages.append({"role":"ai","content":res}) 
