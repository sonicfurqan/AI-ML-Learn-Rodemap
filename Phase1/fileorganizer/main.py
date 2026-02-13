from pathlib import Path
import os
import shutil


downloads_path = str(Path.home() / "Downloads")

file_extenation_dict = {
    ".zip": "Zip",
    ".xls": "Files",
    ".xlsx": "Files",
    ".json": "Files",
    ".pdf": "Files",
    ".jpeg": "Files",
    ".jpg": "Files",
    ".csv": "Files",
    ".log": "Files",
    ".yaml": "Files",
    ".xml": "Files",
    ".dat": "Files",
    ".txt": "Files",
    ".docx": "Files",
    ".pptx": "Files",
    ".png": "Files",
}

directory = Path(downloads_path)
for file_path in directory.iterdir():
    if file_path.is_file():
        filename = file_path.name
        extension = file_path.suffix

        folderName = file_extenation_dict.get(extension, "Others")
        folder_path = directory / folderName
        # do not move any un recognized files
        if folderName != "Others":
            if not folder_path.exists():
                os.mkdir(folder_path)

            source = file_path
            destination = folder_path

            try:
                # Moves the file to the destination folder
                shutil.move(source, destination)
            except shutil.Error as e:
                print(f"Move failed for file {source}:  {e}")
