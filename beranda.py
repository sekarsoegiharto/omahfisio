import streamlit as st
from PIL import Image
from style import load_css  # Jangan lupa panggil ini di main
from streamlit_autorefresh import st_autorefresh


def show():
    load_css()  # Panggil fungsi CSS di awal

    st.markdown("<div style='padding-top: 20px'></div>", unsafe_allow_html=True)
    st.markdown("<div id='beranda'></div>", unsafe_allow_html=True)

    # Hero Section
    col1, col2 = st.columns([2.1, 1])
    with col1:
        st.markdown("<div class='title-text'>The Backbone<br><span class='highlight-text'>of Good Health</span></div>", unsafe_allow_html=True)
        st.markdown("<div class='subtitle'>Kami hadir untuk bantu tingkatkan kualitas hidup Anda melalui terapi fisik profesional dan harga terjangkau.</div>", unsafe_allow_html=True)
        st.markdown("<a href='#testimoni' class='btn'>Pelajari Lebih Lanjut</a>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='logo-wrapper'>", unsafe_allow_html=True)
        st.image("foto/logo-omahfisio.png", use_container_width=False, width=450)
        st.markdown("</div>", unsafe_allow_html=True)

    # Feature Box
    st.markdown("<br><br>", unsafe_allow_html=True)
    feat1, feat2, feat3, feat4 = st.columns(4)
    with feat1:
        st.markdown("<div class='feature-box'><div class='feature-icon'>🙋🏻‍♀️</div><div class='feature-title'>5.000+<br>Klien Bahagia</div></div>", unsafe_allow_html=True)
    with feat2:
        st.markdown("<div class='feature-box'><div class='feature-icon'>🙆🏻‍♀️</div><div class='feature-title'>Harga<br>Terjangkau</div></div>", unsafe_allow_html=True)
    with feat3:
        st.markdown("<div class='feature-box'><div class='feature-icon'>👩🏻‍⚕️</div><div class='feature-title'>Terapis<br>Profesional</div></div>", unsafe_allow_html=True)
    with feat4:
        st.markdown("<div class='feature-box'><div class='feature-icon'>🧘🏻‍♀️</div><div class='feature-title'>7.000+<br>Sesi Terapi</div></div>", unsafe_allow_html=True)

