import streamlit as st
from PIL import Image
import io


def encode_image(image_path, message, output_path):
    # Validasi panjang pesan
    if len(message) > 50:
        raise ValueError("Pesan terlalu panjang! Maksimal 50 karakter.")

    img = Image.open(image_path)
    binary_message = ''.join(format(ord(c), '08b') for c in message)
    binary_message += '1111111111111110'

    img = img.convert("RGB")
    pixels = img.load()

    msg_index = 0
    width, height = img.size
    for y in range(height):
        for x in range(width):
            if msg_index < len(binary_message):
                pixel = list(pixels[x, y])
                for i in range(3):
                    if msg_index < len(binary_message):
                        pixel[i] = (pixel[i] & ~1) | int(
                            binary_message[msg_index])
                        msg_index += 1
                pixels[x, y] = tuple(pixel)

    img.save(output_path)


def decode_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size

    binary_message = ""
    max_chars = 50  # Maksimal 50 karakter
    max_bits = max_chars * 8 + 16  # 8 bits per karakter + 16 bits penanda
    bits_found = 0

    for y in range(height):
        for x in range(width):
            if bits_found >= max_bits:
                break
            pixel = pixels[x, y]
            for i in range(3):
                binary_message += str(pixel[i] & 1)
                bits_found += 1
                if bits_found >= max_bits:
                    break
        if bits_found >= max_bits:
            break

    end_index = binary_message.find('1111111111111110')
    if end_index != -1:
        binary_message = binary_message[:end_index]
    else:
        return "Pesan tidak ditemukan dalam gambar"

    try:
        message = ''.join(chr(int(binary_message[i:i+8], 2))
                          for i in range(0, len(binary_message), 8))
        return message
    except:
        return "Error: Format pesan tidak valid"


def main():
    st.title("Fitur Steganografi Gambar")
    st.caption("Maksimal 50 karakter untuk pesan yang akan disembunyikan")

    option = st.selectbox("Pilih Opsi", ("Sembunyikan Pesan", "Ambil Pesan"))

    if option == "Sembunyikan Pesan":
        st.subheader("Sembunyikan Pesan di Gambar")

        uploaded_image = st.file_uploader(
            "Pilih gambar", type=["png", "jpg", "jpeg"])
        message = st.text_area("Pesan yang ingin disembunyikan")

        if uploaded_image and message:
            # Validasi panjang pesan
            if len(message) > 50:
                st.error("Pesan terlalu panjang! Maksimal 50 karakter.")
                st.info(f"Panjang pesan saat ini: {len(message)} karakter")
                return

            image = Image.open(uploaded_image)
            image.save("input_image.png")

            if st.button("Sembunyikan Pesan"):
                try:
                    encode_image("input_image.png", message,
                                 "output_image.png")
                    st.success("Pesan berhasil disembunyikan!")
                    st.image("output_image.png",
                             caption="Gambar dengan Pesan Tersembunyi")

                    with open("output_image.png", "rb") as file:
                        btn = st.download_button(
                            label="Download Gambar",
                            data=file,
                            file_name="gambar_dengan_pesan.png",
                            mime="image/png"
                        )
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {str(e)}")

    elif option == "Ambil Pesan":
        st.subheader("Ambil Pesan dari Gambar")

        uploaded_image = st.file_uploader(
            "Pilih gambar dengan pesan tersembunyi", type=["png", "jpg", "jpeg"])

        if uploaded_image:
            image = Image.open(uploaded_image)
            image.save("output_image.png")

            if st.button("Ambil Pesan"):
                try:
                    message = decode_image("output_image.png")
                    if message.startswith("Error") or message.startswith("Pesan tidak"):
                        st.error(message)
                    else:
                        st.success("Pesan ditemukan!")
                        st.write("Pesan:", message)
                except Exception as e:
                    st.error(
                        f"Terjadi kesalahan saat mengambil pesan: {str(e)}")


if __name__ == "__main__":
    main()
