from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        1,
        "Produto M",
        "Empresa MALAS.",
        "01/01/2022",
        "01/01/2023",
        "029301",
        "Malas"
    )

    assert produto.id == 1
    assert produto.nome_do_produto == "Produto M"
    assert produto.nome_da_empresa == "Empresa MALAS."
    assert produto.data_de_fabricacao == "01/01/2022"
    assert produto.data_de_validade == "01/01/2023"
    assert produto.numero_de_serie == "029301"
    assert produto.instrucoes_de_armazenamento == "Malas"
