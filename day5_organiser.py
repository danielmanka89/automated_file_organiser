#!/usr/bin/env python3
"""
Automated File Organiser
Watches a folder and automatically sorts files by type, date, or size.
"""

import os
import shutil
import time
import datetime
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ===== CONFIGURATION =====
LARGE_FILE = 10 * 1024 * 1024   # 10 MB
MEDIUM_FILE = 1 * 1024 * 1024   # 1 MB

# Files to NEVER move
PROTECTED_FILES = [
    "day5_organiser.py",
    "organiser.py",
    "README.md",
    ".git"
]

# Global variable to store sort mode (will be set from command line)
SORT_MODE = "type"

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
        return False
    
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    
    shutil.move(file_path, os.path.join(dest_folder, filename))
    print(f"[{SORT_MODE}] {filename} → {dest_folder}/")
    return True

def sort_by_date(file_path):
    filename = os.path.basename(file_path)
    timestamp = os.path.getmtime(file_path)
    date_obj = datetime.datetime.fromtimestamp(timestamp)
    folder_name = date_obj.strftime("%Y-%m-%d")
    
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    
    shutil.move(file_path, os.path.join(folder_name, filename))
    print(f"[{SORT_MODE}] {filename} → {folder_name}/")
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
    
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    
    shutil.move(file_path, os.path.join(dest_folder, filename))
    print(f"[{SORT_MODE}] {filename} ({size} bytes) → {dest_folder}/")
    return True

def sort_file(file_path):
    filename = os.path.basename(file_path)
    
    # Skip protected files
    if filename in PROTECTED_FILES:
        return
    if os.path.isdir(file_path):
        return
    if not os.path.exists(file_path):
        return
    
    if SORT_MODE == "type":
        sort_by_type(file_path)
    elif SORT_MODE == "date":
        sort_by_date(file_path)
    elif SORT_MODE == "size":
        sort_by_size(file_path)

# ===== WATCHER CODE =====
class FileSorterHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"🔍 New file detected: {os.path.basename(event.src_path)}")
            sort_file(event.src_path)

# ===== MAIN =====
def main():
    global SORT_MODE
    
    # Set up command-line arguments
    parser = argparse.ArgumentParser(description="Automated File Organiser")
    parser.add_argument("--folder", help="Folder to watch (default: current folder)")
    parser.add_argument("--sort", choices=["type", "date", "size"], 
                        default="type", help="Sorting method: type, date, or size")
    
    args = parser.parse_args()
    
    # Set the sort mode globally
    SORT_MODE = args.sort
    
    # Determine which folder to watch
    watch_folder = args.folder if args.folder else "."
    
    # Change to the folder if specified
    if args.folder:
        os.chdir(args.folder)
    
    print("=" * 50)
    print(f"AUTO FILE ORGANISER")
    print("=" * 50)
    print(f"Watching folder: {os.getcwd()}")
    print(f"Sorting by: {SORT_MODE.upper()}")
    print("Press Ctrl+C to stop")
    print("-" * 50)
    
    # Start the watcher
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
        print("Auto Organiser stopped")
        print("=" * 50)
    
    observer.join()

if __name__ == "__main__":
    main()