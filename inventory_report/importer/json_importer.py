import json
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        super(JsonImporter, cls).check_extension(file_path, '.json')
        with open(file_path, "r") as json_file:
            dict_list = json.load(json_file)

        return dict_list
