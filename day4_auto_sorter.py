import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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
    "test.py",
    "README.md"
]

def sort_single_file(file_path):
    """Sort a single file based on its extension"""
    
    filename = os.path.basename(file_path)
    
    # Skip protected files
    if filename in PROTECTED_FILES:
        return
    
    # Skip folders
    if os.path.isdir(file_path):
        return
    
    # Check if file still exists (might have been moved already)
    if not os.path.exists(file_path):
        return
    
    # Determine destination folder based on extension
    if filename.endswith((".jpg", ".png", ".gif", ".jpeg")):
        dest_folder = "Images"
    elif filename.endswith((".txt", ".docx", ".md")):
        dest_folder = "Documents"
    elif filename.endswith(".pdf"):
        dest_folder = "PDFs"
    else:
        # Unknown file type - don't move
        return
    
    # Create folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
        print(f"📁 Created folder: {dest_folder}")
    
    # Move the file
    dest_path = os.path.join(dest_folder, filename)
    try:
        shutil.move(file_path, dest_path)
        print(f"✅ Sorted: {filename} → {dest_folder}/")
    except FileNotFoundError:
        # File was already moved by another event - ignore
        pass

# ===== WATCHER CODE =====
class FileSorterHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Only process files (not folders)
        if not event.is_directory:
            print(f"🔍 New file detected: {os.path.basename(event.src_path)}")
            sort_single_file(event.src_path)
    
    # DO NOT sort on modified - that causes double moves!
    # def on_modified(self, event):
    #     pass

# ===== MAIN =====
print("=" * 50)
print("🤖 AUTO FILE ORGANISER IS RUNNING")
print("=" * 50)
print("Watching folder:", os.getcwd())
print("It will automatically sort NEW files by TYPE")
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