import streamlit as st
import base64

# ==================================================
# Helper convert gambar ke Base64
# ==================================================
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# # ==================================================
# # CSS KARTU MINI (rapi & seragam)
# # ==================================================
# st.markdown("""
# <style>

# .media-card {
#     width: 100%;
#     border-radius: 10px;
#     overflow: hidden;
#     border: 1px solid #ddd;
#     background: white;
#     margin-bottom: 14px;
#     box-shadow: 0 1px 4px rgba(0,0,0,0.10);
# }

# /* gambar */
# .media-card img {
#     width: 100%;
#     height: 130px;
#     object-fit: cover;
# }

# /* video */
# .media-card video {
#     width: 100%;
#     height: 130px;
#     object-fit: cover;
# }

# /* title */
# .media-title {
#     text-align: center;
#     padding: 6px 0 10px 0;
#     font-size: 0.8rem;
#     font-weight: 600;
#     color: #333;
# }

# </style>
# """, unsafe_allow_html=True)


# ==================================================
# DATA GALERI (foto & video)
# ==================================================
gallery_items = [
    ("foto/event1.jpg", "Konsultasi", "image"),
    ("foto/event3.jpg", "Jawa Pos Event", "image"),
    ("foto/event2-cropped.png", "Terapi Laser", "image"),
    ("foto/semprot.mp4", "Pertolongan Pertama untuk Cedera Lutut", "video"),
    ("foto/event4.jpg", "Sport Injury Treatment", "image"),
    ("foto/semprot2.mp4", "Support Kaki dengan Kinesio Tape", "video"),
]


# ==================================================
# SECTION 4 KOLOM (PALING RAPIH)
# ==================================================
def show():
    st.markdown('<div id="event"></div>', unsafe_allow_html=True)

    st.markdown("## Kerjasama Event")
    st.markdown("Dokumentasi kegiatan Omah Fisio — event, treatment, dan aktivitas pelayanan.")

    # buat 4 kolom
    cols = st.columns(3)

    col_index = 0

    for file_path, title, file_type in gallery_items:

        with cols[col_index]:

            if file_type == "image":
                # gambar base64
                img_b64 = get_base64(file_path)
                html = f"""
                <div class='media-card'>
                    <img src="data:image/jpeg;base64,{img_b64}">
                    <div class='media-title'>{title}</div>
                </div>
                """
                st.markdown(html, unsafe_allow_html=True)

            else:
                # video langsung
                st.markdown("<div class='media-card'>", unsafe_allow_html=True)
                st.video(file_path)
                st.markdown(f"<div class='media-title'>{title}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

        # pindah ke kolom berikutnya (0 → 1 → 2 → 3 → balik ke 0)
        col_index = (col_index + 1) % 3
    