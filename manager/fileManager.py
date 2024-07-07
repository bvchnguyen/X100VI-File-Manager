import os
import datetime
import shutil

class fileManager():
    def __init__(self):
        self.path: str
        self.filePath: str
        self.file: str
        self.fileList: list
        self.destination: str

    def isPathValid(self, pathName: str) -> bool:
        return os.path.exists(pathName)

    def path_to_drive(self, pathName: str) -> str:
        if(os.path.exists(pathName)):
            self.path = pathName
        else:
            return ""

    def get_path_to_file(self, file: str) -> None:
        self.path = os.path.join(self.path, file)

    def get_files_by_type(self, fileType: str):
        self.fileList = [f for f in os.listdir(self.path) if f.endswith(fileType)]
        if self.fileList.__len__() != 0:
            return self.fileList
            

    def create_folder(self, rootPath: str, folderName: str) -> None:
        if self.isPathValid(rootPath):
            os.mkdir(os.path.join(rootPath, folderName))
            print(f"Created folder: {folderName} in {rootPath}")

    def get_file_by_index(self, index: int) -> str:
        if index < self.fileList.__len__():
            self.file = self.fileList[index]
            return self.file
        raise Exception(f"Index out of range")
        
    def move_RAF_file(self, fileName: str, folderName: str):
        if self.isPathValid(self.path) == False:
            return "Path does not exist"
        
        if fileName.endswith(".RAF"):
            shutil.move(self.path, os.path.join(self.destination, folderName, fileName))
            print(f"Moved: {fileName} to {folderName}")
        return
    
    def retrieve_file_metadata(self):
        fileStats = os.stat(self.path)

        metadata = {
            'Name': self.file,
            'Size (MB)': self.sizeFormat(fileStats.st_size),
            'Date Created': self.timeConvert(fileStats.st_ctime), 
            'Date Modified': self.timeConvert(fileStats.st_mtime),
        }

        return metadata

    def timeConvert(self, atime: datetime):
        newtime = datetime.datetime.fromtimestamp(atime)
        return newtime.strftime('%m-%d-%Y')
    
    def sizeFormat(self, size):
        newform = format(size/1024, ".2f")
        return newform + " KB"

    def move_files_by_date_range(self, targetDate: str, dest_path: str) -> None:
        try: 
            targetDate = datetime.datetime.strptime(targetDate, '%m-%d-%Y')
        except ValueError:
            print("Incorrect date format, should be MM-DD-YYYY")
        
        file_count = 0
        for file in os.listdir(self.path):
            print(file)
            if(file.endswith(".RAF") == False):
                continue
            fileStats = os.stat(file)
            fileDate = self.timeConvert(fileStats.st_ctime)
            if fileDate >= targetDate:
                file_count += 1
                self.move_RAF_file(file, dest_path)
                print(f"Moved: {file})")
            if FileNotFoundError:
                continue
            if(file_count == 0):
                print("No files found in date range")
        print(f"Total files moved: {file_count}")

    def organize_file_by_date():
        return

    def sort_file_by_type():
        return

    def format_sd_card():
        return

    def file_destination():
        return