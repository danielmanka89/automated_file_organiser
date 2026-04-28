import os
import shutil

# List of folders to create
folders_to_create = ["Images", "Documents", "PDFs"]

# Create folders only if they don't already exist
for folder in folders_to_create:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(f"Created {folder} folder")
    else:
        print(f"{folder} folder already exists - using it")

# Move .jpg and .png files to Images folder
# This will OVERWRITE if files already exist there
shutil.move("cat.jpg", "Images/cat.jpg")
shutil.move("family.png", "Images/family.png")

# Move .txt files to Documents folder
shutil.move("notes.txt", "Documents/notes.txt")

# Move .pdf files to PDFs folder
shutil.move("resume.pdf", "PDFs/resume.pdf")

print("All files moved successfully!")
