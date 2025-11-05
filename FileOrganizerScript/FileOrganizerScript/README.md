# File Organizer Script

A simple Python automation script that organizes files in a folder by their extensions.

## Features
- Sorts files into subfolders (e.g., PDF, JPG, DOCX)
- Supports dry-run mode (shows what will move without actually moving files)
- Handles file name collisions safely
- Logs all file moves to `organizer.log`

## How to Run
1. Make sure Python 3 is installed.
2. Place this script (`main.py`) in the folder where your files are located, or provide a folder path.
3. Run the program in terminal or command prompt:

```
python main.py
```

Then enter the folder path when prompted.

## Example Run
```
=== File Organizer Script ===
Enter folder path to organize: C:\Users\Admin\Downloads
Enable dry-run mode? (yes/no): no
✅ Organization complete! 25 files moved.
```

## Optional
You can schedule this script to run automatically:
- **Windows:** Task Scheduler
- **Linux/Mac:** Cron job

