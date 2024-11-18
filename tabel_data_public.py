import streamlit as st
import mysql.connector
import pandas as pd
from db_connection import connect_db


def main():
    st.title("Data Operasi")

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

    if 'is_authenticated' not in st.session_state or not st.session_state.is_authenticated:
        st.error("Silakan login terlebih dahulu!")
        return

    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT id, isi, nama_operasi 
        FROM text
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    if not data:
        st.info("Tidak ada data untuk ditampilkan.")
        return

    table_data = [{"Nomor": i + 1, "ID": row[0], "Isi Pesan": row[1], "Nama Operasi": row[2]}
                  for i, row in enumerate(data)]

    df = pd.DataFrame(table_data)

    col_widths = {
        'Nomor': '10%',
        'ID': '10%',
        'Isi Pesan': '60%',
        'Nama Operasi': '20%'
    }

    html_table = df.to_html(index=False, classes='dataframe')

    style_header = "<style>\n"
    for col, width in col_widths.items():
        style_header += f".dataframe td:nth-child({list(col_widths.keys()).index(col) + 1}) {{ width: {width}; }}\n"
        style_header += f".dataframe th:nth-child({list(col_widths.keys()).index(col) + 1}) {{ width: {width}; }}\n"
    style_header += "</style>"

    st.markdown(style_header + html_table, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
