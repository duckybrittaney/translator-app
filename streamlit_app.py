import openai
import streamlit as st
import json
from openai import OpenAI

openai.api_key = st.secrets["key"]
system_prompt = '''
You are a language translator. A user will give you an input language, an output language, and the text they want translated. Output ONLY their translated message.
'''

def chat(inp,outp,txt):
    user_prompt = f'{inp} -> {outp}, my message is: {txt}'
    response = client.chat.completions.create(model = 'gpt-3.5-turbo-0125',
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt},
    ])
    if submit:
        st.write('Translated text:')
        st.write(response.choices[0].message.content)

st.title("Translator")

with st.form('my_form'):
    input_lan = st.selectbox(
        "Select an input language",
        [
            "Spanish",
            "English",
            "Italian",
        ]
    )
    output_lan = st.selectbox(
        "Select an output language",
        [
            "Mandarin",
            "French",
            "German",
        ]
    )
    text = st.text_input("Type in the text to translate")


    submit = st.form_submit_button('Submit')
    chat(input_lan, output_lan, text)
