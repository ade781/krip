import streamlit as st
import mysql.connector
import binascii
from db_connection import connect_db


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


# Fungsi Caesar Cipher enkripsi
def caesar_encrypt(text, shift):
    result = ""

    # Perulangan untuk setiap karakter dalam teks
    for char in text:
        if char.isalpha():
            # Mengecek apakah huruf besar atau kecil
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Mengabaikan karakter selain huruf

    return result


# Fungsi untuk menyimpan teks terenkripsi dan nama_operasi ke database
def save_text(user_id, encrypted_text, key, nama_operasi):
    conn = connect_db()
    cursor = conn.cursor()
    # Menyimpan nama_operasi bersama dengan teks terenkripsi dan kunci
    cursor.execute("INSERT INTO text (user, isi, kunci, nama_operasi) VALUES (%s, %s, %s, %s)",
                   (user_id, encrypted_text, key, nama_operasi))
    conn.commit()
    conn.close()


# Form input untuk enkripsi
def encryption_form():
    st.subheader("Form Enkripsi")
    nama_operasi = st.text_input(
        "Masukkan Nama Operasi peluncuran roket", key="nama_operasi_input")
    # Input teks untuk enkripsi
    input_text = st.text_area(
        "kode yang akan dienkripsi:", key="input_text_key")

    # Input key dari user untuk enkripsi
    key = st.text_input("Masukkan Key untuk enkripsi:", key="key_input_key")

    # Input nama_operasi

    # Validasi input key untuk memastikan hanya angka
    if key and not key.isdigit():
        st.error("Key hanya boleh berupa angka!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(id) FROM text")
    last_id = cursor.fetchone()[0]
    conn.close()

    if st.button("Enkripsi"):
        if input_text and key and nama_operasi:
            # Pertama, enkripsi menggunakan RC4
            rc4_encrypted = rc4_encrypt(input_text, key)
            # Kedua, enkripsi hasil RC4 menggunakan Caesar Cipher
            # Menggunakan nilai key sebagai shift Caesar
            caesar_shift = int(key)
            caesar_encrypted = caesar_encrypt(rc4_encrypted, caesar_shift)

            # Simpan hasil super enkripsi (RC4 + Caesar) ke database
            save_text(st.session_state.user_id,
                      caesar_encrypted, key, nama_operasi)
            st.success("Berhasil dienkripsi dan disimpan ke database!")
            st.write(f"**ID Data:** {last_id + 1}")
            st.write(f"**Hasil Enkripsi Super:** {caesar_encrypted}")
        else:
            if not input_text:
                st.error("Teks tidak boleh kosong!")
            if not key:
                st.error("Key tidak boleh kosong!")
            if not nama_operasi:
                st.error("Nama Operasi tidak boleh kosong!")


# Halaman utama
def main():
    st.title("Enkripsi RC4 + Caesar (Super Enkripsi)")

    # Cek login
    if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
        st.error("Silakan login terlebih dahulu!")
        return

    if 'user_id' in st.session_state:
        encryption_form()


if __name__ == "__main__":
    main()
