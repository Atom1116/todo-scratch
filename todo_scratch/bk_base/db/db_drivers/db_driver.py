
from abc import ABCMeta, abstractclassmethod
from typing import Dict, Tuple


class DbDriver(metaclass=ABCMeta):

    @abstractclassmethod
    def __enter__(self,):
        pass

    @abstractclassmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @abstractclassmethod
    def connect(self,):
        pass

    @abstractclassmethod
    def disconnect(self,):
        pass

    @abstractclassmethod
    def commit(self,):
        pass

    @abstractclassmethod
    def rollback(self):
        pass

    @abstractclassmethod
    def is_connect(self,) -> bool:
        pass

    @abstractclassmethod
    def query(self, query: str) -> Dict:
        pass

    @abstractclassmethod
    def query_with_param(self, query: str, param: Tuple) -> Dict:
        pass