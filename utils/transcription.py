import os
from io import StringIO

import streamlit as st
import whisperx


def transcribe_audio(audio_data, asr_model, batch_size):
    """
    Transcribes the audio data using the ASR model.

    Parameters:
        audio_data (np.ndarray): Audio waveform data.
        asr_model: The Automatic Speech Recognition model.
        batch_size (int): Batch size for transcription.

    Returns:
        dict: Transcription result containing segments.
    """
    result = asr_model.transcribe(audio_data, batch_size=batch_size)
    return result


def align_transcription(
    transcription_result,
    align_model,
    metadata,
    audio_data,
    device,
    return_char_alignments,
):
    """
    Aligns the transcription result using the alignment model.

    Parameters:
        transcription_result (dict): The initial transcription result.
        align_model: The alignment model.
        metadata (dict): Metadata related to the alignment model.
        audio_data (np.ndarray): Audio waveform data.
        device (str): The device to use for processing (e.g., 'cuda' or 'cpu').
        return_char_alignments (bool): Whether to return character-level alignments.

    Returns:
        dict: Aligned transcription result.
    """
    aligned_result = whisperx.align(
        transcription_result["segments"],
        align_model,
        metadata,
        audio_data,
        device,
        return_char_alignments=return_char_alignments,
    )
    return aligned_result


# utils/transcription.py


def generate_subtitles(transcription_result, options):
    """
    Generates subtitle content from the transcription result.
    Returns:
        content (str): The content of the subtitle file.
        filename (str): The name of the subtitle file.
    """
    # Generate the subtitle content based on the transcription result
    # Example placeholder logic for subtitle generation:
    subtitle_content = ""
    for segment in transcription_result["segments"]:
        start_time = segment["start"]
        end_time = segment["end"]
        text = segment["text"]
        subtitle_content += f"{start_time} --> {end_time}\n{text}\n\n"

    # Define the subtitle filename
    subtitle_filename = "transcription.srt"  # or use other formats like .vtt or .txt

    return subtitle_content, subtitle_filename


def format_timestamp(seconds):
    """
    Format timestamp to HH:MM:SS,MS format (for SRT).

    Parameters:
        seconds (float): The time in seconds to be formatted.

    Returns:
        str: The formatted timestamp string.
    """
    milliseconds = int((seconds - int(seconds)) * 1000)
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


def generate_subtitle_content(subtitles, format_type):
    """
    Generate the subtitle content as a string.

    Parameters:
        subtitles (list): List of subtitle segments.
        format_type (str): Format type for subtitles ('srt' or 'vtt').

    Returns:
        str: The generated subtitle content.
    """
    output = StringIO()

    for idx, subtitle in enumerate(subtitles, start=1):
        output.write(f"{idx}\n")
        output.write(f"{subtitle['start']} --> {subtitle['end']}\n")
        output.write(f"{subtitle['text']}\n\n")

    return output.getvalue()


def save_subtitles(subtitles, format_type="srt"):
    """
    Save the generated subtitles to a file.

    Parameters:
        subtitles (list): List of subtitle segments.
        format_type (str): Format type for subtitles ('srt' or 'vtt').

    Returns:
        str: Path to the saved subtitle file.
    """
    filename = f"transcription.{format_type}"
    with open(filename, "w") as f:
        for idx, subtitle in enumerate(subtitles, start=1):
            f.write(f"{idx}\n")
            f.write(f"{subtitle['start']} --> {subtitle['end']}\n")
            f.write(f"{subtitle['text']}\n\n")

    return filename
