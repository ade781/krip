import streamlit as st
import mysql.connector
from mysql.connector import Error

# Fungsi untuk menghubungkan ke database MySQL


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Ganti dengan host database Anda jika bukan localhost
            database="kripto",  # Nama database yang Anda gunakan
            user="root",  # Ganti dengan username MySQL Anda
            password=""  # Ganti dengan password MySQL Anda jika ada
        )
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

# Fungsi untuk memeriksa kredensial login


def check_login(username, password):
    connection = create_connection()
    if connection is None:
        return False

    cursor = connection.cursor()
    # Ganti nama tabel dengan 'admin'
    query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    connection.close()

    if result:
        return True
    else:
        return False

# Halaman login


def login_page():
    st.title("Login Page")

    # Form untuk memasukkan username dan password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            if check_login(username, password):
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")
        else:
            st.warning("Please enter both username and password")


# Menjalankan halaman login
if __name__ == "__main__":
    login_page()
