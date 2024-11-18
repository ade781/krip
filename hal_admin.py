import streamlit as st
import tabel_data
import tabel_data_user
import hal_dekripsi
import new_admin
import tabel_data_admin
import hal_steganografi
import hal_file


def apply_custom_styles():
    st.markdown("""
    <style>
        /* High-security theme */
        .stApp {
            background: #0a192f;
            color: #e6f1ff;
        }
        
        /* Command center header */
        .command-center {
            background: linear-gradient(170deg, #172a45 0%, #0a192f 100%);
            padding: 2rem;
            border-radius: 15px;
            border: 1px solid #64ffda;
            box-shadow: 0 0 20px rgba(100, 255, 218, 0.1);
            margin-bottom: 2rem;
            animation: pulse 4s infinite;
        }
        
        @keyframes pulse {
            0% { box-shadow: 0 0 20px rgba(100, 255, 218, 0.1); }
            50% { box-shadow: 0 0 30px rgba(100, 255, 218, 0.2); }
            100% { box-shadow: 0 0 20px rgba(100, 255, 218, 0.1); }
        }
        
        .security-badge {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            color: #ff0000;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-size: 0.8rem;
            margin-bottom: 1rem;
            display: inline-block;
            animation: blink 2s infinite;
        }
        
        @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0.5; }
            100% { opacity: 1; }
        }
        
        .admin-notice {
            background: rgba(255, 255, 255, 0.05);
            border-left: 3px solid #64ffda;
            padding: 1rem;
            margin: 1rem 0;
            font-family: 'Courier New', monospace;
        }
        
        /* Cyber-secure sidebar */
        .css-1d391kg {
            background: linear-gradient(180deg, #172a45 0%, #0a192f 100%);
        }
        
        .stSelectbox {
            background: #172a45;
            border-radius: 8px;
            border: 1px solid #64ffda;
        }
        
        /* Status indicators */
        .status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 2rem;
        }
        
        .status-item {
            background: rgba(255, 255, 255, 0.05);
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #64ffda;
        }
        
        /* Retro terminal effect */
        .terminal-text {
            font-family: 'Courier New', monospace;
            color: #64ffda;
            line-height: 1.6;
            margin: 1rem 0;
        }
        
        /* Warning banner */
        .warning-banner {
            background: rgba(255, 0, 0, 0.1);
            border: 1px solid #ff0000;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            font-weight: bold;
        }
        
        /* Access level indicator */
        .access-level {
            position: fixed;
            top: 1rem;
            right: 1rem;
            background: #ff0000;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            font-size: 0.8rem;
            z-index: 1000;
            animation: fadeInOut 2s infinite;
        }
        
        @keyframes fadeInOut {
            0% { opacity: 0.7; }
            50% { opacity: 1; }
            100% { opacity: 0.7; }
        }
    </style>
    """, unsafe_allow_html=True)


