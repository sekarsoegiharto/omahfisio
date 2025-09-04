import streamlit as st

import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

st.set_page_config(page_title="Omah Fisio", layout="wide")

# ==== CSS Styling ====
st.markdown("""
    <style>
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 2rem;
    }
    body {
        background-color: #F6E6C9;
        font-family: 'Segoe UI', sans-serif;
    }
    .frame-box {
        background-color: white;
        border: 5px solid #D1A75E;
        border-radius: 40px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        padding: 50px;
        margin: 20px auto 40px auto;
        max-width: 1200px;
        animation: fade-in 1s ease-in-out;
    }
    @keyframes fade-in {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .title-text {
        font-size: 81px;
        font-weight: 700;
        color: #6B3E26;
        line-height: 1.4;
    }
    .highlight-text {
        font-size: 70px;
        font-weight: bold;
        color: #D1A75E;
    }
    .subtitle {
        font-size: 20px;
        color: #5a4b3f;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .btn {
        background-color: #7C4A21;
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 8px;
        font-size: 18px;
        cursor: pointer;
        text-decoration: none;
    }
    .feature-box {
        background-color: white;
        border-radius: 25px;
        padding: 40px 30px;
        margin: 10px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: #7C4A21;
        border: 4px solid #D1A75E;
        transition: transform 0.2s ease;
    }
            
    .feature-box:hover {
        transform: translateY(-5px);
    }
            
    .feature-icon {
        font-size: 40px;
        color: #D1A75E;
        margin-bottom: 10px;
    }
    .feature-title {
        font-size: 28px;
        font-weight: 700;
        line-height: 1.5;
        text-align: center;
    }

    .logo-wrapper img {
        border-radius: 30px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        border: 3px solid #D1A75E;
        max-width: 180px; /* <--- Ukuran kecil */
        float: right;     /* <--- Pindah ke kanan */
        margin-top: 20px;
    }
    .alamat-section {
        text-align: center;
        padding-top: 60px;
        padding-bottom: 60px;
    }
    .alamat-title {
        font-size: 38px;
        font-weight: bold;
        color: #7C4A21;
        margin-bottom: 10px;
    }
    .alamat-text {
        font-size: 20px;
        color: #5a4b3f;
        margin-bottom: 30px;
    }
    .alamat-img {
        max-width: 500px;
        width: 100%;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
        border: 4px solid #D1A75E;
        margin-bottom: 30px;
    }
            
    a.btn {
    # text-decoration: none !important;
    color: white !important;
    }
    
    a.btn:hover {
    color: white !important;
    }

    </style>
""", unsafe_allow_html=True)

# ==== Navigation Bar ====
st.markdown("""
    <style>
    html {
        scroll-behavior: smooth;
    }

    .block-container {
        padding-top: 120px;
    }

    .navbar {
        position: fixed;
        top: 0;
        right: 0;
        width: 100%;
        z-index: 999;
        display: flex;
        justify-content: flex-end;
        align-items: center;
        background-color: white;
        padding: 20px 40px;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    .navbar a {
        margin-left: 25px;
        color: #7C4A21;
        text-decoration: none;
        font-weight: 600;
        font-size: 16px;
        transition: color 0.3s ease;
    }

    .navbar a:hover {
        color: #D1A75E;
    }

    .navbar .cta-btn {
        background-color: #7C4A21;
        color: white;
        padding: 8px 20px;
        border-radius: 6px;
        margin-left: 30px;
        font-size: 15px;
        font-weight: bold;
        text-decoration: none;
    }

    .navbar .cta-btn:hover {
        background-color: #A86C37;
    }
    </style>

    <div class="navbar">
        <a href="#beranda">Beranda</a>
        <a href="#profil">Profil</a>
        <a href="#layanan">Layanan</a>
        <a href="#fasilitas">Fasilitas</a>
        <a href="#alamat">Lokasi</a>
        <a class="cta-btn" href="https://wa.me/6287856838456" target="_blank">Booking Sekarang</a>
    </div>
""", unsafe_allow_html=True)
    
