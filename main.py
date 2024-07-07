import os
import sys
from datetime import datetime

from manager.fileManager import fileManager

def main():


    fm = fileManager()
    fm.destination = '/Users/bvch/Library/CloudStorage/GoogleDrive-bvchnguyen@gmail.com'
    fm.path_to_drive("/Volumes/X100VI/DCIM/100_FUJI")

    print(f"Google drive: {os.path.exists('/Users/bvch/Library/CloudStorage/GoogleDrive-bvchnguyen@gmail.com')}")

    if (fm.path == ""):
        print("Path does not exist")
        sys.exit(1)

    # get user input
    user_answer = True

    while True:
        user_answer = input("Do you want to create a new folder? (Y/N): ").strip().lower()
        if user_answer == "y":
            folder_name = input("Enter folder name: ")
            fm.create_folder(fm.destination, folder_name)
            fm.destination = os.path.join(fm.destination, folder_name)
            break
        elif user_answer == "n":
            break
        else:
            print("Invalid input, please enter 'Y' or 'N'.")

    print(f"New Destination: {fm.destination}")
    fm.get_files_by_type(".RAF")
    fm.move_files_by_date_range("07-02-2024", fm.destination)
    # fm.create_folder(fm.destination, "Odesza")

    # fm.get_files_by_type(".RAF")

    # if (fm.fileList.__len__() == 0):
    #     print("No RAF files found")
    #     sys.exit(1)

    # fileTest = fm.get_file_by_index(0)
    # fm.get_path_to_file(fileTest)
    # print(fm.retrieve_file_metadata())

    # fm.move_RAF_file(fileTest, "Odesza/RAF", False);

if __name__ == "__main__":
    main()