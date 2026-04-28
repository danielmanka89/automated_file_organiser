import os
import shutil

folders = {
    "Images": [".jpg", ".png", ".gif", ".jpeg"],
    "Documents": [".txt", ".docx", ".md"],
    "PDFs": [".pdf"]
}

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Created {folder} folder")

all_files = os.listdir(".")

for file in all_files:
    if os.path.isdir(file) or file == "day2_smart_move.py":
        continue
    
    for folder, extensions in folders.items():
        for ext in extensions:
            if file.endswith(ext):
                shutil.move(file, f"{folder}/{file}")
                print(f"Moved {file} to {folder}")
                break