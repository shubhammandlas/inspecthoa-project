from abc import ABC, abstractmethod

# Interface class
class FileReader(ABC):
    @abstractmethod
    def read(self):
        pass