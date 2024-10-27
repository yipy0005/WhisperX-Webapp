
# WhisperX Audio Transcription and Speaker Diarization App Documentation

## Introduction
This documentation provides a step-by-step guide to using the **WhisperX Audio Transcription and Speaker Diarization App**. The app is built using **Streamlit**, allowing users to transcribe audio files, align the transcription with audio timestamps, and perform speaker diarization. Below are the instructions for using the app, along with details about its directory structure and file organization.

## Directory Structure

```plaintext
└── ./
    ├── components
    │   ├── file_uploader.py
    │   ├── model_loader.py
    │   ├── processing_options.py
    │   └── result_display.py
    ├── utils
    │   ├── audio_processing.py
    │   ├── config.py
    │   ├── diarization.py
    │   └── transcription.py
    └── main.py
```

### Overview of Key Files
1. **main.py**: The main entry point for the Streamlit app. Handles the user interface and the sequence of audio processing.
2. **components/**: Contains the user interface components and model handling functions.
   - **file_uploader.py**: Handles file upload through the Streamlit sidebar.
   - **model_loader.py**: Loads the necessary models for transcription, alignment, and diarization.
   - **processing_options.py**: Allows users to configure processing options.
   - **result_display.py**: Displays transcription results and allows users to download the results.
3. **utils/**: Contains helper functions for audio processing, transcription, alignment, and diarization.
   - **audio_processing.py**: Manages audio extraction and format conversion.
   - **config.py**: Manages configuration settings, including loading and saving the Hugging Face token.
   - **diarization.py**: Functions for speaker diarization and assigning labels to speakers.
   - **transcription.py**: Handles transcription and alignment processes and subtitle generation.

## How to Use the App

### 1. Launch the App
To run the app, navigate to the root directory and execute:
```bash
streamlit run main.py
```

### 2. Steps to Follow in the App

#### **Step 1: Upload Audio**
- In the sidebar, you will see the **"Step 1: Upload Audio"** section.
- Click the **"Upload Audio/Video File"** button and upload a file. Supported file formats include `.mp3`, `.wav`, `.m4a`, and `.mp4`.
- The uploaded file is processed and converted to a suitable format if necessary.

#### **Step 2: Choose Processing Options**
- Navigate to **"Step 2: Processing Options"** in the sidebar.
- Here, you can select from several options:
  - **Perform Alignment**: Aligns the transcription to the exact audio timestamps.
  - **Return Character Alignment**: Provides a detailed alignment at the character level.
  - **Perform Speaker Diarization**: Enables multi-speaker identification and labeling.
  - **Batch Size**: Adjusts the number of audio segments to process in parallel.
  - **Compute Type**: Selects the precision for computation (`int8` or `float16`).

#### **Step 3: Process the Audio**
- Go to **"Step 3: Process Audio"** in the sidebar.
- Click the **"Start Processing"** button to begin transcription, alignment, and/or diarization based on the chosen options.
- A progress bar will indicate the current processing stage:
  - **Transcription**: The uploaded audio is transcribed.
  - **Alignment**: If selected, transcription is aligned to the audio timestamps.
  - **Diarization**: If enabled, the app identifies different speakers.

#### **Step 4: View and Download Results**
- Once processing is complete, navigate to **"Step 4: View and Download Results"** in the sidebar.
- The transcription results will be displayed on the main page, showing each segment's start and end timestamps alongside the transcribed text.
- You can download the results in `.srt` or `.txt` format.

#### **Step 5: Download Transcription**
- Navigate to **"Step 5: Download Transcription"**.
- Choose the desired file format (e.g., `.srt` or `.txt`) and download the transcription using the provided download button.

### Configuration of Hugging Face Token
- The app requires a Hugging Face API token for certain functionalities.
- During the first run, if the token is missing, the app will prompt you to provide it.
- Once entered, the token will be saved for future use.
- You can manage the token via the `config.py` file or through the app's sidebar interface.

## Code Overview

### Key Functions

#### 1. **File Upload** (`components/file_uploader.py`)
```python
def upload_audio_file():
    uploaded_file = st.sidebar.file_uploader(
        "Upload Audio/Video File", type=["mp3", "wav", "m4a", "mp4"]
    )
    return uploaded_file
```
This function handles audio file uploads through the sidebar.

#### 2. **Model Loading** (`components/model_loader.py`)
- `load_asr_model`: Loads the ASR (Automatic Speech Recognition) model.
- `load_alignment_model`: Loads the model used for aligning transcriptions.
- `load_diarization_model`: Loads the speaker diarization model.

#### 3. **Processing Options** (`components/processing_options.py`)
```python
def select_processing_options():
    st.sidebar.subheader("Processing Options")
    # Options for alignment, character alignment, diarization, etc.
    ...
```
Provides options for customizing audio processing, including alignment and diarization.

#### 4. **Audio Processing** (`utils/audio_processing.py`)
```python
def process_audio(audio_file):
    # Converts the uploaded audio to the correct format and loads it.
    ...
```
Manages conversion and processing of audio files to a suitable format for transcription.

#### 5. **Transcription and Alignment** (`utils/transcription.py`)
- `transcribe_audio`: Handles the transcription of audio data using the ASR model.
- `align_transcription`: Aligns the transcription with audio timestamps if the option is enabled.
- `generate_subtitles`: Generates subtitle content from the transcription.

### Key Concepts

#### **Alignment**
Alignment ensures that the transcription aligns precisely with the audio, improving the accuracy of timestamps.

#### **Diarization**
Diarization separates and labels different speakers in a multi-speaker audio file, useful for interviews or meetings.

## Troubleshooting
1. **Memory Issues**: If you face memory issues during processing, try reducing the batch size in the "Processing Options."
2. **CUDA Device Not Found**: Ensure that your system has a compatible GPU for CUDA-based computation, or switch to CPU mode.
3. **Missing Hugging Face Token**: Ensure the token is saved correctly in `.streamlit/secrets.toml`.

## Conclusion
This guide covers the setup, usage, and key features of the WhisperX Audio Transcription and Speaker Diarization App. Adjust processing settings as needed to suit your audio files, and refer to this documentation for any specific steps or troubleshooting.
