import streamlit as st


def display_transcription(transcription_result):
    st.subheader("Transcription Results")
    for segment in transcription_result["segments"]:
        st.write(f"[{segment['start']} - {segment['end']}]: {segment['text']}")


# def download_results(subtitles, options):
#     st.subheader("Download Results")
#     if subtitles:
#         subtitle_format = st.selectbox("Choose Subtitle Format", options=["SRT", "VTT"])
#         subtitle_file = f"transcription.{subtitle_format.lower()}"
#         st.download_button(
#             "Download Subtitles", data=subtitles, file_name=subtitle_file
#         )
