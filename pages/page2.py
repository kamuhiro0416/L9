import streamlit as st

st.title("🔄 データリセット")

st.write("保持されているユーザー情報をリセットします")

if st.session_state.get('user_name'):
    st.info("現在保存されている情報:")
    st.write(f"名前:{st.session_state.get('user_name','未設定')}")
    st.write(f"学年:{st.session_state.get('user_grade','未設定')}")
    st.write(f"趣味:{','.join (st.session_state.get('user_hobbies','未設定'))}")

    if st.button("🗑️ すべての情報をリセット", type="primary"):
        st.session_state.user_name = ""
        st.session_state.user_grade = ""
        st.session_state.user_hobbies = ""
        st.success("✅　すべての情報をリセットしました")
        st.rerun()

    else:
        st.warning("リセットする情報がありません")