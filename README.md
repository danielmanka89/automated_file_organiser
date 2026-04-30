# Automated File Organiser

I'm building a Python script that watches a folder and sorts files automatically. This is my first real coding project.

## Day 1 - Python Setup & Creating Folders

**What I learned:**
- Python can talk to my computer's file system
- `os.mkdir()` creates a new folder
- `os.rmdir()` deletes an empty folder

**Problems I solved:**
- FileExistsError (folder already there) → delete it first or use a new name
- FileNotFoundError (folder doesn't exist) → check what's actually there

**Status:** Day 1 complete

## Day 2 - Moving Files Automatically

**What I learned:**
- `shutil.move()` moves files from one place to another
- File extensions (`.jpg`, `.pdf`, `.txt`) tell you what type of file a file is
- `os.listdir()` gets all files in a folder
- Loops can check every file automatically
- Created a "skip list" to protect important files from being moved

**What I built:**
A smart script that automatically sorts files into folders based on their extensions:
- Images (.jpg, .png) → Images folder
- Documents (.txt, .docx) → Documents folder  
- PDFs (.pdf) → PDFs folder

**My code:** `day2_move_files.py` and `day2_smart_move.py`

**Status:** Day 2 complete

## Day 3 - Smart Sorting (Type, Date, Size)

**What I built:** A Python script that sorts files automatically by:

- **Type** - .jpg → Images, .pdf → PDFs, .txt → Documents
- **Date** - Old files → 2024-01-01, New files → today's date
- **Size** - Small, Medium, Large folders based on file size

**My code:** `day3_smart_sorter.py`

**Status:** Day 3 complete