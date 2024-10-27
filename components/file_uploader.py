import streamlit as st


def upload_audio_file():
    uploaded_file = st.sidebar.file_uploader(
        "Upload Audio/Video File", type=["mp3", "wav", "m4a", "mp4"]
    )
    return uploaded_file
