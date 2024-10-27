import whisperx


def load_asr_model(device, compute_type):
    # Load the ASR model
    return whisperx.load_model("large-v3", device, compute_type=compute_type)


def load_alignment_model(device, language_code):
    # Load the alignment model
    return whisperx.load_align_model(language_code=language_code, device=device)


def load_diarization_model(device, hf_token):
    # Load the diarization model
    return whisperx.DiarizationPipeline(use_auth_token=hf_token, device=device)
