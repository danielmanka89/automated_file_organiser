 Automated File Organiser 

> Never hunt for files again. This Python script watches any folder you choose and automatically sorts incoming files into organized subfolders based on their type, modification date, or file size.

## 🎯 Why I Built This

As a beginner learning Python, I wanted to solve a real problem I face daily: my Downloads folder is always a mess. This script runs in the background and organizes everything automatically - no more manual sorting!

## Features

| Feature | What it does | Example |
|---------|--------------|---------|
| **Type-based sorting** | Sorts by file extension | Images → `/Images`, PDFs → `/Documents` |
| **Date-based sorting** | Sorts by when file was last modified | `2026-04-27/` folder for today's files |
| **Size-based sorting** | Sorts by file size | `/Large (>10MB)`, `/Small (<1MB)` |
| **Watchdog monitoring** | Watches folder in real-time | New file appears → automatically sorted within seconds |
| **Command-line arguments** | Customize without editing code | `--folder ~/Downloads --sort type` |

## Technologies Used

- **Python 3.10+** - Core programming language
- **os module** - Interacts with your file system (create folders, move files)
- **shutil module** - Handles high-level file operations (copy, move, delete)
- **watchdog module** - Monitors folders for changes (like a security camera for files)
- **argparse module** - Parses command-line arguments (like choosing options from a menu)

## How It Works (Simple Explanation)

1. You tell the script which folder to watch (e.g., `~/Downloads`)
2. You choose how to sort: by file type, date, or size
3. The script runs in the background, constantly watching
4. When a new file appears, the script:
   - Checks the file (what type? when created? how big?)
   - Creates appropriate subfolder if needed (e.g., `/PDFs`)
   - Moves the file automatically
5. Your folder stays organized without any effort!

## Installation & Setup

### Prerequisites (what you need before starting)

```bash
# Check if Python is installed (Day 1 will cover this)
python --version

# Install required modules (Day 2 will cover this)
pip install watchdog