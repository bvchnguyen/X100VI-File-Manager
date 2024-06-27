import os
import datetime

class fileManager():
    def __init__(self):
        self.path: str
        self.filePath: str
        self.file: str
        self.fileList: list
        self.destination: str

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

    def get_file_by_index(self, index: int) -> str:
        if index < self.fileList.__len__():
            self.file = self.fileList[index]
            return self.file
        raise Exception(f"Index out of range")
        
    def move_RAF_file():
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

    def get_files_by_date_range(self, startDate: str, endDate: str):
        return

    def organize_file_by_date():
        return

    def sort_file_by_type():
        return

    def format_sd_card():
        return

    def file_destination():
        return