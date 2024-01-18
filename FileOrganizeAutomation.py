import os, shutil

# Base path for the user's profile
user_profile_path = os.environ['USERPROFILE']

# Define the standard folder paths
standard_folders = {
    "Pictures": os.path.join(user_profile_path, 'Pictures'),
    "Videos": os.path.join(user_profile_path, 'Videos'),
    "Documents": os.path.join(user_profile_path, 'Documents'),
    "Music": os.path.join(user_profile_path, 'Music'),
    "Archives": os.path.join(user_profile_path, 'Archives'),  
    "Executables": os.path.join(user_profile_path, 'Executables')
    # Add more standard folders as needed
}

# Ensure standard folders exist
for folder in standard_folders.values():
    os.makedirs(folder, exist_ok=True)

# File mappings to standard folders
file_mappings = {
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".txt", ".md", ".pdf", ".docx", ".pptx", ".xlsx", ".csv", ".xpi", ".alp"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar.gz"],
    "Executables": [".exe", ".msi"],

    # Add more mappings as needed
}

# Ensure standard folders exist
for folder in standard_folders.values():
    os.makedirs(folder, exist_ok=True)

# Path to the Downloads folder
downloads_path = os.path.join(user_profile_path, 'Downloads')

# Organize files from Downloads
for file in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file)
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in file_mappings.items():
            if file_ext in extensions:
                destination_path = standard_folders[folder]
                shutil.move(file_path, destination_path)
                moved = True
                break

        if not moved:
            print(f"Unorganized file: {file}")
