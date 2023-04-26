from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def stock_products_by_company(file):
        companies = {}
        for item in file:
            if item["nome_da_empresa"] in companies:
                companies[item["nome_da_empresa"]] += 1
            else:
                companies[item["nome_da_empresa"]] = 1
        return companies

    @classmethod
    def generate(cls, file):

        report = super().generate(file)

        stock_products = cls.stock_products_by_company(file)

        report += "\nProdutos estocados por empresa:\n"
        for company, count in stock_products.items():
            report += f"- {company}: {count}\n"

        return report
