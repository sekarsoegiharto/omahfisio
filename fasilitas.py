import streamlit as st

def show():
    st.markdown("<div style='padding-top: 20px'></div>", unsafe_allow_html=True)
    st.markdown("<div id='fasilitas'></div>", unsafe_allow_html=True)

    st.markdown("<h2 style='color:#2c2c2c;'>🏥 Fasilitas Omah Fisio</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("foto/infra-red.jpg", caption="Alat Infra Red", use_container_width=True)
        st.image("foto/tens.jpg", caption="Tens", use_container_width=True)
        st.image("foto/shock-wave.jpg", caption="Shock Wave", use_container_width=True)

    with col2:
        st.image("foto/gym-ball.jpg", caption="Fasilitas Terapi", use_container_width=True)
        st.image("foto/kasur.jpg", caption="Tempat Terapi", use_container_width=True)
        st.image("foto/ruang-tunggu.jpg", caption="Ruang Tunggu Omah Fisio", use_container_width=True)

    with col3:
        st.image("foto/ultrasound-besar-landscape.jpg", caption="Ultrasound", use_container_width=True)
        st.image("foto/sepeda.jpg", caption="Sepeda Statis", use_container_width=True)
        st.image("foto/laser.jpg", caption="Low Laser Therapy", use_container_width=True)
