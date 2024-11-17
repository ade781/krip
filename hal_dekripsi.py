import streamlit as st
import binascii
from db_connection import connect_db

# Fungsi RC4 dekripsi
def rc4_decrypt(text, key):
    # Inisialisasi array S
    S = list(range(256))
    j = 0

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + ord(key[i % len(key)])) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    decrypted = []
    i = j = 0

    # Konversi text ke bytes
    text_bytes = binascii.unhexlify(text)

    for byte in text_bytes:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        decrypted.append(k ^ byte)

    # Konversi hasil ke string
    return bytes(decrypted).decode('utf-8', errors='ignore')  # Ignore errors if decoding fails


# Fungsi Caesar Cipher dekripsi
def caesar_decrypt(text, shift):
    result = ""

    # Perulangan untuk setiap karakter dalam teks
    for char in text:
        if char.isalpha():
            # Mengecek apakah huruf besar atau kecil
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Mengabaikan karakter selain huruf

    return result


# Fungsi untuk mengambil data dari database dan mendekripsi teks
def decrypt_text(encrypted_text, key):
    try:
        # Pertama, dekripsi menggunakan Caesar Cipher
        caesar_shift = int(key)
        caesar_decrypted = caesar_decrypt(encrypted_text, caesar_shift)

        # Kedua, dekripsi hasil Caesar menggunakan RC4
        rc4_decrypted = rc4_decrypt(caesar_decrypted, key)

        return rc4_decrypted
    except ValueError:
        raise ValueError("Key harus berupa angka!")
    except Exception as e:
        raise Exception(f"Terjadi kesalahan saat dekripsi: {e}")


# Form input untuk dekripsi
def decryption_form():
    st.subheader("Form Dekripsi")

    # Input teks yang telah dienkripsi
    encrypted_text = st.text_area(
        "Teks yang telah dienkripsi:", key="input_encrypted_text_key")

    # Input key dari user untuk dekripsi
    key = st.text_input("Masukkan Key untuk dekripsi:",
                        key="key_input_decrypt_key")

    # Validasi input key untuk memastikan hanya angka
    if key and not key.isdigit():
        st.error("Key hanya boleh berupa angka!")
        return

    if st.button("Dekripsi"):
        if encrypted_text and key:
            try:
                # Dekripsi teks menggunakan metode Super Enkripsi (RC4 + Caesar)
                decrypted_text = decrypt_text(encrypted_text, key)
                st.success("Dekripsi berhasil!")
                st.write(f"**Hasil Dekripsi:** {decrypted_text}")
            except ValueError as ve:
                st.error(str(ve))  # Menampilkan pesan kesalahan jika key tidak valid
            except Exception as e:
                st.error(f"Error: {e}")  # Menangani error lain (misalnya kesalahan dalam proses dekripsi)
        else:
            if not encrypted_text:
                st.error("Teks yang sudah dienkripsi tidak boleh kosong!")
            if not key:
                st.error("Key tidak boleh kosong!")


# Halaman utama untuk dekripsi
def main():
    st.title("Dekripsi RC4 + Caesar (Super Enkripsi)")

    # Cek login
    if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
        st.error("Silakan login terlebih dahulu!")
        return

    if 'user_id' in st.session_state:
        decryption_form()


if __name__ == "__main__":
    main()
