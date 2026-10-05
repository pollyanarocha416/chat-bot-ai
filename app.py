from config import gemini_api_key, ai_url
import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(
    api_key=gemini_api_key,
    base_url=ai_url,
)

st.write("## ChatBot de IA")


if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

msg = st.chat_input("Escreva a mensagem aqui")

for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)


if msg:
    st.chat_message("user").write(msg)
    msg1 = {"role": "user", "content": msg}
    st.session_state["lista_mensagens"].append(msg1)

    reposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"], model="gemini-flash-lite-latest"
    )

    response_ai = reposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(response_ai)
    msg2 = {"role": "assistant", "content": response_ai}
    st.session_state["lista_mensagens"].append(msg2)

# audio_value = st.audio_input("Grave um audio :|")
# if audio_value:
#     st.audio(audio_value)
