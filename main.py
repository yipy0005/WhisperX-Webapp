import gc
import os

import streamlit as st
import toml
import torch
import whisperx

from components.file_uploader import upload_audio_file
from components.model_loader import (
    load_alignment_model,
    load_asr_model,
    load_diarization_model,
)
from components.processing_options import select_processing_options
from components.result_display import display_transcription
from utils.audio_processing import process_audio
from utils.transcription import (
    align_transcription,
    generate_subtitles,
    transcribe_audio,
)

# Set the page configuration at the very top of the script
st.set_page_config(page_title="WhisperX Transcription App", layout="wide")


# Utility functions for handling the Hugging Face token
def load_hf_token():
    """Load Hugging Face token from .streamlit/secrets.toml if it exists."""
    try:
        # Check if token is in Streamlit secrets
        return st.secrets["hf_token"]
    except (KeyError, FileNotFoundError):
        st.error("Hugging Face Token is required. Please set it up.")
        return None


def save_hf_token(hf_token):
    """Save Hugging Face token to .streamlit/secrets.toml."""
    secrets_path = ".streamlit/secrets.toml"

    # Write the Hugging Face token to the secrets file
    with open(secrets_path, "w") as secrets_file:
        toml.dump({"hf_token": hf_token}, secrets_file)
    st.success("Token saved successfully! Reload the app to use the saved token.")


def check_and_create_secrets_file():
    """Check if .streamlit/secrets.toml exists and create it if not present."""
    secrets_path = ".streamlit/secrets.toml"
    if not os.path.isfile(secrets_path):
        os.makedirs(".streamlit", exist_ok=True)
        with open(secrets_path, "w") as secrets_file:
            secrets_file.write("# Hugging Face Token\n")
    else:
        try:
            hf_token = st.secrets["hf_token"]
        except (KeyError, FileNotFoundError):
            # If file does not exist, ask the user for a Hugging Face token and create the file
            hf_token = st.sidebar.text_input(
                "Enter Hugging Face Token:", type="password"
            )
            if st.sidebar.button("Save Token"):
                save_hf_token(hf_token)
                st.sidebar.success(
                    "Token saved successfully! Reload the app to use the saved token."
                )
                st.stop()  # Stop the app so the user can reload with the token saved.


# Check and create secrets.toml if not present before main() runs
check_and_create_secrets_file()


def main():
    st.title("WhisperX Audio Transcription and Speaker Diarization")

    # Initialize session state for subtitle content and filename
    if "subtitle_content" not in st.session_state:
        st.session_state["subtitle_content"] = None
    if "subtitle_filename" not in st.session_state:
        st.session_state["subtitle_filename"] = None

    # Load the Hugging Face token
    hf_token = load_hf_token()

    if not hf_token:
        st.sidebar.error("Hugging Face Token is required. Please set it up.")
        return
    else:
        st.sidebar.text("Hugging Face Token Loaded")

    # Step 1: Upload Audio
    st.sidebar.title("Step 1: Upload Audio")
    audio_file = upload_audio_file()

    if audio_file:
        # Process audio file to get audio data
        audio_data = process_audio(audio_file)

        # Step 2: Choose Processing Options
        st.sidebar.title("Step 2: Processing Options")
        options = select_processing_options()

        # Step 3: Process the Audio
        st.sidebar.title("Step 3: Process Audio")
        if st.sidebar.button("Start Processing"):
            # Initialize progress bar
            progress_bar = st.progress(0)

            device = "cuda" if torch.cuda.is_available() else "cpu"
            compute_type = options["compute_type"]

            # Transcription
            st.write("Loading ASR model...")
            progress_bar.progress(10)
            asr_model = load_asr_model(device, compute_type)
            st.write("Transcribing audio...")
            transcription_result = transcribe_audio(
                audio_data, asr_model, options["batch_size"]
            )
            st.write("Transcription completed.")
            progress_bar.progress(40)

            # Clear ASR model if low on GPU resources
            del asr_model
            gc.collect()
            torch.cuda.empty_cache()

            # Alignment (if selected)
            if options["align"]:
                st.write("Loading alignment model...")
                progress_bar.progress(50)
                align_model, metadata = load_alignment_model(
                    device, transcription_result["language"]
                )
                st.write("Aligning transcription...")
                transcription_result = align_transcription(
                    transcription_result,
                    align_model,
                    metadata,
                    audio_data,
                    device,
                    options["return_char_alignments"],
                )
                st.write("Alignment completed.")
                progress_bar.progress(70)

                # Clear alignment model if low on GPU resources
                del align_model
                gc.collect()
                torch.cuda.empty_cache()

            # Diarization (if selected)
            if options["diarize"]:
                st.write("Loading diarization model...")
                progress_bar.progress(80)
                diarization_model = load_diarization_model(device, hf_token)
                st.write("Performing speaker diarization...")
                diarize_segments = diarization_model(audio_data)
                transcription_result = whisperx.assign_word_speakers(
                    diarize_segments, transcription_result
                )
                st.write("Diarization completed.")
                progress_bar.progress(90)

            # Step 4: Display Results
            st.sidebar.title("Step 4: View and Download Results")
            display_transcription(transcription_result)

            # Subtitle generation and storing in session state
            subtitle_content, subtitle_filename = generate_subtitles(
                transcription_result, options
            )
            st.session_state["subtitle_content"] = subtitle_content
            st.session_state["subtitle_filename"] = subtitle_filename

            # Complete progress bar
            progress_bar.progress(100)

    # Download Subtitle Button
    if st.session_state["subtitle_content"] and st.session_state["subtitle_filename"]:
        st.download_button(
            label="Download Subtitle File",
            data=st.session_state["subtitle_content"],
            file_name=st.session_state["subtitle_filename"],
            mime="text/plain",
        )


if __name__ == "__main__":
    main()
