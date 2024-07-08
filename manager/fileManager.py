import os
from datetime import datetime
import shutil

class fileManager():
    def __init__(self):
        self.path: str
        self.filePath: str
        self.file: str
        self.fileList: list
        self.destination: str
        self.moveCount: int = 0

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
            print(f"Created folder: {folderName} in {rootPath}")
            os.mkdir(os.path.join(rootPath, folderName))

    def retrieve_file_metadata(self, path: str):
        fileStats = os.stat(path)

        metadata = {
            'Size_MB': self.sizeFormat(fileStats.st_size),
            'Date_created': self.timeConvert(fileStats.st_ctime),
            'Date_modified': self.timeConvert(fileStats.st_mtime),
        }
        return metadata

    def timeConvert(self, atime: datetime):
        newtime = datetime.fromtimestamp(atime)
        return newtime.strftime('%m-%d-%Y')
    
    def sizeFormat(self, size):
        newform = format(size/1024, ".2f")
        return newform + " KB"
    
    def copy_files_with_date(self, targetDate: str, folderName: str, fileType: str):
        for f in os.listdir(self.path):
            if f.endswith(fileType):
                self.filePath = os.path.join(self.path, f)
                fileStats = self.retrieve_file_metadata(self.filePath)
                file_date = datetime.strptime(fileStats['Date_created'], '%m-%d-%Y')
                target_date = datetime.strptime(targetDate, '%m-%d-%Y')
                if file_date == target_date:
                    self.moveCount += 1
                    shutil.copy2(self.filePath, os.path.join(self.path, folderName))
                    print(f'{self.moveCount}. Copied {f} -> {self.path}/{folderName}')   
    
    def move_dir_to_dest(self, folderName: str):
        shutil.move(os.path.join(self.path, folderName), self.destination)