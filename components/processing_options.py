import streamlit as st


def select_processing_options():
    """
    Allows the user to select options for processing the audio.
    This includes options for alignment, diarization, batch size, and compute type.
    """

    st.sidebar.subheader("Processing Options")

    # Option to perform alignment
    align = st.sidebar.checkbox(
        "Perform Alignment",
        help="Perform alignment of the transcription to match audio timestamps accurately.",
    )

    # Option to return character-level alignment
    return_char_alignments = st.sidebar.checkbox(
        "Return Character Alignment",
        help="If enabled, provides detailed character-level alignment within the transcript.",
    )

    # Option to perform speaker diarization
    diarize = st.sidebar.checkbox(
        "Perform Speaker Diarization",
        help="Identify and label different speakers in the audio, useful for multi-speaker recordings.",
    )

    # Batch size
    batch_size = st.sidebar.slider(
        "Batch Size",
        min_value=1,
        max_value=32,
        value=16,
        help="Number of audio segments to process in parallel. Lower the number if you face memory issues.",
    )

    # Compute type for model, set to 'int8' by default
    compute_type = st.sidebar.selectbox(
        "Compute Type",
        options=["int8", "float16"],
        index=0,  # Default to 'int8'
        help="Select computation precision. 'int8' is the default and uses lower memory.",
    )

    # Return the selected options as a dictionary
    options = {
        "align": align,
        "return_char_alignments": return_char_alignments,
        "diarize": diarize,
        "batch_size": batch_size,
        "compute_type": compute_type,
    }

    return options
