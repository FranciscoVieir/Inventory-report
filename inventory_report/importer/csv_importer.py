import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path: str):
        if not file_path.endswith('.csv'):
            raise ValueError("Invalid file type. Please provide a CSV file.")

        with open(file_path, encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",", quotechar='"')
            documents_list = list(csv_reader)

        return documents_list
