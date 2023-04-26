from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        oldest_date = min(item['data_de_fabricacao'] for item in data)
        nearest_expire_date = min(
            item['data_de_validade'] for item in data
            if item['data_de_validade'] >= datetime.now().strftime('%Y-%m-%d')
        )
        most_products_company = max(
            set(item['nome_da_empresa'] for item in data),
            key=[item['nome_da_empresa'] for item in data].count
        )

        report = [
            f"Data de fabricação mais antiga: {oldest_date}",
            f"Data de validade mais próxima: {nearest_expire_date}",
            f"Empresa com mais produtos: {most_products_company}"
        ]
        return "\n".join(report)
