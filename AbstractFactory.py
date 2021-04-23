from __future__ import annotations
from abc import ABC, abstractmethod

class Directory(ABC):
    @abstractmethod
    def addCsv(self):
        pass

    @abstractmethod
    def changeData(self, index):
        pass

    @abstractmethod
    def removeProduct(self, index):
        pass
