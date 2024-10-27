import streamlit as st


def display_transcription(transcription_result):
    st.subheader("Transcription Results")
    for segment in transcription_result["segments"]:
        st.write(f"[{segment['start']} - {segment['end']}]: {segment['text']}")


def download_transcription():
    st.subheader("Download Transcription")

    if st.session_state["subtitle_content"] and st.session_state["subtitle_filename"]:
        # Choose the file format
        file_format = st.selectbox("Choose File Format", options=["srt", "txt"])

        # Update the file extension based on the selected format
        file_name = f"transcription.{file_format}"

        # Display download button
        st.download_button(
            label="Download Transcription File",
            data=st.session_state["subtitle_content"],
            file_name=file_name,
            mime="text/plain",
        )
