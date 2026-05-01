import time
import os
import shutil
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ===== CONFIGURATION - CHANGE THIS TO SWITCH SORTING MODE =====
SORT_MODE = "size"  # Options: "type", "date", "size"

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
    "day4_watcher.py",
    "day4_auto_sorter.py",
    "day4_auto_sorter_v2.py",
    "test.py",
    "README.md"
]

# ===== SORTING FUNCTIONS =====

def sort_by_type(file_path):
    filename = os.path.basename(file_path)
    
    if filename.endswith((".jpg", ".png", ".gif", ".jpeg")):
        dest_folder = "Images"
    elif filename.endswith((".txt", ".docx", ".md")):
        dest_folder = "Documents"
    elif filename.endswith(".pdf"):
        dest_folder = "PDFs"
    else:
        return False  # Unknown type
    
    # Create folder and move
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    shutil.move(file_path, os.path.join(dest_folder, filename))
    print(f"✅ [{SORT_MODE.upper()}] {filename} → {dest_folder}/")
    return True

def sort_by_date(file_path):
    filename = os.path.basename(file_path)
    
    # Get last modified date
    timestamp = os.path.getmtime(file_path)
    date_obj = datetime.datetime.fromtimestamp(timestamp)
    folder_name = date_obj.strftime("%Y-%m-%d")
    
    # Create folder and move
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    shutil.move(file_path, os.path.join(folder_name, filename))
    print(f"✅ [{SORT_MODE.upper()}] {filename} → {folder_name}/")
    return True

def sort_by_size(file_path):
    filename = os.path.basename(file_path)
    size = os.path.getsize(file_path)
    
    if size >= LARGE_FILE:
        dest_folder = "Large"
    elif size >= MEDIUM_FILE:
        dest_folder = "Medium"
    else:
        dest_folder = "Small"
    
    # Create folder and move
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    shutil.move(file_path, os.path.join(dest_folder, filename))
    print(f"✅ [{SORT_MODE.upper()}] {filename} ({size} bytes) → {dest_folder}/")
    return True

def sort_file(file_path):
    filename = os.path.basename(file_path)
    
    # Skip protected files
    if filename in PROTECTED_FILES:
        return
    
    # Skip folders
    if os.path.isdir(file_path):
        return
    
    # Check if file still exists
    if not os.path.exists(file_path):
        return
    
    # Call the appropriate sorting function
    if SORT_MODE == "type":
        sort_by_type(file_path)
    elif SORT_MODE == "date":
        sort_by_date(file_path)
    elif SORT_MODE == "size":
        sort_by_size(file_path)
    else:
        print(f"❌ Unknown sort mode: {SORT_MODE}")

# ===== WATCHER CODE =====
class FileSorterHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"🔍 New file: {os.path.basename(event.src_path)}")
            sort_file(event.src_path)

# ===== MAIN =====
print("=" * 50)
print(f"🤖 AUTO FILE ORGANISER - Sorting by {SORT_MODE.upper()}")
print("=" * 50)
print(f"Watching: {os.getcwd()}")
print("Press Ctrl+C to stop")
print("-" * 50)

event_handler = FileSorterHandler()
observer = Observer()
observer.schedule(event_handler, path=".", recursive=False)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
    print("\n" + "=" * 50)
    print("🛑 Auto Organiser stopped")
    print("=" * 50)

observer.join()
