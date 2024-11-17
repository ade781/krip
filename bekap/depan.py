import streamlit as st


def home_page():
    st.title("Welcome to the Login Portal")

    # Membuat dua kolom untuk tombol login
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login as User"):
            st.session_state.login_type = "User"
    with col2:
        if st.button("Login as Admin"):
            st.session_state.login_type = "Admin"


def user_login_page():
    import user  # Mengimpor file user.py
    user.login_page()


def admin_login_page():
    import admin  # Mengimpor file admin.py
    admin.login_page()


# Main program
if __name__ == "__main__":
    if "login_type" not in st.session_state:
        # Inisialisasi state awal jika belum ada
        st.session_state.login_type = None

    # Menentukan halaman berdasarkan login_type
    if st.session_state.login_type == "User":
        user_login_page()
    elif st.session_state.login_type == "Admin":
        admin_login_page()
    else:
        home_page()
