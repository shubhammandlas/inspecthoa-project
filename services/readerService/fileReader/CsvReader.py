from services.readerService.fileReader.FileReader import FileReader
import csv

class CsvReader(FileReader):
    def __init__(self, file):
        self.file = file
    
    def read(self):
        fileBinary = self.file.read()
        file_contents = fileBinary.decode('utf-8')
        csv_reader = csv.DictReader(file_contents.splitlines())
        data = [row for row in csv_reader]
        return data
