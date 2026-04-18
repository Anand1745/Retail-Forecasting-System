import os

def create_folders():
    folders = ["data", "outputs", "outputs/plots", "models"]
    for folder in folders:
        os.makedirs(folder, exist_ok=True)