import streamlit as st
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def load_css():
    st.markdown("""
        <style>
        header {visibility: hidden;}
        html { scroll-behavior: smooth; }
        section.main > div {
            padding-top: 0rem !important;
        }

        .block-container {
            padding-top: 1rem;
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

        .btn:hover {
            background-color: #A86C37;
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
            max-width: 180px;
            float: right;
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
            color: white !important;
        }

        a.btn:hover {
            color: white !important;
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
                
        #profil::before,
        #layanan::before,
        #fasilitas::before,
        #alamat::before {
            content: "";
            display: block;
            height: 100px;
            margin-top: -100px;
            visibility: hidden;
        }

        /* Testimoni Section */
        .testimoni-card {
            background-color: #F6ECE2;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 30px;
            display: flex;
            align-items: flex-start;
            gap: 20px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
                
        #testimoni::before {
            content: "";
            display: block;
            height: 100px;  /* = tinggi navbar */
            margin-top: -100px;
            visibility: hidden;
        }

        .testimoni-text {
            font-size: 16px;
            color: #5C3A1B;
            line-height: 1.6;
            font-family: 'Georgia', serif;
        }

        .testimoni-name {
            font-weight: bold;
            margin-top: 10px;
        }

        .star {
            color: #8B5E3C;
            font-size: 18px;
            margin-bottom: 10px;
        }

        .circle-img {
            width: 70px;
            height: 70px;
            border-radius: 50%;
            object-fit: cover;
            border: 3px solid #D1B98C;
        }
                
        .promo-left {
            margin-right: auto;
            background-color: #ff4d4d;
            color: white;
            padding: 6px 16px;
            border-radius: 12px;
            font-weight: bold;
            font-size: 15px;
            box-shadow: 0 0 12px rgba(255, 77, 77, 0.8), 0 0 20px rgba(255, 77, 77, 0.6);
            animation: pulseGlow 1.8s infinite;
        }

        @keyframes pulseGlow {
            0% {
                box-shadow: 0 0 10px rgba(255, 77, 77, 0.6), 0 0 20px rgba(255, 77, 77, 0.4);
            }
            50% {
                box-shadow: 0 0 20px rgba(255, 77, 77, 0.9), 0 0 30px rgba(255, 77, 77, 0.7);
            }
            100% {
                box-shadow: 0 0 10px rgba(255, 77, 77, 0.6), 0 0 20px rgba(255, 77, 77, 0.4);
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Navbar HTML
    st.markdown("""
        <div class="navbar">
            <div class="promo-left">Limited Offer! 2 Sesi, 350 Ribu</div>
            <a href=#beranda>Beranda</a>
            <a href=#profil>Profil</a>
            <a href=#layanan>Layanan</a>
            <a href=#fasilitas>Fasilitas</a>
            <a href=#alamat>Lokasi</a>
            <a class="cta-btn" href="https://wa.me/6287856838456" target="_blank">Booking Sekarang</a>
        </div>
    """, unsafe_allow_html=True)
