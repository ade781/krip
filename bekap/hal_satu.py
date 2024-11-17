import streamlit as st
import mysql.connector
import binascii

# Fungsi untuk koneksi database


def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="kripto"
    )

# Fungsi RC4 enkripsi


def rc4_encrypt(text, key):
    # Inisialisasi array S
    S = list(range(256))
    j = 0

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    cipher = []
    i = j = 0

    # Konversi text ke bytes
    text_bytes = text.encode('utf-8')

    for byte in text_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        cipher.append(k ^ byte)

    # Konversi hasil ke hexadecimal
    return binascii.hexlify(bytes(cipher)).decode('utf-8')

# Fungsi untuk menyimpan teks terenkripsi


def save_text(user_id, encrypted_text):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO text (user, isi) VALUES (%s, %s)",
                   (user_id, encrypted_text))
    conn.commit()
    conn.close()

# Form input untuk enkripsi


def encryption_form():
    st.subheader("Form Enkripsi")
    # Input teks
    input_text = st.text_area("Teks yang akan dienkripsi:")
    # Input key dari user
    key = st.text_input("Masukkan Key untuk enkripsi:")

    if st.button("Enkripsi"):
        if input_text and key:
            encrypted_text = rc4_encrypt(input_text, key)
            save_text(st.session_state.user_id, encrypted_text)
            st.success("Berhasil dienkripsi dan disimpan ke database!")
        else:
            if not input_text:
                st.error("Teks tidak boleh kosong!")
            if not key:
                st.error("Key tidak boleh kosong!")

# Halaman utama


def main():
    st.title("Enkripsi RC4")

    # Cek login
    if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
        st.error("Silakan login terlebih dahulu!")
        return

    if 'user_id' in st.session_state:
        encryption_form()

        if st.button("Logout"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


if __name__ == "__main__":
    main()
