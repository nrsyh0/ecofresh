import streamlit as st  
from pathlib import Path
from streamlit_option_menu import option_menu 
from chempy import balance_stoichiometry
from periodictable import elements 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re
import math
from sklearn.linear_model import LinearRegression 
from io import BytesIO

# ============================
# LOAD CUSTOM CSS
# ============================
try:
    css_file = Path(__file__).parent / "style.css"
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

# ============================
# CONFIGURASI HALAMAN
# ============================
st.set_page_config(
    page_title="EcoFresh",
    page_icon="🌿",
    layout="wide",
)

# ============================
# SIDEBAR MENU
# ============================
with st.sidebar:
    selected = option_menu(
        menu_title="EcoFresh Menu",
        options=["Home", "Tentang Produk", "Kandungan & Manfaat", "FAQ", "Kontak"],
        icons=["house", "info-circle", "droplet", "question-circle", "envelope"],
        default_index=0,
    )

# ============================
# PAGE: HOME
# ============================
if selected == "Home":
    st.title("🌿 EcoFresh — Edukasi Deodoran Fermentasi dari Limbah Sayur")
    st.write("""
    **Selamat datang di EcoFresh!**  
    EcoFresh adalah platform edukasi mengenai inovasi *deodoran alami berbahan dasar limbah sayur hasil fermentasi*.  
    Website ini dirancang sebagai media informasi interaktif untuk memahami bagaimana sisa sayuran dapat menjadi produk yang aman, bermanfaat, dan ramah lingkungan.

    Melalui EcoFresh, kamu dapat mempelajari:
    - Mengapa limbah sayur dipilih sebagai bahan dasar
    - Peran fermentasi dalam menghasilkan senyawa aktif
    - Kandungan dan manfaat produk deodoran alami
    - Jawaban atas pertanyaan umum pengguna

    EcoFresh hadir untuk mengajak masyarakat memilih gaya hidup yang lebih alami dan berkelanjutan.
    """)

# ============================
# PAGE: TENTANG PRODUK
# ============================
elif selected == "Tentang Produk":
    st.title("🥗 Tentang Produk EcoFresh")
    
    st.subheader("Latar Belakang")
    st.write("""
    Limbah sayur merupakan salah satu jenis sampah organik dengan jumlah produksi sangat besar setiap harinya. 
    Jika tidak dikelola, limbah ini dapat menimbulkan bau tidak sedap serta merusak lingkungan.

    Dalam penelitian ini, limbah sayur dimanfaatkan melalui **fermentasi** sehingga menghasilkan bahan dasar kaya bakteri baik 
    atau NTB (*Natural Termentasi Bakteri*), yang berpotensi menekan bau badan secara alami.
    """)

    st.subheader("Mengapa Limbah Sayur?")
    st.write("""
    - Masih mengandung senyawa organik yang bermanfaat.  
    - Fermentasi meningkatkan aktivitas mikroba baik yang menghasilkan senyawa antibakteri dan antijamur.  
    - Mendukung konsep **zero waste**.  
    - Menjadi alternatif alami yang lebih aman daripada bahan kimia sintetis.  
    """)

# ============================
# PAGE: KANDUNGAN & MANFAAT
# ============================
elif selected == "Kandungan & Manfaat":
    st.title("🧪 Kandungan dan Manfaat EcoFresh")

    st.subheader("Kandungan Aktif Utama")
    st.write("""
    - **NTB (Natural Termentasi Bakteri):** Menghambat pertumbuhan bakteri penyebab bau badan.  
    - **Asam organik alami:** Menjaga pH kulit tetap stabil.  
    - **Antioksidan:** Membantu merawat kesehatan kulit.  
    - **Senyawa antijamur alami:** Mengurangi risiko iritasi pada area ketiak.  
    """)

    st.subheader("Manfaat untuk Kulit")
    st.write("""
    - Mengurangi bau badan secara alami  
    - Menstabilkan pH kulit  
    - Aman untuk kulit sensitif  
    - Tidak meninggalkan noda pada pakaian  
    - Menjaga kelembapan kulit  
    """)

    st.subheader("Kelebihan Dibanding Deodoran Sintetis")
    st.write("""
    - Terbuat dari bahan alami  
    - Bebas aluminium, paraben, triclosan, dan pewangi sintetis  
    - Ramah lingkungan  
    - Aman untuk penggunaan jangka panjang  
    - Menggunakan bahan yang mudah terurai (*biodegradable*)  
    """)

# ============================
# PAGE: FAQ
# ============================
elif selected == "FAQ":
    st.title("❓ Frequently Asked Questions (FAQ)")

    st.write("**1. Apakah EcoFresh aman untuk kulit sensitif?**  
    Ya, karena terbuat dari bahan alami tanpa zat kimia keras.")

    st.write("**2. Apakah aromanya tahan lama?**  
    Aromanya lembut dan alami, ketahanan tergantung aktivitas harian.")

    st.write("**3. Bagaimana cara penyimpanan produk?**  
    Simpan di tempat sejuk dan hindari sinar matahari langsung.")

    st.write("**4. Apakah aman digunakan setiap hari?**  
    Aman, karena tidak mengandung zat berbahaya.")

    st.write("**5. Apakah hasil fermentasi tidak berbahaya?**  
    Fermentasi dilakukan secara terkontrol sehingga menghasilkan bakteri baik yang aman.")

# ============================
# PAGE: KONTAK
# ============================
elif selected == "Kontak":
    st.title("📩 Kontak EcoFresh")

    st.write("Isi formulir berikut jika kamu memiliki pertanyaan atau saran:")

    name = st.text_input("Nama")
    email = st.text_input("Email")
    message = st.text_area("Pesan")

    if st.button("Kirim"):
        if name and email and message:
            st.success("Pesan kamu sudah terkirim! Terima kasih telah menghubungi EcoFresh.")
        else:
            st.warning("Mohon lengkapi semua data sebelum mengirim.")

    st.write("---")
    st.write("Atau hubungi kami melalui email: **ecofresh.support@gmail.com**")
