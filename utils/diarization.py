import whisperx


def diarize_speakers(diarization_model, audio_data, options):
    # Perform diarization using the diarization model
    return diarization_model(audio_data)


def assign_speaker_labels(diarize_segments, transcription_result):
    # Assign speaker labels to the transcription result
    return whisperx.assign_word_speakers(diarize_segments, transcription_result)
