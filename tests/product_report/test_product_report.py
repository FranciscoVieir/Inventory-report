from inventory_report.inventory.product import Product


def test_relatorio_produto():
    mock = {
        "id": 1,
        "nome_da_empresa": "Empresa Wolks",
        "nome_do_produto": "Pizza de Pepperoni",
        "data_de_fabricacao": "2023/07/25",
        "data_de_validade": "2023/08/25",
        "numero_de_serie": "2B36 2C6Y 96BP TU35",
        "instrucoes_de_armazenamento": "Mantenha em um lugar congelado",
    }

    product = Product(**mock)

    expected = (
        f"O produto {mock['nome_do_produto']}"
        f" fabricado em {mock['data_de_fabricacao']}"
        f" por {mock['nome_da_empresa']} com validade"
        f" até {mock['data_de_validade']}"
        f" precisa ser armazenado {mock['instrucoes_de_armazenamento']}."
    )

    assert repr(product) == expected
