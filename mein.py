import streamlit as st

st.title("ユーザー情報入力")

if 'user_name' not in st.session_state:
    st.session_state.user_name=""

if 'user_grade' not in st.session_state:
    st.session_state.user_grade=""

if 'user_hobbies' not in st.session_state:
    st.session_state.user_hobbies=""

name = st.text_input("あなたの名前を入力してください")
grade = st.selectbox("あなたの学年を選んでください",
                     ["小学４年生","小学５年生","小学６年生","中学１年生","中学２年生","中学３年生"])
hobbies = st.multiselect("あなたの趣味を選んでください",
                         ["読書","運動","ゲーム","音楽","絵画","その他"])
if st.button("情報を保持"):
    st.session_state.user_name = name 
    st.session_state.user_grade=grade
    st.session_state.user_hobbies= hobbies
    st.success("情報を保持しました")