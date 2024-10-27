
# WhisperX Audio Transcription and Diarization Web App

This project is a user-friendly web application built with **Streamlit** for audio transcription and speaker diarization using WhisperX models. It supports both audio and video files, including `.mp3`, `.wav`, `.m4a`, and `.mp4`, with a focus on accurate transcription, speaker identification, and customizable processing options.

## Key Features

- **Audio Transcription**: Convert spoken content in audio or video files into accurate text transcriptions.
- **Speaker Diarization**: Automatically identify and label different speakers in multi-speaker recordings.
- **Precise Alignment**: Synchronize transcription text with audio timestamps, with optional character-level detail.
- **Batch Processing**: Process audio in user-defined segments to optimize memory and performance.
- **Downloadable Outputs**: Export results in `.srt` or `.txt` format for easy sharing and use.

## Directory Structure

```plaintext
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
├── DOCUMENTATION.md             # Detailed user guide for the app
├── environment.yaml             # Conda environment configuration
└── main.py                      # Main Streamlit app file
```

## Getting Started

### Prerequisites

- **Anaconda** or **Miniconda** (recommended for environment management)
- **Git** for cloning the repository

### Installation Guide

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:yipy0005/WhisperX-Webapp.git
   cd WhisperX-Webapp
   ```

2. **Create the Conda Environment**:

   Set up a dedicated environment using the provided configuration:

   ```bash
   conda env create -f environment.yaml
   ```

   This will:
   - Create a new Conda environment named `whisperx_webapp`.
   - Install Python 3.10 and all required dependencies.

3. **Activate the Environment**:

   ```bash
   conda activate whisperx_webapp
   ```

### Running the Application

1. **Activate the environment** (if not already activated):

   ```bash
   conda activate whisperx_webapp
   ```

2. **Launch the Streamlit App**:

   ```bash
   streamlit run main.py
   ```

3. **Access the App**:
   Open your web browser and navigate to `http://localhost:8501` to use the app.

## Usage Guide

To learn more about using the app, including detailed instructions for each step, please refer to the [DOCUMENTATION.md](DOCUMENTATION.md) file.

## Troubleshooting

### Common Issues
1. **Environment Activation**: Ensure your Conda environment is activated (`conda activate whisperx_webapp`) before running the app.
2. **CUDA Device Not Found**: If you're encountering GPU-related errors, ensure your system has a compatible GPU and CUDA setup. Alternatively, you can run the app on the CPU.
3. **Memory Management**: If you experience memory constraints during processing, reduce the batch size in the app's settings.

### Getting Help
For any unresolved issues or questions, feel free to [open an issue](https://github.com/yipy0005/WhisperX-Webapp/issues) on the GitHub repository. Please include a detailed description of the problem to help us assist you better.

## Contribution

Contributions are welcome! If you'd like to enhance the app or report bugs, follow these steps:
1. **Fork the Repository**
2. **Create a New Branch** for your feature or fix.
3. **Submit a Pull Request** with a detailed description of changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- **Streamlit**: For providing a simple and powerful framework for building web applications.
- **WhisperX**: For enabling advanced audio transcription and diarization capabilities.

Feel free to explore, experiment, and contribute to the project!
