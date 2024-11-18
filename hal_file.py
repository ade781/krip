import streamlit as st
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AES_Encryptor:
    def __init__(self, key):
        # Pastikan panjang key adalah 32 byte (256-bit)
        self.key = key.encode('utf-8')
        if len(self.key) != 32:
            raise ValueError("Key harus 32 karakter untuk AES-256")

    def encrypt(self, data):
        """Enkripsi data menggunakan AES-256 ECB"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        # Padding data agar panjangnya kelipatan dari block_size
        return cipher.encrypt(pad(data, AES.block_size))

    def decrypt(self, data):
        """Dekripsi data menggunakan AES-256 ECB"""
        cipher = AES.new(self.key, AES.MODE_ECB)
        # Menghapus padding setelah dekripsi
        return unpad(cipher.decrypt(data), AES.block_size)


def main():
    st.title("Enkripsi dan Dekripsi File dengan AES")

    # Penjelasan tipe file yang dapat di-upload
    st.markdown("""
    **Tipe file yang didukung:**
    - Text (.txt)
    - PDF (.pdf)
    - Microsoft Word (.docx)
    - CSV (.csv)
    - ZIP (.zip)
    - JPG (.jpg)
    """)

    # Input untuk key
    key_input = st.text_input("Masukkan Key (32 karakter):", type="password")

    # Pilihan untuk enkripsi atau dekripsi file menggunakan selectbox
    option = st.selectbox("Pilih Aksi:", ("Enkripsi File", "Dekripsi File"))

    if option == "Enkripsi File":
        # Pilih file yang akan dienkripsi
        file = st.file_uploader("Pilih File untuk Dienkripsi", type=[
                                "pdf", "txt", "csv", "docx", "zip", "jpg"])

        if file:
            # Tombol konfirmasi setelah file terupload
            if st.button("Konfirmasi File untuk Enkripsi"):
                # Membaca file yang diupload
                file_data = file.read()

                if key_input:
                    # Enkripsi file
                    try:
                        aes = AES_Encryptor(key_input)
                        encrypted_data = aes.encrypt(file_data)

                        # Tentukan nama file terenkripsi
                        encrypted_file_name = f"encrypted_{file.name}.bin"

                        # Simpan file terenkripsi
                        with open(encrypted_file_name, "wb") as f:
                            f.write(encrypted_data)

                        st.success(
                            f"File berhasil dienkripsi menjadi {encrypted_file_name}!")

                        # Tombol download untuk file terenkripsi
                        with open(encrypted_file_name, "rb") as f:
                            file_data = f.read()
                            st.download_button(
                                label="Download File Terenkripsi",
                                data=file_data,
                                file_name=encrypted_file_name,
                                mime="application/octet-stream" 
                            )
                    except ValueError as e:
                        st.error(f"Error: {e}")
                else:
                    st.error("Masukkan Key terlebih dahulu untuk enkripsi!")

    elif option == "Dekripsi File":
        file = st.file_uploader("Pilih File yang Terenkripsi", type=[
                                "bin", "pdf", "txt", "csv", "docx", "zip", "jpg"])

        if file:
            # Tombol konfirmasi setelah file terupload
            if st.button("Konfirmasi File untuk Dekripsi"):
                # Membaca file .bin yang diupload
                encrypted_data = file.read()

                if key_input:
                    # Dekripsi file tersebut
                    try:
                        aes = AES_Encryptor(key_input)
                        decrypted_data = aes.decrypt(encrypted_data)

                        # Mendapatkan nama file asli
                        original_file_name = file.name.replace(".bin", "")

                        mime_type = "application/octet-stream" 
                        if original_file_name.endswith(".pdf"):
                            mime_type = "application/pdf"
                        elif original_file_name.endswith(".txt"):
                            mime_type = "text/plain"
                        elif original_file_name.endswith(".csv"):
                            mime_type = "text/csv"
                        elif original_file_name.endswith(".docx"):
                            mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        elif original_file_name.endswith(".jpg"):
                            mime_type = "image/jpeg"
                        elif original_file_name.endswith(".zip"):
                            mime_type = "application/zip"

                        # Simpan file terdekripsi dengan ekstensi yang sesuai
                        decrypted_file_name = f"decrypted_{original_file_name}"

                        with open(decrypted_file_name, "wb") as f:
                            f.write(decrypted_data)

                        st.success(
                            f"File berhasil didekripsi menjadi {decrypted_file_name}!")

                        with open(decrypted_file_name, "rb") as f:
                            file_data = f.read()  # Membaca file biner untuk di-download
                            st.download_button(
                                label="Download File Terdekripsi",
                                data=file_data,
                                file_name=decrypted_file_name,
                                mime=mime_type 
                            )
                    except ValueError as e:
                        st.error(f"Error: {e}")
                else:
                    st.error("Masukkan Key terlebih dahulu untuk dekripsi!")


if __name__ == "__main__":
    main()
