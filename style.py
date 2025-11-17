import streamlit as st
import base64
import streamlit.components.v1 as components


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

logo_base64 = get_base64_of_bin_file("foto/logo-omahfisio.png")


def load_css():  
    st.markdown(f"""
        <div id="menuToggle">
        <input type="checkbox" />
        <span></span>
        <span></span>
        <span></span>
        
        <div id="sideNav">
            <div class="close-btn">&times;</div>  <!-- TOMBOL X -->
            <a href="#beranda">Beranda</a>
            <a href="#profil">Profil</a>
            <a href="#layanan">Layanan</a>
            <a href="#fasilitas">Fasilitas</a>
            <a href="#event">Kerjasama Event</a>
            <a href="#alamat">Lokasi</a>
            <a href="https://wa.me/6287856838456">Booking Sekarang <br><br><br></a>
            <div class="promo-left">Promo menarik 350.000 untuk 2x datang</div> 
        </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <style>
        header {visibility: hidden;}
        html { scroll-behavior: smooth; }
        section.main > div {
             padding-top: 0rem !important;
        }
                
        /* Tombol silang (X) untuk close side menu */
        .close-btn {
            position: absolute;
            top: 5px;
            left: 20px;
            font-size: 38px;
            font-weight: bold;
            color: #6B3E26;
            cursor: pointer;
            z-index: 99999;
        }

        .block-container {
            padding-top: 0rem;
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
            padding: 45px 40px;
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
        #alamat::before,
        #event::before {
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
        
        /* === PROMO MOBILE VERSION === */
        @media (max-width: 768px) {
            .promo-left {
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                margin-top: 16px !important;
                width: 65% !important;   /* box ngepas dengan teks */
                margin: 0 auto !important;       /* center secara horizontal *
                padding: 4px 12px !important;    /* lebih kecil */
                font-size: 13px !important;      /* teks lebih kecil */
                border-radius: 10px !important;

                background-color: #ff4d4d !important;
                color: white !important;
                font-weight: bold !important;

                box-shadow: 0 0 8px rgba(255, 77, 77, 0.7),
                            0 0 14px rgba(255, 77, 77, 0.5) !important;

                text-align: center !important;   /* pastikan teks center */
            }
        }
        /* Animation untuk HP (lebih soft) */
        @keyframes pulseGlowMobile {
            0% {
                box-shadow: 0 0 6px rgba(255, 77, 77, 0.5),
                            0 0 10px rgba(255, 77, 77, 0.3);
            }
            50% {
                box-shadow: 0 0 12px rgba(255, 77, 77, 0.8),
                            0 0 20px rgba(255, 77, 77, 0.6);
            }
            100% {
                box-shadow: 0 0 6px rgba(255, 77, 77, 0.5),
                            0 0 10px rgba(255, 77, 77, 0.3);
            }
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
                
        /* MOBILE RESPONSIVE */
        @media(max-width: 600px) {
            .feature-box {
                padding: 20px 18px;
            }
            .feature-icon { font-size: 30px; }
            .feature-title { font-size: 18px; }
        }
                
        /* TEXt NORMALISASI */
        .frame-box p {
            font-size: 17px;
            line-height: 1.6;
            color: #6B3E26;
        }
        /* ==== TYPOGRAPHY ==== */
        .title-text { font-size: 81px; font-weight: 700; color: #6B3E26; }
        .highlight-text { font-size: 70px; font-weight: bold; color: #D1A75E; }
        
        /* ==== PARAGRAPH STYLE ==== */
        p, li, span, div {
            font-size: 17px;
            line-height: 1.6;
            color: #6B3E26;
        }

        /* Mobile text */
        @media(max-width: 600px){
            .frame-box {
                padding: 22px !important;
                max-width: 96% !important;
            }
            .frame-box p {
                font-size: 14px !important;
                line-height: 1.5 !important;
            }
        }    

        /* HP LOGO – TIDAK IKUT SCROLL */
        @media(max-width: 768px){
            .logo-wrapper {
                position: absolute;
                top: -800px;
                right: -10px;
                width: 180px !important;    /* ukuran HP (lebih kecil) */
            }
        }   
        
        /* =========================
       HAMBURGER MOBILE (kiri atas)
       ========================= */
        @media(max-width: 768px){
        .hamburger{
            position: fixed;
            top: 16px;
            left: 16px;     /* <<< geser ke kiri */
            width: 26px;    /* <<< kecil */
            height: 20px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            z-index: 10001;
        }

        .hamburger div{
            height: 3px;
            background: #6B3E26;    /* warna coklat elegant */
            border-radius: 2px;
        }

        /* =========================
           SIDE NAV
           ========================= */
        .side-nav{
            position: fixed;
            left: -250px;
            top: 0;
            width: 250px;
            height: 100%;
            background: white;
            padding: 50px 20px;
            transition: 0.3s;
            z-index: 10000;
            box-shadow: 3px 0 15px rgba(0,0,0,0.15);
        }
        .side-nav.open{ left: 0; }

        .side-nav a{
            display: block;
            margin-bottom: 22px;
            font-weight: 700;
            font-size: 17px;
            color: #6B3E26;
            text-decoration: none;
        }

        .side-nav a.cta{
            background: #6B3E26;
            padding: 10px 20px;
            border-radius: 10px;
            color: white !important;
            margin-top: 20px;
            font-size: 16px;
            display: inline-block;
        }

        /* Hide desktop navbar on mobile */
        .navbar {
            display: none !important;
        }
    } 
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    section[data-testid="stSidebar"] {display: none;}

    #menuToggle { display: none; }

    @media (max-width: 780px) {

    #menuToggle {
        display: block;
        position: fixed;
        top: 15px;
        left: 15px;
        z-index: 30;
        color: #6B3E26;
    }

    #menuToggle input {
        display: block;
        width: 40px;
        height: 32px;
        position: absolute;
        top: 0;
        left: 0;
        opacity: 0;
        z-index: 40;
        cursor: pointer;
    }

    #menuToggle span {
        display: block;
        width: 40px;
        height: 7px;
        margin-bottom: 6px;
        background: #333;
        border-radius: 3px;
        background: #6B3E26;  
    }

    #sideNav {
        position: fixed;
        top: 0;
        left: -260px;
        width: 240px;
        height: 100%;
        background: white;
        padding-top: 60px;
        box-shadow: 2px 0 8px rgba(0,0,0,0.2);
        transition: left 0.3s ease;
        z-index: 20;
    }

    #sideNav a {
        padding: 12px 20px;
        display: block;
        font-size: 18px;
        text-decoration: none;
        color: #6B3E26;
    }

    #menuToggle input:checked ~ #sideNav {
        left: 0;
    }
    }
    </style>
    """, unsafe_allow_html=True)


    # hide_github_logo = """
    #     <style>
    #         #MainMenu {display: none !important;}
    #         footer {display: none !important;}
    #         .stDeployButton {display: none;}
    #         .viewerBadge_container__1QSob {display: none;}
    #         .st-emotion-cache-1gulkj5 {display: none;}  /* GitHub corner link */
    #         </style>
    #     """
    # st.markdown(hide_github_logo, unsafe_allow_html=True)

    # hide_streamlit_style = """
    #     <style>
    #     #MainMenu {visibility: hidden;}
    #     footer {visibility: hidden;}
    #     .stDeployButton {display: none;}
    #     .viewerBadge_container__1QSob {display: none;}
    #     </style>
    # """
    # st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # hide_all = """
    #     <style>
    #     #MainMenu {visibility: hidden;}
    #     footer {visibility: hidden;}
    #     .stDeployButton {display: none;}
    #     .viewerBadge_container__1QSob {display: none;}
    #     .st-emotion-cache-1gulkj5 {display: none;}  /* GitHub logo */
    #     header {visibility: hidden;} /* hide Streamlit header */
    #     </style>
    # """
    # st.markdown(hide_all, unsafe_allow_html=True)

    # Navbar HTML
    st.markdown("""
        <div class="navbar">
            <div class="promo-left">Promo menarik 350.000 untuk 2x datang</div>
            <a href=#beranda>Beranda</a>
            <a href=#profil>Profil</a>
            <a href=#layanan>Layanan</a>
            <a href=#fasilitas>Fasilitas</a>
            <a href=#event>Kerjasama Event</a>
            <a href=#alamat>Lokasi</a>
            <a class="cta-btn" href="https://wa.me/6287856838456" target="_blank">Booking Sekarang</a>
        </div>
    """, unsafe_allow_html=True)