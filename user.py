import bcrypt
import streamlit as st
from hal_satu import main as hal_satu_main
from new_user import create_user
from db_connection import connect_db


def login_page():
    if 'is_authenticated' in st.session_state and st.session_state.is_authenticated:
        hal_satu_main()
        return

    if 'is_registering' in st.session_state and st.session_state.is_registering:
        create_user()
        return

    st.title("Login Pengguna")

    username = st.text_input("Username", key="username_input")
    password = st.text_input("Password", type="password", key="password_input")

    if st.button("Login", key="login_button"):
        conn = connect_db()
        cursor = conn.cursor()

        # Cari user berdasarkan username
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user:
            try:
                input_password = password.encode('utf-8')
                # Hash yang disimpan di database juga dalam format bytes
                stored_hash = user[2].encode('utf-8')

                # Periksa kecocokan password dengan bcrypt
                if bcrypt.checkpw(input_password, stored_hash):  # Verifikasi password
                    st.session_state.user_id = user[0]
                    st.session_state.is_authenticated = True
                    st.session_state.user_type = 'user'
                    # Menyimpan username di session_state
                    st.session_state.username = user[1]
                    st.session_state.is_registering = False
                    st.rerun()
                else:
                    st.error("Password salah!")
            except Exception as e:
                st.error(f"Error saat verifikasi: {str(e)}")
        else:
            st.error("Username tidak ditemukan!")

        conn.close()

    if st.button("Kembali", key="back_button"):
        st.session_state.login_type = None
        st.rerun()

    if st.button("Daftar Pengguna Baru", key="register_button"):
        st.session_state.is_registering = True
        st.rerun()
