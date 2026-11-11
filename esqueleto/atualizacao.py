"""
atualizacao.py — TIME 6 (parte 1): ATUALIZAR E REMOVER

Responsabilidade: o "U" (update) e o "D" (delete) do CRUD, mais o caixa.

Prefixos: atualizar_, remover_
Depende de: cadastro.py (T3) — existe
Usado por: main.py (T6)

Combinados:
- Só "nome" e "preco" podem ser alterados aqui. A "quantidade" só muda
  por venda ou reposição (estoque.py, Time 5).
- Devolvem True quando deu certo e False quando o código (ou campo) não existe.
"""

from cadastro import existe

CAMPOS_EDITAVEIS = ["nome", "preco"]


def atualizar_produto(produtos, codigo, campo, novo_valor):
    """Troca o valor de um campo do produto. Devolve False se o código ou o campo for inválido."""
    # Duas cercas: existe(produtos, codigo)? campo in CAMPOS_EDITAVEIS?
    pass  # TODO Time 6


def remover_produto(produtos, codigo):
    """Apaga o produto do dicionário. Devolve False se o código não existir."""
    # Dica: del produtos[codigo]
    pass  # TODO Time 6


def atualizar_caixa(sistema, valor):
    """Soma 'valor' ao caixa (positivo em venda). Devolve o novo saldo."""
    pass  # TODO Time 6


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python atualizacao.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]

    print("atualizar_produto(1, 'preco', 7.0) ->", atualizar_produto(produtos, 1, "preco", 7.0), "(esperado: True)")
    print("preco da coxinha ->", produtos[1]["preco"], "(esperado: 7.0)")
    print("atualizar_produto(1, 'quantidade', 0) ->", atualizar_produto(produtos, 1, "quantidade", 0), "(esperado: False)")
    print("atualizar_produto(99, 'nome', 'x') ->", atualizar_produto(produtos, 99, "nome", "x"), "(esperado: False)")

    print("remover_produto(3) ->", remover_produto(produtos, 3), "(esperado: True)")
    print("remover_produto(3) de novo ->", remover_produto(produtos, 3), "(esperado: False)")
    print("codigos restantes ->", list(produtos), "(esperado: [1, 2])")

    print("atualizar_caixa(+12) ->", atualizar_caixa(sistema, 12.0), "(esperado: 12.0)")
    print("atualizar_caixa(+4.5) ->", atualizar_caixa(sistema, 4.5), "(esperado: 16.5)")
