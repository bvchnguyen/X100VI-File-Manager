import os
import sys
from datetime import datetime
import shutil

from manager.fileManager import fileManager

def main():


    fm = fileManager()
    fm.destination = '/Users/bvch/Library/CloudStorage/GoogleDrive-bvchnguyen@gmail.com'
    fm.path_to_drive("/Volumes/X100VI/DCIM/100_FUJI")

    print(f"Google drive: {os.path.exists('/Users/bvch/Library/CloudStorage/GoogleDrive-bvchnguyen@gmail.com')}")

    if (fm.path == ""):
        print("Path does not exist")
        sys.exit(1)

    targetDate = input("Enter the date of the files to move (MM-DD-YYYY): ")
    raf_folder = 'test_raf'
    jpg_folder = 'test_jpg'
    fm.create_folder(fm.path, raf_folder)
    fm.create_folder(fm.path, jpg_folder)
    fm.copy_files_with_date(targetDate, raf_folder, ".RAF")
    fm.copy_files_with_date(targetDate, jpg_folder, ".JPG")


    # get user input
    # user_answer = True
    # while True:
    #     folder = input("Enter folder name: ")
    #     fm.create_folder(fm.path, folder)
    #     fm.copy_files_with_date("07-07-2024", str(folder))
    #     get_started = input("Do you want to organize more files? (Y/N): ").strip().lower()
    #     if get_started == "n":
    #         shutil.move(os.path.join(fm.path, folder), fm.destination)
    #         print("Goodbye!")
    #         sys.exit(1)

if __name__ == "__main__":
    main()