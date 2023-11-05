from services.readerService.fileReader.CsvReader import CsvReader
from services.readerService.fileReader.XlsxReader import XlsxReader


class FileReaderFactory():

    def getReader(self, file):
        name = file.filename
        if (name.endswith('.csv')):
            reader = CsvReader(file)

        elif (name.endswith('.xlsx')):
            reader = XlsxReader(file)

        data = reader.read()
        return data
