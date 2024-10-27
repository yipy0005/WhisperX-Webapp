
# WhisperX Audio Transcription and Diarization Web App

This project is a simple web application built with Streamlit for performing audio transcription and speaker diarization using WhisperX models. The application supports audio and video files, including `.mp3`, `.wav`, `.m4a`, and `.mp4`.

## Features

- **Audio Transcription**: Convert spoken content in audio or video files into text.
- **Speaker Diarization**: Identify and label different speakers in multi-speaker recordings.
- **Alignment**: Accurate alignment of text to audio timestamps, with optional character-level precision.
- **Batch Processing**: Handle audio in customizable segments for optimized memory usage.

## Directory Structure

```
./
├── components
│   ├── file_uploader.py         # Handles file upload via Streamlit
│   ├── model_loader.py          # Loads ASR, alignment, and diarization models
│   ├── processing_options.py    # Allows users to configure processing options
│   └── result_display.py        # Displays transcription results in the app
├── utils
│   ├── audio_processing.py      # Audio extraction and preprocessing
│   ├── config.py                # Configuration for Hugging Face tokens
│   ├── diarization.py           # Diarization logic for speaker separation
│   └── transcription.py         # Transcription and alignment functions
├── environment.yaml             # Conda environment configuration
└── main.py                      # Main Streamlit app file
```

## Installation

### Prerequisites

- Install [Anaconda](https://www.anaconda.com/products/individual-download) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
- Ensure you have [Git](https://git-scm.com/) installed to clone the repository.

### Step-by-Step Setup

1. **Clone the repository**:

   ```bash
   git clone git@github.com:yipy0005/WhisperX-Webapp.git
   cd WhisperX-Webapp
   ```

2. **Set up the Conda environment**:

   To create a new environment with all the dependencies specified, use:

   ```bash
   conda env create -f environment.yaml
   ```

   This command will:
   - Create a new Conda environment named `whisperx_webapp`.
   - Install Python 3.10 and all required packages.

3. **Activate the Conda environment**:

   ```bash
   conda activate whisperx_webapp
   ```

### Running the Application

1. **Activate the environment** (if not already activated):

   ```bash
   conda activate whisperx_webapp
   ```

2. **Run the Streamlit app**:

   ```bash
   streamlit run main.py
   ```

3. Open your web browser and go to the URL provided by Streamlit, usually `http://localhost:8501`.

## Troubleshooting

If you encounter any issues or have questions:

1. Make sure your Conda environment is activated (`conda activate whisperx_webapp`).
2. If you still encounter problems, please **raise an issue** in the GitHub repository, and provide a detailed description of the problem.
