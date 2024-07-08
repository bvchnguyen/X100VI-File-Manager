import os
import sys

from manager.fileManager import fileManager
from dotenv import load_dotenv

def main():
    load_dotenv('.env')
    fm = fileManager()
    fm.destination = os.getenv('FILE_DEST')
    fm.path_to_drive(os.getenv('FILE_PATH'))

    if (fm.path == "" or fm.destination == ""):
        print("Path does not exist")
        sys.exit(1)

    targetDate = input("Enter the date of the files to move (MM-DD-YYYY): ")
    
    raf_folder = 'test_raf'
    jpg_folder = 'test_jpg'

    fm.create_folder(fm.path, raf_folder)
    fm.create_folder(fm.path, jpg_folder)
    fm.copy_files_with_date(targetDate, raf_folder, ".RAF")
    fm.copy_files_with_date(targetDate, jpg_folder, ".JPG")

    print(f"Total files copied and moved: {fm.moveCount}")

    fm.move_dir_to_dest(raf_folder)
    fm.move_dir_to_dest(jpg_folder)

if __name__ == "__main__":
    main()