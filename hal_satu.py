import streamlit as st
import hal_enkripsi
import hal_dekripsi
import hal_steganografi
import tabel
import tabel_data_public
import hal_file


def apply_custom_styles():
    st.markdown("""
    <style>
        /* Dashboard styling */
        .dashboard-title {
            background: linear-gradient(120deg, #1e3c72, #2a5298);
            padding: 1.5rem;
            border-radius: 15px;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }
        
        .mission-status {
            background: rgba(30, 60, 114, 0.1);
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            border-left: 4px solid #1e3c72;
        }
        
        .security-notice {
            font-size: 0.9rem;
            color: #666;
            padding: 1rem;
            border: 1px solid #ddd;
            border-radius: 8px;
            margin-top: 2rem;
        }
        
        .stSelectbox {
            background: #f8f9fa;
            border-radius: 8px;
            padding: 0.5rem;
        }
        
        .stSidebar .sidebar-content {
            background: #f8f9fa;
        }
        
        .sidebar-info {
            padding: 1rem;
            background: linear-gradient(45deg, #2196F3, #21CBF3);
            color: white;
            border-radius: 8px;
            margin-top: 1rem;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #1e3c72;
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #2a5298;
        }
    </style>
    """, unsafe_allow_html=True)


def main():
    apply_custom_styles()

    # Custom title with styling
    st.markdown(f"""
        <div class="dashboard-title">
            <h1>🚀 Terminal Kontrol Rahasia</h1>
            <p>Operator: {st.session_state.username} | Status: Aktif</p>
        </div>
        
        <div class="mission-status">
            <h3>⚠️ Peringatan Keamanan Tingkat Tinggi</h3>
            <p>Anda telah memasuki sistem pengamanan kode peluncuran roket level Alpha-7. 
            Setiap tindakan yang Anda lakukan akan dicatat dan dimonitor oleh sistem keamanan pusat.</p>
        </div>
    """, unsafe_allow_html=True)

    menu_options = {
        "Enkripsi": "🔐 Enkripsi Kode Peluncuran",
        "Dekripsi": "🔓 Dekripsi Pesan Rahasia",
        "Tabel Data": "📊 Matrix Kode Orbital",
        "Tabel Data Operasi": "📊 Matrix Kode Orbital",
        "Steganografi": "🎯 Kamuflase Data Sensitif",
        "Enkripsi File": "📂 Enkripsi Dokumen Klasifikasi",
        "logout": "🚪 Akhiri Sesi"
    }

    st.sidebar.markdown("""
        <div style='text-align: center; padding: 1rem; background: #1e3c72; color: white; border-radius: 10px; margin-bottom: 1rem;'>
            🛰️ PUSAT KONTROL ROKET
        </div>
    """, unsafe_allow_html=True)

    selected_menu = st.sidebar.selectbox(
        "Navigasi Terminal", list(menu_options.keys()))

    if selected_menu == "Enkripsi":
        hal_enkripsi.main()
    elif selected_menu == "Dekripsi":
        hal_dekripsi.main()
    elif selected_menu == "Tabel":
        tabel.main()
    elif selected_menu == "Tabel data public":
        tabel_data_public.main()
    elif selected_menu == "Steganografi":
        hal_steganografi.main()
    elif selected_menu == "Enkripsi File":
        hal_file.main()
    elif selected_menu == "logout":
        st.warning("⚠️ Mengakhiri sesi keamanan...")
        st.session_state.is_authenticated = False
        st.session_state.username = ""
        st.session_state.user_id = ""
        st.rerun()

    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div class='sidebar-info'>
            <h4>🔒 Protokol Keamanan Aktif</h4>
            <p>Semua aktivitas dalam terminal ini dilindungi oleh sistem super enkripsi</p>
        </div>  
        
        <div style='text-align: center; padding: 1rem; margin-top: 1rem; font-size: 0.8rem;'>
            Dibuat dengan dedikasi untuk keamanan nasional 🚀
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="security-notice">
            <h4>📡 Status Sistem</h4>
            <ul>
                <li>Super Enkripsi: Ada</li>
                <li>Firewall Neural: Terpasang</li>
                <li>Backup Redundansi: Siap</li>
            </ul>
            <p><em>Remember: Keamanan adalah prioritas utama dalam misi peluncuran.</em></p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
