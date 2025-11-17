import streamlit as st
from style import get_base64_of_bin_file

def show():
    st.markdown("<div style='padding-top: 10px'></div>", unsafe_allow_html=True)

    # Ambil gambar latar dan denah
    bg_image = get_base64_of_bin_file("foto/blur-depan.jpg")
    denah = get_base64_of_bin_file("foto/denah.svg")

    st.markdown(f"""
        <style>
        .alamat-section {{
            position: relative;
            background-image: url("data:image/jpg;base64,{bg_image}");
            background-size: cover;
            background-position: center;
            border-radius: 20px;
            padding: 80px 20px;
            margin: 30px 0;
            color: #333;
            display: flex;
            justify-content: center;
        }}

        .alamat-card {{
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 20px;
            padding: 40px 30px;
            box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.15);
            max-width: 90vw;
            width: 800px;
            text-align: center;
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
            margin-bottom: 20px;
        }}

        .alamat-text a {{
            color: #D1A75E;
            text-decoration: underline;
            font-weight: bold;
        }}

        .denah-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
        }}
        </style>

        <div id="alamat" class="alamat-section">
            <div class="alamat-card">
                <div class="alamat-title">📍 Lokasi Kami</div>
                <div class="alamat-text">
                    <strong>Jl. Simpang Darmo Permai Selatan IV No.92, Pradahkalikendal, Kec. Dukuhpakis, Surabaya, Jawa Timur 60187</strong><br>
                    <a href="https://maps.app.goo.gl/PBeEhddhaQfkiXvb7" target="_blank">
                        Buka di Google Maps
                    </a>
                </div>  
                <div class="denah-container">
                    <img src="data:image/svg+xml;base64,{denah}" alt="Denah Lokasi" />
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # st.markdown("""
    #     <hr style="border: none; border-top: 2px solid #D1A75E; margin-top: 60px;">
    #     <div style="text-align: center; font-size: 15px; color: #5a4b3f; margin-top: 30px; font-family: 'Segoe UI', sans-serif;">
    #         Punya pertanyaan? Tekan Booking Sekarang!
    #         <br><br>
    #         Follow kami di Instagram
    #         <a href="https://www.instagram.com/omah.fisio" target="_blank" style="color: #D1A75E; text-decoration: none; font-weight: bold;">
    #                 @omah.fisio
    #         </a>
    #         <br><br>
    #         &copy; 2025 Omah Fisio. All rights reserved.
    #     </div>
    #     """, unsafe_allow_html=True)