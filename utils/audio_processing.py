import tempfile

import whisperx
from moviepy.editor import AudioFileClip


def process_audio(audio_file):
    # Save the UploadedFile to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
        temp_audio_path = temp_audio_file.name

        if audio_file.name.endswith(".mp4"):
            # If it's an mp4 file, extract the audio using moviepy
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=".mp4"
            ) as temp_video_file:
                # Save the UploadedFile to a temporary mp4 file
                temp_video_file.write(audio_file.read())
                temp_video_path = temp_video_file.name

            # Extract audio from mp4 using moviepy and save it as a temporary .wav file
            audio_clip = AudioFileClip(temp_video_path)
            audio_clip.write_audiofile(temp_audio_path)
            audio_clip.close()

        else:
            # Save other audio files to the temporary file directly
            temp_audio_file.write(audio_file.read())

        # Load the audio from the temporary file using WhisperX
        return whisperx.load_audio(temp_audio_path)
