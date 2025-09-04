import streamlit as st

def show():
    st.markdown("<div style='padding-top: 20px'></div>", unsafe_allow_html=True)
    st.markdown("<div id='layanan'></div>", unsafe_allow_html=True)
    st.header("Layanan Omah Fisio")

    layanan = [
        ("🧠", "Terapi Stroke &<br>Rehabilitasi Pasca Operasi"),
        ("🏃‍♂️", "Terapi Sport Injury &<br>Recovery"),
        ("🧒", "Terapi Tumbuh<br>Kembang Anak"),
        ("🧬", "Terapi ALS"),
        ("⚡", "Terapi Low Back Pain"),
        ("🦴", "Terapi Spondylosis"),
        ("🧍‍♂️", "Terapi Spondylthesis"),
        ("❄️", "Terapi Frozen Shoulder"),
        ("🧓", "Terapi Osteoarthritis"),
    ]

    # Buat tampilan 3 kolom per baris
    for i in range(0, len(layanan), 3):
        cols = st.columns(3)
        for col, (icon, title) in zip(cols, layanan[i:i+3]):
            with col:
                st.markdown(f"""
                    <div class='feature-box'>
                        <div class='feature-icon'>{icon}</div>
                        <div class='feature-title'>{title}</div>
                    </div>
                """, unsafe_allow_html=True)
