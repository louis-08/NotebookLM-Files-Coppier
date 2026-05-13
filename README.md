# flatten_folder

A simple Python script that copies all files from a folder (including all subfolders, no matter how deep) into a single flat destination folder — no subdirectories.

The source folder is left completely unchanged.

## Usage

```bash
python flatten_folder.py <source_folder> <destination_folder>
```

### Examples

**Linux / macOS / Git Bash**
```bash
python flatten_folder.py ~/Documents/MyStuff ~/Desktop/Flattened
```

**Windows (PowerShell / CMD)**
```powershell
python flatten_folder.py "C:\Users\You\Documents\MyStuff" "C:\Users\You\Desktop\Flattened"
```

> If the folder name contains spaces or special characters (e.g. brackets), wrap the path in quotes.

## Behavior

- The destination folder is created automatically if it doesn't exist.
- Files are **copied**, not moved — the source is never modified.
- File metadata (timestamps etc.) is preserved.
- **Name collisions** are handled automatically: if two files from different subfolders share the same name, the second becomes `filename_1.ext`, the third `filename_2.ext`, and so on.

## Requirements

Python 3.6+ — no external dependencies.
