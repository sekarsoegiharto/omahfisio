import streamlit as st
import base64

# =========================================
# CSS global untuk grid fasilitas
# =========================================
def load_facility_css():
    st.markdown("""
    <style>

    /* GRID WRAPPER */
    .facility-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
        gap: 20px;
        margin-top: 25px;
        padding-right: 10px;
    }

    /* CARD */
    .facility-card {
        background: #ffffff;
        padding: 12px;
        border-radius: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.10);
        transition: 0.2s ease;
        text-align: center;
    }

    /* CARD HOVER EFFECT */
    .facility-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.18);
    }

    /* GAMBAR */
    .facility-card img {
        width: 160px;
        height: 160px;
        object-fit: cover;
        border-radius: 12px;
        margin-bottom: 10px;
    }

    /* TEKS */
    .facility-card h4 {
        margin: 0;
        font-size: 1rem;
        color: #333;
        font-weight: 600;
    }

    </style>
    """, unsafe_allow_html=True)


# =========================================
# Komponen Card
# =========================================
def facility_card(img_path, title):
    st.markdown(f"""
    <div class="facility-card">
        <img src="{img_path}">
        <h4>{title}</h4>
    </div>
    """, unsafe_allow_html=True)

# Fungsi konversi gambar ke base64
def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =========================================
# Halaman Fasilitas
# =========================================
def show():
    load_facility_css()

    st.markdown("## Fasilitas Omah Fisio")

    fasilitas = [
        (f"data:image/jpeg;base64,{get_base64_of_bin_file('foto/ditarik.jpg')}", "Mobilisasi Bahu"),
        (f"data:image/jpeg;base64,{get_base64_of_bin_file('foto/posisi-istirahat.jpg')}", "Stretching Relaksasi"),
        (f"data:image/jpeg;base64,{get_base64_of_bin_file('foto/tens.jpg')}", "TENS Therapy"),
        (f"data:image/jpeg;base64,{get_base64_of_bin_file('foto/laser.jpg')}", "Low Laser Therapy"),
        (f"data:image/jpeg;base64,{get_base64_of_bin_file('foto/gym-ball.jpg')}", "Area Exercise"),
        (f"data:image/jpeg;base64,{get_base64_of_bin_file('foto/ruang-tunggu.jpg')}", "Ruang Tunggu Nyaman"),
    ]


    # buka grid wrapper
    st.markdown("<div class='facility-grid'>", unsafe_allow_html=True)

    # render tiap card
    for img, title in fasilitas:
        facility_card(img, title)

    # tutup wrapper
    st.markdown("</div>", unsafe_allow_html=True)