# ==== Hero Section ====
with st.container():
    col1, col2 = st.columns([2.1, 1])
    
    with col1:
        st.markdown("<div class='title-text'><br>The Backbone<br><span class='highlight-text'>of Good Health</span></div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Kami hadir untuk bantu tingkatkan kualitas hidup Anda melalui terapi fisik profesional dan harga terjangkau.</div>", unsafe_allow_html=True)
        st.markdown("<a href='#testimoni' class='btn'>Pelajari Lebih Lanjut</a>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='logo-wrapper'><br><br><br><br><br>", unsafe_allow_html=True)
        st.image("foto/logo-omahfisio.png", use_container_width=False, width=450)
        st.markdown("</div>", unsafe_allow_html=True)

# ==== Spasi antar section ====
st.markdown("<br>", unsafe_allow_html=True)
# ==== Feature Box ====
st.markdown("", unsafe_allow_html=True)
feat1, feat2, feat3, feat4 = st.columns(4)

with feat1:
    st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>🙋🏻‍♀️</div>
            <div class='feature-title'>10.000+<br>Klien Bahagia</div>
        </div>
    """, unsafe_allow_html=True)

with feat2:
    st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>🙆🏻‍♀️</div>
            <div class='feature-title'>Harga<br>Terjangkau</div>
        </div>
    """, unsafe_allow_html=True)

with feat3:
    st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>👩🏻‍⚕️</div>
            <div class='feature-title'>Terapis<br>Profesional</div>
        </div>
    """, unsafe_allow_html=True)

with feat4:
    st.markdown("""
        <div class='feature-box'>
            <div class='feature-icon'>🧘🏻‍♀️</div>
            <div class='feature-title'>50.000+<br>Sesi Terapi</div>
        </div>
    """, unsafe_allow_html=True)

#testimoni section
st.markdown("""<div id="testimoni"></div>""", unsafe_allow_html=True)
st.markdown("## 🌟 Testimoni Klien Kami")
st.write("Beberapa pengalaman positif dari klien yang sudah merasakan manfaat terapi fisik di Omah Fisio.")

# Testimoni 1: Kiri gambar, kanan teks (bisa kosong atau caption pendek)
col1, col2 = st.columns([1, 1])
with col1:
    st.image("foto/profil.jpg", use_container_width=True)
with col2:
    st.write("")

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Testimoni 2: Kanan gambar, kiri teks
col1, col2 = st.columns([1, 1])
with col1:
    st.write("")
with col2:
    st.image("foto/blur-depan.jpg", use_container_width=True)

# Spacer
st.markdown("<br>", unsafe_allow_html=True)

# Testimoni 3
col1, col2 = st.columns([1, 1])
with col1:
    st.image("foto/blur-depan.jpg", use_container_width=True)
with col2:
    st.write("")

# Testimoni 4
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    st.write("")
with col2:
    st.image("foto/blur-depan.jpg", use_container_width=True)



#lokasi section
bg_image = get_base64_of_bin_file("foto/blur-depan.jpg")

st.markdown(f"""
<style>
.alamat-section {{
    position: relative;
    background-image: url("data:image/jpg;base64,{bg_image}");
    background-size: cover;
    background-position: center;
    border-radius: 20px;
    padding: 300px 50px;
    margin: 30px 0;
    text-align: center;
    color: #333;
}}

.alamat-card {{
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 20px;
    padding: 30px 20px;
    display: inline-block;
    box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.15);
    max-width: 500px;
    margin: auto;
}}

.alamat-title {{
    font-size: 28px;
    font-weight: 700;
    color: #7A4E25;
    margin-bottom: 10px;
}}

.alamat-text {{
    font-size: 16px;
    font-weight: 400;
    color: #444;
}}

.alamat-text a {{
    color: #D1A75E;
    text-decoration: underline;
    font-weight: bold;
}}
</style>

<div id="alamat" class="alamat-section">
    <div class="alamat-card">
        <div class="alamat-title">📍 Lokasi Kami</div>
        <div class="alamat-text">
            Jalan Simpang Darmo Permai Selatan no. 92<br>
            <a href="https://maps.app.goo.gl/PBeEhddhaQfkiXvb7" target="_blank">
                Buka di Google Maps
            </a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# === Foto Lokasi Ditampilkan di Bawah Alamat ===
with st.container():
    col2, col3 = st.columns(2)

    with col2:
         st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
         st.image("foto/klinik-depan-portrait.jpg", width=400, caption="Tampak Depan Klinik Omah Fisio")

    with col3:
         st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
         st.image("foto/gym.jpg", width=400, caption="Fasilitas Terapi")
        



