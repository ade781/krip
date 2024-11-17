import bcrypt
import streamlit as st
from db_connection import connect_db


def create_user():
    st.title("Daftar Pengguna Baru")

    # Input untuk username, password dan konfirmasi password
    username = st.text_input("Username", key="new_username_input")
    password = st.text_input(
        "Password", type="password", key="new_password_input")
    password_confirm = st.text_input(
        "Konfirmasi Password", type="password", key="confirm_password_input")

    if st.button("Daftar", key="submit_register"):
        if password == password_confirm:
            try:
                # Hash password dengan bcrypt
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

                # Ubah hash menjadi string
                hashed_password_str = hashed_password.decode('utf-8')

                # Simpan ke database
                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO user (username, password) VALUES (%s, %s)", (username, hashed_password_str))
                conn.commit()

                st.success("Pengguna baru berhasil didaftarkan!")
                st.info(
                    "Silakan login dengan username dan password yang baru saja Anda buat.")
                conn.close()
            except Exception as e:
                st.error(f"Terjadi kesalahan: {str(e)}")
        else:
            st.error("Password dan konfirmasi password tidak cocok.")

    # Tombol untuk kembali ke halaman login
    if st.button("Kembali ke Halaman Login", key="back_to_login"):
        st.session_state.is_registering = False
        st.session_state.page = "login"
