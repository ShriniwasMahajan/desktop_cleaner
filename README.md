# Desktop Cleaner

## Description

Desktop Cleaner is a user-friendly Python application that helps you organize your desktop automatically. It sorts your files based on their extensions and creation dates into dedicated folders, promoting a clutter-free and well-structured desktop environment.

## Features

### Automatic File Sorting: 
- Sorts files by extension and creation date, creating folders for each category.
### Unclassified File Handling: 
- Organizes files with unknown extensions into an "Others" or "Unknowns" folder.
### Safe Duplicate Handling: 
- Renames duplicate files to prevent accidental data loss, using a numbering scheme (e.g., "filename_2.ext").
### No File Data Handling: 
- Falls back to the current date for sorting files without creation data.
### Optional Startup Integration: 
- Can be set to run automatically at system boot for continuous organization.

## Installation
1. Download or clone this repository
2. Install required modules
   ```
   pip install pathlib watchdog datetime typing
   ```
3. Customize the folder paths and names in deskcleaner.py according the system

## Usage

1. Open a terminal or command prompt and navigate to the directory containing the desktop_cleaner.py script.
2. Run one of the scripts below:
   ```
   py deskcleaner.py
   python deskcleaner.py
   ```
