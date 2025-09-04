import streamlit as st
from style import get_base64_of_bin_file

profil = get_base64_of_bin_file("foto/profil-lingkaran.png")

def show():
    st.markdown(f"""
    <div style='
        border: 2px solid #D3BFA6;
        border-radius: 15px;
        padding: 30px;
        background-color: #fffaf5;
        margin-top: 20px;
        margin-bottom: 40px;
    '>
        <h2 style="color: #5C3A1B; font-family: 'Georgia', serif; text-align: center; margin-top: 0px; font-size: 50px;">Profil Kami</h2>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 40px;">
            <div style="flex: 1; min-width: 300px; display: flex; justify-content: center;">
                <img src="data:image/png;base64,{profil}" style="width: 450px; max-width: 100%; height: auto;" />
            </div>
            <div style="flex: 2; min-width: 300px;">
                <div style='
                    font-size: 20px;
                    color: #5C3A1B;
                    font-family: Georgia, serif;
                    line-height: 1.8;
                    text-align: justify;
                    text-justify: inter-word;
                    text-indent: 40px;
                '>
                    <p><b>Omah Fisio Surabaya</b> didirikan pada tahun 2022 oleh Fisioterapis <b>Anjani Septania Soegiharto</b>. Fisio Anjani menempuh pendidikan di Universitas Udayana pada tahun 2020 dan menyelesaikan studi profesinya pada tahun 2021. Pada awalnya, Omah Fisio hadir sebagai bentuk kepedulian terhadap pasien yang kesulitan mengakses layanan fisioterapi di klinik atau rumah sakit, sehingga hanya melayani melalui layanan <i>home care</i>.</p>
                    <p>Seiring berjalannya waktu, setelah mengumpulkan cukup banyak pengalaman serta mendapatkan dukungan dari keluarga dan sahabat terdekat, Anjani akhirnya membulatkan tekad untuk mendirikan <b>praktek mandiri fisioterapi</b> pada tahun 2024. Praktek ini menangani berbagai jenis kasus fisioterapi, seperti <b>stroke, cedera olahraga, cedera akibat aktivitas kerja berulang (overuse), keterlambatan tumbuh kembang anak</b>, dan lain sebagainya.</p>
                    <p><b>Omah Fisio</b> kini dikenal sebagai salah satu <b>pionir klinik fisioterapi</b> dengan pendekatan personal dan berbasis komunitas yang berada di Surabaya. Dengan didirikannya Omah Fisio, kami berharap dapat menjadi tempat pemulihan yang <b>nyaman, profesional, dan mudah dijangkau</b> oleh masyarakat yang membutuhkan layanan fisioterapi berkualitas di Surabaya dan sekitarnya.</p>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
