"""
estoque.py — TIME 5: ESTOQUE

Responsabilidade: cuidar da quantidade de cada produto.
É o único arquivo que pode mudar produtos[codigo]["quantidade"].

Prefixos: verificar_, baixar_, repor_, situacao_, produtos_, contar_
Depende de: cadastro.py (T3) — buscar_produto
Usado por: interface.py (T1) e main.py (T6)

Combinados:
- A quantidade nunca fica negativa.
- Produto com quantidade <= ESTOQUE_MINIMO está "BAIXO"; com 0 está "ESGOTADO".
"""

from cadastro import buscar_produto

ESTOQUE_MINIMO = 5


def verificar_estoque(produtos, codigo, quantidade):
    """Devolve True se o produto existe E tem quantidade suficiente para vender."""
    # Dica: use buscar_produto; se vier None, devolva False.
    pass  # TODO Time 5


def baixar_estoque(produtos, codigo, quantidade):
    """Tira unidades do estoque (venda). Devolve False se não tiver o suficiente."""
    # Dica: chame verificar_estoque antes de subtrair.
    pass  # TODO Time 5


def repor_estoque(produtos, codigo, quantidade):
    """Soma unidades no estoque (reposição). Devolve False se o produto não existir."""
    pass  # TODO Time 5


def situacao_produto(produto):
    """Devolve "ESGOTADO" (0), "BAIXO" (até o mínimo) ou "OK". A ordem dos if importa!"""
    pass  # TODO Time 5


def produtos_em_falta(produtos):
    """Devolve um dicionário só com os produtos BAIXO ou ESGOTADO ({codigo: produto})."""
    # Dica: comece com em_falta = {} e vá adicionando os que não estão "OK".
    pass  # TODO Time 5


def contar_unidades(produtos):
    """Soma a quantidade de todos os produtos (total de unidades na cantina)."""
    pass  # TODO Time 5


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python estoque.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]

    print("verificar_estoque(1, 5) ->", verificar_estoque(produtos, 1, 5), "(esperado: True)")
    print("verificar_estoque(1, 50) ->", verificar_estoque(produtos, 1, 50), "(esperado: False)")
    print("verificar_estoque(99, 1) ->", verificar_estoque(produtos, 99, 1), "(esperado: False)")

    print("baixar_estoque(1, 15) ->", baixar_estoque(produtos, 1, 15), "(esperado: True)")
    print("quantidade da coxinha ->", produtos[1]["quantidade"], "(esperado: 5)")
    print("baixar_estoque(1, 10) ->", baixar_estoque(produtos, 1, 10), "(esperado: False, nao muda)")
    print("quantidade da coxinha ->", produtos[1]["quantidade"], "(esperado: 5)")

    print("repor_estoque(3, 10) ->", repor_estoque(produtos, 3, 10), "(esperado: True)")
    print("quantidade do pao de queijo ->", produtos[3]["quantidade"], "(esperado: 14)")
    print("repor_estoque(99, 1) ->", repor_estoque(produtos, 99, 1), "(esperado: False)")

    print("situacao_produto(coxinha) ->", situacao_produto(produtos[1]), "(esperado: BAIXO)")
    print("situacao_produto(suco) ->", situacao_produto(produtos[2]), "(esperado: OK)")
    baixar_estoque(produtos, 1, 5)
    print("situacao_produto(coxinha zerada) ->", situacao_produto(produtos[1]), "(esperado: ESGOTADO)")

    print("produtos_em_falta ->", list(produtos_em_falta(produtos)), "(esperado: [1])")
    print("contar_unidades ->", contar_unidades(produtos), "(esperado: 24)")
