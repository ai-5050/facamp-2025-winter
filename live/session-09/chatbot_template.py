import streamlit as st

st.title("⚽️ 나는 데이터로 축구한다")

with st.sidebar:
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        value=st.secrets["openai_api_key"],
    )

if prompt := st.chat_input("무엇이 궁금하세요?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.write("저는 완성되지 않은 Chatbot이라 잘 모르겠습니다ㅜㅜ")
