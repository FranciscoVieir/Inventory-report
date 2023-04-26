from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    products_list = [
        {
            "id": "1",
            "nome_do_produto": "Arroz",
            "nome_da_empresa": "Tmarket",
            "data_de_fabricacao": "2021-02-18",
            "data_de_validade": "2023-09-17",
            "numero_de_serie": "KQ97 934B 9212 837N A28F",
            "instrucoes_de_armazenamento": "instrucao 1",
        },
        {
            "id": "2",
            "nome_do_produto": "Feijão",
            "nome_da_empresa": "Tmarket",
            "data_de_fabricacao": "2020-12-06",
            "data_de_validade": "2023-12-25",
            "numero_de_serie": "RV38 057W 6451 943O D85E",
            "instrucoes_de_armazenamento": "instrucao 2",
        },
        {
            "id": "3",
            "nome_do_produto": "Suco",
            "nome_da_empresa": "GMARKET",
            "data_de_fabricacao": "2020-12-22",
            "data_de_validade": "2024-11-07",
            "numero_de_serie": "TY22 6318 9411 127L H39B",
            "instrucoes_de_armazenamento": "instrucao 3",
        },
        {
            "id": "4",
            "nome_do_produto": "Sabonete",
            "nome_da_empresa": "COMB FARMACIA",
            "data_de_fabricacao": "2020-12-24",
            "data_de_validade": "2025-08-19",
            "numero_de_serie": "DG95 843K 7551 456P J76A",
            "instrucoes_de_armazenamento": "instrucao 4",
        },
        {
            "id": "5",
            "nome_do_produto": "Creme dental",
            "nome_da_empresa": "Moore Medical LLC",
            "data_de_fabricacao": "2021-04-14",
            "data_de_validade": "2025-01-14",
            "numero_de_serie": "KL78 276D 3223 751K S19V",
            "instrucoes_de_armazenamento": "instrucao 5",
        },
        {
            "id": "6",
            "nome_do_produto": "Desinfetante",
            "nome_da_empresa": "COMB FARMACIA",
            "data_de_fabricacao": "2021-07-18",
            "data_de_validade": "2024-10-05",
            "numero_de_serie": "JHG54321",
            "instrucoes_de_armazenamento": "instrucao 6",
        },
        {
            "id": "7",
            "nome_do_produto": "Leite",
            "nome_da_empresa": "REMLAMP",
            "data_de_fabricacao": "2021-07-17",
            "data_de_validade": "2023-11-18",
            "numero_de_serie": "FDS36985",
            "instrucoes_de_armazenamento": "instrucao 7",
        },
        {
            "id": "8",
            "nome_do_produto": "Sabonete",
            "nome_da_empresa": "GMARKET",
            "data_de_fabricacao": "2021-02-22",
            "data_de_validade": "2024-03-14",
            "numero_de_serie": "ABC12345",
            "instrucoes_de_armazenamento": "instrucao 8",
        },
        {
            "id": "9",
            "nome_do_produto": "Sabão em pó",
            "nome_da_empresa": "Tmarket",
            "data_de_fabricacao": "2020-09-06",
            "data_de_validade": "2024-05-21",
            "numero_de_serie": "XYZ67890",
            "instrucoes_de_armazenamento": "instrucao 9",
        },
        {
            "id": "10",
            "nome_do_produto": "Óleo",
            "nome_da_empresa": "Tmarket",
            "data_de_fabricacao": "2020-12-08",
            "data_de_validade": "2023-12-08",
            "numero_de_serie": "QWE24680",
            "instrucoes_de_armazenamento": "instrucao 10",
        },
    ]

    colored_keys = [
        "\033[32mData de fabricação mais antiga:\033[0m",
        "\033[32mData de validade mais próxima:\033[0m",
        "\033[32mEmpresa com mais produtos:\033[0m",
    ]

    colored_values = [
        "\033[36m2020-09-06\033[0m",
        "\033[36m2023-09-17\033[0m",
        "\033[31mTmarket\033[0m",
    ]

    expected_simple_report = (
        f"{colored_keys[0]} {colored_values[0]}\n"
        f"{colored_keys[1]} {colored_values[1]}\n"
        f"{colored_keys[2]} {colored_values[2]}"
    )

    expected_complete_report = (
        f"{colored_keys[0]} {colored_values[0]}\n"
        f"{colored_keys[1]} {colored_values[1]}\n"
        f"{colored_keys[2]} {colored_values[2]}\n"
        "Produtos estocados por empresa:\n"
        "- Tmarket: 4\n"
        "- GMARKET: 2\n"
        "- COMB FARMACIA: 2\n"
        "- Moore Medical LLC: 1\n"
        "- REMLAMP: 1\n"
    )

    colored_simple_report = ColoredReport(SimpleReport).generate(products_list)
    colored_complete_report = ColoredReport(CompleteReport).generate(
        products_list
    )

    assert colored_simple_report == expected_simple_report
    assert colored_complete_report == expected_complete_report
