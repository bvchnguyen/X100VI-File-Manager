import os
import sys
from datetime import datetime

from manager.fileManager import fileManager

def main():

    fm = fileManager()

    fm.path_to_drive("/Volumes/X100VI/DCIM/100_FUJI")

    if (fm.path == ""):
        print("Path does not exist")
        sys.exit(1)

    fm.get_files_by_type(".RAF")

    if (fm.fileList.__len__() == 0):
        print("No RAF files found")
        sys.exit(1)

    fileTest = fm.get_file_by_index(0)
    fm.get_path_to_file(fileTest)
    print(fm.retrieve_file_metadata())


if __name__ == "__main__":
    main()