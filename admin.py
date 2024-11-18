# admin.py
import bcrypt
import streamlit as st
from hal_admin import main as hal_admin_main
from db_connection import connect_db


def admin_login():
    if 'is_authenticated' in st.session_state and st.session_state.is_authenticated:
        if st.session_state.user_type == 'admin':
            hal_admin_main()  
        return

    st.title("Login Admin")

    username = st.text_input("Username Admin", key="admin_username_input")
    password = st.text_input(
        "Password Admin", type="password", key="admin_password_input")

    if st.button("Login", key="admin_login_button"):
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM admin WHERE username = %s", (username,))
        admin = cursor.fetchone()

        if admin:
            try:
                input_password = password.encode('utf-8')
                stored_hash = admin[2].encode('utf-8')

                if bcrypt.checkpw(input_password, stored_hash):
                    st.session_state.user_id = admin[0]
                    st.session_state.is_authenticated = True
                    st.session_state.user_type = 'admin'
                    st.session_state.username = admin[1]
                    st.rerun()  
                else:
                    st.error("Password salah!")
            except Exception as e:
                st.error(f"Error saat verifikasi: {str(e)}")
        else:
            st.error("Username admin tidak ditemukan!")

        conn.close()

    if st.button("Kembali", key="admin_back_button"):
        st.session_state.login_type = None
        st.rerun()
