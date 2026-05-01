# Automated File Organiser

I built this because my Downloads folder was a mess. This Python script watches any folder and automatically sorts files into organized subfolders by type, date, or size.

## The Problem

Every time I needed a specific PDF or image, I spent minutes scrolling through hundreds of files with random names. I had zero coding experience, but I knew there had to be a better way.

## My Solution

Over 5 days, I built a script that watches a folder and sorts files automatically.

| Day | What I Built |
|-----|---------------|
| Day 1 | Learned Python basics - created and deleted folders with `os` module |
| Day 2 | Sorted files by extension (.jpg → Images, .pdf → PDFs) using `shutil.move()` |
| Day 3 | Added sorting by date (2026-04-30 folders) and size (Small/Medium/Large) |
| Day 4 | Made it watch folders in real-time with `watchdog` - sorts files as they appear |
| Day 5 | Added command-line arguments with `argparse` and background running |

## Tools I Used

- **Python 3** - The language I learned
- **os module** - Talks to my computer's file system
- **shutil module** - Moves files around
- **watchdog library** - Watches folders for changes
- **argparse module** - Adds command-line options
- **VS Code** - Where I wrote all my code
- **Git & GitHub** - Saved my progress

## How to Use It

```bash
# Sort by file type
python organiser.py --folder ~/Downloads --sort type

# Sort by date
python organiser.py --folder ~/Downloads --sort date

# Sort by size
python organiser.py --folder ~/Downloads --sort size

---------------------------------------------------------

## Day 1 - Python Setup & Creating Folders

**Date:** Day 1

**What I learned:**
- Python can talk to my computer's file system
- `os.mkdir()` creates a new folder
- `os.rmdir()` deletes an empty folder

**Problems I solved:**
- FileExistsError (folder already there) → delete it first or use a new name
- FileNotFoundError (folder doesn't exist) → check what's actually there

**Code files:** `day1_create_folder.py`, `test.py`

**Status:** ✅ Complete

---

## Day 2 - Moving Files Automatically

**Date:** Day 2

**What I learned:**
- `shutil.move()` moves files from one place to another
- File extensions (`.jpg`, `.pdf`, `.txt`) tell you what type of file it is
- `os.listdir()` gets all files in a folder
- Loops can check every file automatically
- Created a "skip list" to protect important files

**What I built:**
A script that sorts files into folders based on extensions:
- Images (.jpg, .png) → Images folder
- Documents (.txt, .docx) → Documents folder
- PDFs (.pdf) → PDFs folder

**Code files:** `day2_move_files.py`, `day2_smart_move.py`

**Status:** ✅ Complete

---

## Day 3 - Smart Sorting (Type, Date, Size)

**Date:** Day 3

**What I learned:**
- `os.path.getmtime()` gets file's last modified date
- `datetime` converts timestamps to readable dates
- `os.path.getsize()` gets file size in bytes
- One script can sort three different ways

**What I built:**
A script that sorts files by:
- **Type** - .jpg → Images, .pdf → PDFs, .txt → Documents
- **Date** - Old files → 2024-01-01, New files → today's date
- **Size** - Small, Medium, Large folders based on file size

**Code files:** `day3_smart_sorter.py`, `day3_check_date.py`, `day3_check_size.py`

**Status:** ✅ Complete

---

## Day 4 - Real-Time Folder Watching

**Date:** Day 4

**What I learned:**
- `watchdog` library monitors folders for changes
- Observer keeps watching continuously
- Event handlers respond to file creation
- Auto-sorting happens instantly when files appear

**What I built:**
A background script that watches my folder and automatically sorts new files by Type, Date, or Size - without me doing anything!

**Code files:** `day4_watcher.py`, `day4_auto_sorter.py`, `day4_auto_sorter_v2.py`

**Status:** ✅ Complete

---

## Tools Used

| Tool | Purpose |
|------|---------|
| Python 3 | Programming language |
| os module | Interact with file system |
| shutil module | Move files |
| watchdog library | Watch folders in real-time |
| VS Code | Code editor |
| Git & GitHub | Version control |

---