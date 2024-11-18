import bcrypt
import streamlit as st
from db_connection import connect_db


def main():
    st.title("Daftar Komandan Baru (Admin)")

    st.markdown("""
    ### Penting!
    **Hanya pengguna yang benar-benar terpercaya yang seharusnya memiliki akses sebagai admin.**
    Keamanan sistem ini sangat bergantung pada peran yang diberikan kepada pengguna admin.
    Harap pastikan bahwa yang didaftarkan memiliki hak dan wewenang yang sesuai.
    """)

    username = st.text_input("Username", key="new_username_input")
    password = st.text_input(
        "Password", type="password", key="new_password_input")
    password_confirm = st.text_input(
        "Konfirmasi Password", type="password", key="confirm_password_input")

    role = "admin"  

    if st.button("Daftar", key="submit_register"):
        if password == password_confirm:
            try:
                salt = bcrypt.gensalt()
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

                hashed_password_str = hashed_password.decode('utf-8')

                conn = connect_db()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO admin (username, password) VALUES (%s, %s)",
                    (username, hashed_password_str)
                )
                conn.commit()

                st.success(f"Pengguna {role} baru berhasil didaftarkan!")
                st.info(
                    "Silakan login dengan username dan password yang baru saja Anda buat.")
                conn.close()

            except Exception as e:
                st.error(f"Terjadi kesalahan: {str(e)}")
        else:
            st.error("Password dan konfirmasi password tidak cocok.")

    if st.button("Kembali ke Halaman Login", key="back_to_login"):
        st.session_state.is_registering = False
        st.session_state.page = "login"

    st.warning("**Peringatan:** Pengguna yang ditambahkan sebagai admin harus benar-benar dapat dipercaya, karena memiliki akses penuh ke sistem ini. Pastikan Anda memilih dengan bijak!")
