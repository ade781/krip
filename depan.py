import streamlit as st
import mysql.connector


def apply_custom_styles():
    st.markdown("""
    <style>
        /* Main container styling */
        .main {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Header styling */
        .header {
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            animation: fadeIn 1s ease-in;
        }
        
        .header-title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .header-subtitle {
            font-size: 1.2rem;
            color: #e0e0e0;
            text-align: center;
            font-style: italic;
        }

        /* Message styling */
        .message {
            font-size: 1.1rem;
            line-height: 1.6;
            color: #2c3e50;
            text-align: justify;
            margin-bottom: 1.5rem;
            padding: 0 1rem;
        }
        
        /* Button styling */
        .stButton button {
            background: linear-gradient(45deg, #2196F3, #21CBF3);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 1.5rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.2);
        }
        
        /* Animation keyframes */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        /* Card styling */
        .card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .header-title {
                font-size: 2rem;
            }
            .header-subtitle {
                font-size: 1rem;
            }
            .message {
                font-size: 1rem;
                padding: 0 0.5rem;
            }
        }
    </style>
    """, unsafe_allow_html=True)


def header():
    st.markdown("""
    <div class="header">
        <div class="header-title">
            🚀 Sistem Keamanan Peluncuran Roket
        </div>
        <div class="header-subtitle">
            Platform Kontrol Akses Aman
        </div>
    </div>
    """, unsafe_allow_html=True)


def home_page():
    apply_custom_styles()
    header()

    st.markdown("""
    <div class="card">
        <div class="message">
            Ketika Anda membaca ini, maka Anda sekarang adalah salah satu orang yang memegang kunci rahasia Roket Company. 
            Sebuah tanggung jawab besar telah dipercayakan kepada Anda untuk menjaga keamanan dan kerahasiaan sistem peluncuran kami. 
            Ingatlah bahwa setiap akses yang Anda lakukan akan tercatat dalam sistem dan memiliki dampak langsung pada keamanan operasional kami. 
            Pilih tingkat akses Anda dengan bijak, dan pastikan untuk selalu menjaga kerahasiaan kredensial yang diberikan.
        </div>
        <h3 style="text-align: center; color: #1e3c72; margin-bottom: 1.5rem;">
            Silakan Pilih Tingkat Akses Anda
        </h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🧑‍💼 Masuk sebagai Pengguna", key="user_button", help="Akses dashboard pengguna", use_container_width=True):
            st.session_state.login_type = "User"
            st.rerun()

    with col2:
        if st.button("👨‍💻 Masuk sebagai Admin", key="admin_button", help="Akses konsol admin", use_container_width=True):
            st.session_state.login_type = "Admin"
            st.rerun()


def user_login_page():
    import user
    user.login_page()


def admin_login_page():
    import admin
    admin.admin_login()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Keamanan Peluncuran Roket",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    if "login_type" not in st.session_state:
        st.session_state.login_type = None

    if st.session_state.login_type == "User":
        user_login_page()
    elif st.session_state.login_type == "Admin":
        admin_login_page()
    else:
        home_page()
