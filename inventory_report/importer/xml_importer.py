import xml.etree.ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        super(XmlImporter, cls).check_extension(file_path, ".xml")
        data = ET.parse(file_path)
        dataRoot = data.getroot()

        dict_list = []
        for element in dataRoot:
            dictionary = {}
            for sub_element in element:
                dictionary[sub_element.tag] = sub_element.text
            dict_list.append(dictionary)

        return dict_list
