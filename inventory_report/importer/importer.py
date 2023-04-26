from abc import ABC, abstractclassmethod
import os


class Importer(ABC):
    @abstractclassmethod
    def import_data(cls, file_path: str):
        pass

    @classmethod
    def check_extension(cls, file_path: str, ext: str):
        file_ext = os.path.splitext(file_path)[1]
        if file_ext != ext:
            raise ValueError("Invalid file type. Please provide a CSV file.")