def main():
    apply_custom_styles()

    # Access Level Indicator
    st.markdown("""
        <div class="access-level">
            LEVEL OMEGA • AKSES TERTINGGI
        </div>
    """, unsafe_allow_html=True)

    # Command Center Header
    st.markdown(f"""
        <div class="command-center">
            <div class="security-badge">
                ⚠️ TERMINAL KOMANDO PUSAT • AKSES TERBATAS
            </div>
            <h1>🛸 PUSAT KOMANDO ALPHA-OMEGA</h1>
            <p>Administrator: {st.session_state.username} | Kode Otorisasi: OMEGA-{hash(st.session_state.username) % 10000:04d}</p>
        </div>
        
        <div class="admin-notice">
            <p>PERINGATAN KEAMANAN LEVEL-OMEGA:</p>
            <p>Anda telah memasuki zona pengawasan tertinggi sistem peluncuran roket. 
            Setiap tindakan yang dilakukan di terminal ini memiliki dampak langsung pada keamanan nasional.</p>
            <p>Status: AKTIF | SUPER ENKRIPSI | RIVEST CHIPER 4 | Protokol: ALPHA-ZERO</p>
        </div>
    """, unsafe_allow_html=True)

    # Menu Options with Enhanced Security Descriptions
    menu_options = {
        "data": "🔐 Database Peluncuran Terenkripsi",
        "data pengguna": "👤 Manajemen Personel Rahasia",
        "data komando": "👤 Data Komando Tertinggi",
        "dekripsi": "🔓 Dekripsi Protokol Level-Omega",
        "steganografi": "🔓 Steganografi",
        "enkripsi file": "🔓 Enkripsi File",
        "tambah admin": "⚡ Registrasi Komandan Baru [OMEGA CLEARANCE]",
        "logout": "🚪 Terminasi Sesi Keamanan"
    }

    # Enhanced Sidebar
    st.sidebar.markdown("""
        <div style='background: rgba(100, 255, 218, 0.1); padding: 1rem; border-radius: 10px; border: 1px solid #64ffda;'>
            <h3>🎯 PUSAT KENDALI OMEGA</h3>
            <p style='font-size: 0.8rem;'>Sistem Aktif • Pengawasan 24/7</p>
        </div>
    """, unsafe_allow_html=True)

    selected_menu = st.sidebar.selectbox(
        "Terminal Navigasi", list(menu_options.keys()))

    # Status Grid
    st.markdown("""
        <div class="status-grid">
            <div class="status-item">
                <h4>🛡️ Status Keamanan</h4>
                <p>LEVEL MAKSIMUM</p>
            </div>
            <div class="status-item">
                <h4>🌍 Jaringan Global</h4>
                <p>TERHUBUNG</p>
            </div>
            <div class="status-item">
                <h4>🔐 Enkripsi Quantum</h4>
                <p>AKTIF</p>
            </div>
        </div>
        
        <div class="terminal-text">
            > Sistem peluncuran dalam status siaga<br>
            > Protokol keamanan level Omega diaktifkan<br>
            > Pemantauan aktivitas real-time aktif
        </div>
    """, unsafe_allow_html=True)

    # Menu Routing with Security Checks
    if selected_menu == "data":
        st.markdown(
            '<div class="warning-banner">⚠️ Mengakses database terenkripsi...</div>', unsafe_allow_html=True)
        tabel_data.main()
    elif selected_menu == "data pengguna":
        st.markdown(
            '<div class="warning-banner">⚠️ Membuka arsip personel rahasia...</div>', unsafe_allow_html=True)
        tabel_data_user.main()
    elif selected_menu == "data komando":
        st.markdown(
            '<div class="warning-banner">⚠️ Membuka arsip personel rahasia...</div>', unsafe_allow_html=True)
        tabel_data_admin.main()
    elif selected_menu == "dekripsi":
        st.markdown(
            '<div class="warning-banner">⚠️ Memulai protokol dekripsi level Omega...</div>', unsafe_allow_html=True)
        hal_dekripsi.main()
    elif selected_menu == "steganografi":
        st.markdown(
            '<div class="warning-banner">⚠️ Memulai protokol dekripsi level Omega...</div>', unsafe_allow_html=True)
        hal_steganografi.main()
    elif selected_menu == "enkripsi file":
        st.markdown(
            '<div class="warning-banner">⚠️ Memulai protokol dekripsi level Omega...</div>', unsafe_allow_html=True)
        hal_file.main()
    elif selected_menu == "tambah admin":
        st.markdown(
            '<div class="warning-banner">⚠️ Mengakses sistem registrasi komandan...</div>', unsafe_allow_html=True)
        new_admin.main()
    elif selected_menu == "logout":
        st.warning("⚠️ Menonaktifkan protokol keamanan dan mengakhiri sesi...")
        st.session_state.is_authenticated = False
        st.session_state.username = ""
        st.session_state.user_id = ""
        st.rerun()

    # Enhanced Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
        <div style='text-align: center; padding: 1rem; background: rgba(100, 255, 218, 0.1); border-radius: 10px; border: 1px solid #64ffda;'>
            <h4>🔒 SISTEM PENGAWASAN AKTIF</h4>
            <p style='font-size: 0.8rem;'>Dibangun dengan protokol keamanan tertinggi untuk melindungi aset strategis nasional</p>
            <p style='font-size: 0.7rem; color: #64ffda;'>v2.5.7-OMEGA</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