# HEADER hanya satu kali
    st.markdown("<div id='testimoni'></div>", unsafe_allow_html=True)

    st.markdown("""
        <style>
            a.review-link {
                color: #5C3A1B !important;
                font-weight: bold;
                font-size: 18px;
                text-decoration: none;
                transition: color 0.3s ease;
            }
            a.review-link:hover {
                color: #f6ece2 !important;
            }
        </style>
    """, unsafe_allow_html=True)
    # Buat dua kolom: kiri (judul & deskripsi), kanan (link review)
    col_kiri, col_kanan = st.columns([3, 1])

    with col_kiri:
        st.markdown("## 🌟 Testimoni Klien Kami")
        st.write("Beberapa pengalaman positif dari klien yang sudah merasakan manfaat terapi fisik di Omah Fisio.")

    with col_kanan:
        st.markdown("""
            <div style="text-align:right; margin-top:25px;">
                <a class="review-link" href="https://maps.app.goo.gl/fx1DyWuB8qQioQpr7" target="_blank">
                    Cek review lainnya di sini
                </a>
            </div>
        """, unsafe_allow_html=True)

    import base64

    # Fungsi konversi gambar ke base64
    def get_base64_of_bin_file(bin_file_path):
        with open(bin_file_path, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Ambil base64 user image
    user_img_base64 = get_base64_of_bin_file("foto/user.png")
    user_img_data = f"data:image/png;base64,{user_img_base64}"

    # Dummy data testimoni
    testimoni_data = [
        {"nama": "Restu", "foto": user_img_data, "ulasan": "Tempatnya nyaman, di dalam perumahan. Terapisnya ramah dan menjelaskan terapi dengan mudah. Setelah beberapa kali terapi, rasa sakit mulai berkurang."},
        {"nama": "arin amln", "foto": user_img_data, "ulasan": "Punya low back pain, kesini 2x udah mendingan bgt. Ramah bintang 5, Terimakasihhhh"},
        {"nama": "Livia N S", "foto": user_img_data, "ulasan": "Terapisnya ramah dan sangat membantu. Dijelaskan dengan bahasa yang mudah dimengerti dan ditangani dengan sangat hati-hati."},
        {"nama": "Oei Mei Lin", "foto": user_img_data, "ulasan": """Saya ini kasusnya sendi lutut geser jadi sakit dan bengkak. Di awal sebelum dikasih treatment ultrasound dan laser, dijelaskan dulu sama Fisioterapisnya apa aja treatment yang bakal diberikan serta durasinya, kemudian ditambah lagi edukasi serta saran praktis lainnya untuk membantu mempercepat perbaikan dan penyembuhan dari permasalahan sendi lututnya. So helpful sih buat orang awam yg kadang bingung mesti ngapain ketika punya permasalahan kaki makin sakit" gini tapi belum berani untuk operasi. Thank you Anjani @omah.fisio for the good service and very nice hospitality experience. 💯👏🏻"""},
        {"nama": "St. Lutfi Chaniroh", "foto": user_img_data, "ulasan": "hari ini ikut event mills running di sneakerzone surabaya dan kebetulan boots nya omah fisio dan pengen nyoba karena kebetulan kaki lagi shin splint langsung di streching dan di treatment tens (kaya kesetrum) untuk meredakan nyari katanya alhamdulillah setelah itu agak berkurang nyerinya trimakasih omah fisio🙏🏻"},
        {"nama": "nurul iriandani", "foto": user_img_data, "ulasan": "Makasih omah terapii. Kartini Cup jadi semangaaatttt"},
        {"nama": "Silvika Rina Fatin Seryza", "foto": user_img_data, "ulasan": "Sebagai orang auka kerja depan laptop keluhanku ya lowerback pain dan nyeri persendian itu ga nyaman banget kalo kambuh pas lagi beraktivitas, tadi pas terapi juga cecenya jelasin detail apa yang harus di lakukan terus penyebabnya apa ajaaa... pokoknya best banget nih omah fisio, buat penyakit lainnya juga bisa langsung cus terapi disini, apalagi yang ga suka pijet nih mantulll"},
        {"nama": "reny setyawati", "foto": user_img_data, "ulasan": "Keluhan saya Piriformis Syndrome, datang ke Omah Fisio ditangani kak Nia ( Fisiotherapist Omah Fisio ) dengan telaten, ramah, sabar dan detail. Tempatnya bersih, sirkulasi udara bagus, alatnya lengkap, kak Nia juga mengedukasi gerakan² yang tidak diperbolehkan supaya bisa recovery. Recommended banget terapi disini, saya mau ditangani lebih intensif oleh kak Nia supaya bisa pulih sempurna. Semoga makin sukses kak Nia dan Omah Fisio, Tuhan memberkati❤️"},
        {"nama": "Arsy", "foto": user_img_data, "ulasan": "tempatnya bersih nyaman agak masuk perumahan gitu, terapisnya kak anjani ramah banget, penjelasannya juga gampang dipahami"},
        {"nama": "Maria Ayu Dwi Bestari", "foto": user_img_data, "ulasan": "Tempat terapinya masuk sedikit dari jalan utama tapi dalemnya bersih banget. Keluhan awal punggung sakit dan susah buat kembali ke posisi tegak. Habis terapi sekali, bedanya kerasa banget, punggung sudah ngga terlalu sakit. Terapisnya juga ramah dan seru diajak ngobrol 👍 lalu juga dikasih saran gimana spy ngga kambuh lagi sakitnya …"},
        {"nama": "Mona Maria", "foto": user_img_data, "ulasan": "Terapis nya ramah dan menyenangkan. Proses terapi juga nyaman dan nggak sakit sama sekali. Ruang terapi pun cozy dan tenang. Terimakasih dan sukses selalu buat omah fisio 😍 …"},
        {"nama": "Dani Andhrika", "foto": user_img_data, "ulasan": "Hari ini coba di stand omah studio di Kartini Cup Sidoarjo.. jempol kiri yg dulu pernah kebentur racket setelah di treatment laser jadi lebih enteng.. thanks ya"},
    ]

    # --- Setup Carousel ---
    items_per_page = 4
    total_pages = (len(testimoni_data) - 1) // items_per_page + 1

    # --- Autorefresh every 5 seconds ---
    count = st_autorefresh(interval=5000, key="carousel_refresh")

    # --- Gunakan count sebagai indeks
    page = count % total_pages

    # --- Render Carousel ---
    start_idx = page * items_per_page
    end_idx = start_idx + items_per_page
    current_testimonials = testimoni_data[start_idx:end_idx]

    col1, col2 = st.columns(2)
    for idx, testi in enumerate(current_testimonials):
        col = col1 if idx % 2 == 0 else col2
        with col:
            st.markdown(f"""
            <div style="background-color:#f6ece2; border-radius:15px; padding:20px; margin-bottom:25px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                <div style="display:flex; align-items:center; gap:15px;">
                    <img src="{testi['foto']}" style="width:70px;height:70px;border-radius:50%;object-fit:cover;border:3px solid #D1B98C;">
                    <div style="font-size:18px;">⭐⭐⭐⭐⭐</div>
                </div>
                <div style="margin-top:15px; font-size:16px; color:#5C3A1B; line-height:1.6;">
                    {testi['ulasan']}
                </div>
                <div style="margin-top:10px; font-weight:bold;">- {testi['nama']}</div>
            </div>
            """, unsafe_allow_html=True)
