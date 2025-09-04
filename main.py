import streamlit as st
from style import load_css
import profil, layanan, fasilitas, lokasi, beranda

st.set_page_config(page_title="Omah Fisio", layout="wide")
load_css()

# Tambahkan anchor di masing-masing section
st.markdown('<div id="beranda"></div>', unsafe_allow_html=True)
beranda.show()

st.markdown('<div id="profil"></div>', unsafe_allow_html=True)
profil.show()

st.markdown('<div id="layanan"></div>', unsafe_allow_html=True)
layanan.show()

st.markdown('<div id="fasilitas"></div>', unsafe_allow_html=True)
fasilitas.show()

st.markdown('<div id="alamat"></div>', unsafe_allow_html=True)
lokasi.show()

# Footer
st.markdown("""
    <hr style="border: none; border-top: 2px solid #D1A75E; margin-top: 60px;">

    <div style="text-align: center; font-size: 15px; color: #5a4b3f; margin-top: 30px; font-family: 'Segoe UI', sans-serif;">
        Follow kami di Instagram
        <a href="https://www.instagram.com/omah.fisio" target="_blank" style="color: #D1A75E; text-decoration: none; font-weight: bold;">
                @omah.fisio
        </a>
        <br><br>
        &copy; 2025 Omah Fisio. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
