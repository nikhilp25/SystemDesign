from abc import ABC, abstractmethod

class DataParser(ABC):
    def _parse(self):
        self._open()
        self._dataParser()
        self.close()

    def _open(self):
        print("Opening the file")

    def close(self):
        print("Closing the file")
    
    @abstractmethod
    def _dataParser(self):
        pass

class CSVParser(DataParser):
    def _dataParser(self):
        print("Parsing CSV Data")

class JSONParser(DataParser):
    def _dataParser(self):
        print("Parsing JSON Data")

csv = CSVParser()
json = JSONParser()

csv._parse()
json._parse()