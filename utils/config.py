import os

# Define a file path to store the Hugging Face token
TOKEN_FILE_PATH = "hf_token.txt"


def load_hf_token():
    """
    Load the Hugging Face token from a local file if it exists.
    """
    if os.path.exists(TOKEN_FILE_PATH):
        with open(TOKEN_FILE_PATH, "r") as file:
            return file.read().strip()
    return None


def save_hf_token(token):
    """
    Save the Hugging Face token to a local file.
    """
    with open(TOKEN_FILE_PATH, "w") as file:
        file.write(token)
