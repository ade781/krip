import streamlit as st
import mysql.connector
import pandas as pd
from db_connection import connect_db


def main():
    st.title("Data Tabel Enkripsi")

    # Add custom CSS for table styling
    st.markdown("""
        <style>
        .dataframe {
            width: 100% !important;
            max-width: 100% !important;
            table-layout: fixed !important;
            border-collapse: collapse;
        }
        .dataframe td, .dataframe th {
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            padding: 8px !important;
            text-align: left !important;
            vertical-align: top !important;
            border: 1px solid #ddd;
        }
        .dataframe th {
            font-weight: bold;
        }
        .dataframe td {
            max-width: 300px !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Cek login
    if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
        st.error("Silakan login terlebih dahulu!")
        return

    # Fitur pencarian berdasarkan username
    username_search = st.text_input("Cari berdasarkan Username:", "")

    # Cek ID user login
    if 'user_id' in st.session_state:
        user_id = st.session_state.user_id

        # Ambil data dari database berdasarkan username jika ada input pencarian
        conn = connect_db()
        cursor = conn.cursor()

        if username_search:
            query = """
                SELECT 
                    text.id, 
                    text.user, 
                    user.username, 
                    text.isi, 
                    text.kunci,
                    text.nama_operasi
                FROM 
                    text
                INNER JOIN 
                    user 
                ON 
                    text.user = user.id
                WHERE 
                    user.username LIKE %s
            """
            cursor.execute(query, ('%' + username_search + '%',))
        else:
            query = """
                SELECT 
                    text.id, 
                    text.user, 
                    user.username, 
                    text.isi, 
                    text.kunci,
                    text.nama_operasi
                FROM 
                    text
                INNER JOIN 
                    user 
                ON 
                    text.user = user.id
            """
            cursor.execute(query)

        data = cursor.fetchall()
        conn.close()

        if not data:
            st.info("Tidak ada data untuk ditampilkan.")
            return

        # Tambahkan nomor secara otomatis untuk setiap baris data
        table_data = [{"Nomor": i + 1, "ID": row[0], "ID_User": row[1], "Username": row[2], "Isi": row[3], "Key": row[4], "Nama Operasi": row[5]}
                      for i, row in enumerate(data)]

        df = pd.DataFrame(table_data)

        # Define custom column widths
        col_widths = {
            'Nomor': '7%',
            'ID': '7%',
            'ID_User': '8%',
            'Username': '15%',
            'Isi': '45%',
            'Key': '10%',
            'Nama Operasi': '15%'  # Kolom Nama Operasi
        }

        # Create the HTML table with custom column widths
        html_table = df.to_html(index=False, classes='dataframe')

        # Add column width styles
        style_header = "<style>\n"
        for col, width in col_widths.items():
            style_header += f".dataframe td:nth-child({list(col_widths.keys()).index(col) + 1}) {{ width: {width}; }}\n"
            style_header += f".dataframe th:nth-child({list(col_widths.keys()).index(col) + 1}) {{ width: {width}; }}\n"
        style_header += "</style>"

        # Display the table with custom styling
        st.markdown(style_header + html_table, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
