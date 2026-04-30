import os
import shutil
import datetime

# ===== CONFIGURATION =====
SORT_BY = "size"  # Change to "date" or "size" to test

# Size thresholds (in bytes)
LARGE_FILE = 10 * 1024 * 1024   # 10 MB
MEDIUM_FILE = 1 * 1024 * 1024   # 1 MB

# Files to NEVER move
PROTECTED_FILES = [
    "day1_create_folder.py",
    "day2_move_files.py",
    "day2_smart_move.py",
    "day3_check_date.py",
    "day3_check_size.py",
    "day3_smart_sorter.py",
    "test.py",
    "README.md"
]

# ===== TYPE SORTING =====
def sort_by_type():
    print("\n--- Sorting by TYPE ---\n")
    
    # Create folders
    folders = ["Images", "Documents", "PDFs"]
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"Created folder: {folder}")
    
    # Get all files
    all_files = os.listdir(".")
    
    for file in all_files:
        # Skip folders and protected files
        if os.path.isdir(file):
            continue
        if file in PROTECTED_FILES:
            print(f"Skipping: {file}")
            continue
        
        # Move based on extension
        if file.endswith((".jpg", ".png", ".gif", ".jpeg")):
            shutil.move(file, f"Images/{file}")
            print(f"Moved {file} -> Images/")
        elif file.endswith((".txt", ".docx")):
            shutil.move(file, f"Documents/{file}")
            print(f"Moved {file} -> Documents/")
        elif file.endswith(".pdf"):
            shutil.move(file, f"PDFs/{file}")
            print(f"Moved {file} -> PDFs/")
        else:
            print(f"Unknown type: {file} (not moved)")

# ===== DATE SORTING =====
def sort_by_date():
    print("\n--- Sorting by DATE ---\n")
    
    all_files = os.listdir(".")
    
    for file in all_files:
        if os.path.isdir(file):
            continue
        if file in PROTECTED_FILES:
            print(f"Skipping: {file}")
            continue
        
        # Get the last modified date
        timestamp = os.path.getmtime(file)
        date_obj = datetime.datetime.fromtimestamp(timestamp)
        folder_name = date_obj.strftime("%Y-%m-%d")
        
        # Create folder if needed
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Created folder: {folder_name}")
        
        # Move the file
        shutil.move(file, f"{folder_name}/{file}")
        print(f"Moved {file} -> {folder_name}/")

# ===== SIZE SORTING =====
def sort_by_size():
    print("\n--- Sorting by SIZE ---\n")
    
    # Create folders
    for folder in ["Large", "Medium", "Small"]:
        if not os.path.exists(folder):
            os.mkdir(folder)
            print(f"Created folder: {folder}")
    
    all_files = os.listdir(".")
    
    for file in all_files:
        if os.path.isdir(file):
            continue
        if file in PROTECTED_FILES:
            print(f"Skipping: {file}")
            continue
        
        # Get file size
        size = os.path.getsize(file)
        
        # Decide folder
        if size >= LARGE_FILE:
            folder = "Large"
        elif size >= MEDIUM_FILE:
            folder = "Medium"
        else:
            folder = "Small"
        
        # Move the file
        shutil.move(file, f"{folder}/{file}")
        print(f"Moved {file} ({size} bytes) -> {folder}/")

# ===== MAIN =====
print(f"\n{'='*40}")
print(f"FILE ORGANISER - Sorting by {SORT_BY.upper()}")
print(f"{'='*40}")

if SORT_BY == "type":
    sort_by_type()
elif SORT_BY == "date":
    sort_by_date()
elif SORT_BY == "size":
    sort_by_size()
else:
    print(f"ERROR: Unknown sort method '{SORT_BY}'")

print("\n--- DONE ---\n")
