"""
cadastro.py — TIME 3: CADASTRO (guardar e achar)

Responsabilidade: guardar e localizar registros nos dicionários.
É o arquivo BASE: não importa nenhum outro time.

Prefixos: gerar_, existe, cadastrar_, buscar_, registrar_
Depende de: ninguém
Usado por: estoque.py (T5), main.py / atualizacao.py (T6)

Combinados:
- Códigos são números inteiros gerados por gerar_codigo (maior código + 1, começando em 1).
- cadastrar_ e registrar_ devolvem o código gerado.
- buscar_ devolve o dicionário encontrado ou None quando não acha.
"""


def gerar_codigo(dicionario):
    """Devolve o próximo código livre: o maior código + 1 (ou 1 se estiver vazio)."""
    # Dica: percorra o dicionário com for guardando o maior código, depois some 1.
    pass  # TODO Time 3


def existe(dicionario, codigo):
    """Devolve True se o código está no dicionário."""
    # Dica: a palavra "in" resolve em uma linha.
    pass  # TODO Time 3


def cadastrar_produto(produtos, dados):
    """
    Gera um código novo e guarda produtos[codigo] = dados.
    'dados' vem pronto de ler_dados_produto(): {"nome", "preco", "quantidade"}.
    Devolve o código gerado.
    """
    pass  # TODO Time 3


def buscar_produto(produtos, codigo):
    """Devolve o dicionário do produto, ou None se o código não existir."""
    pass  # TODO Time 3


def buscar_codigo_por_nome(produtos, nome):
    """
    Procura um produto pelo nome (sem diferenciar maiúsculas de minúsculas).
    Devolve o código do produto, ou None se não achar.
    """
    # Dica: compare produtos[codigo]["nome"].lower() com nome.lower().
    pass  # TODO Time 3


def registrar_venda(vendas, venda):
    """
    Guarda a venda montada pelo Time 6.
    venda = {"produto": codigo, "quantidade": int, "total": float}
    Devolve o código gerado.
    """
    pass  # TODO Time 3


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python cadastro.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]

    print("gerar_codigo ->", gerar_codigo(produtos), "(esperado: 4)")
    print("gerar_codigo({}) ->", gerar_codigo({}), "(esperado: 1)")
    print("existe(2) ->", existe(produtos, 2), "(esperado: True)")
    print("existe(99) ->", existe(produtos, 99), "(esperado: False)")
    print("buscar_produto(1) ->", buscar_produto(produtos, 1))
    print("buscar_produto(99) ->", buscar_produto(produtos, 99), "(esperado: None)")

    novo = {"nome": "Brigadeiro", "preco": 2.5, "quantidade": 30}
    codigo = cadastrar_produto(produtos, novo)
    print("cadastrar_produto ->", codigo, "(esperado: 4)")
    print("buscar_codigo_por_nome('coxinha') ->", buscar_codigo_por_nome(produtos, "coxinha"), "(esperado: 1)")
    print("buscar_codigo_por_nome('pizza') ->", buscar_codigo_por_nome(produtos, "pizza"), "(esperado: None)")

    venda = {"produto": 1, "quantidade": 2, "total": 12.0}
    print("registrar_venda ->", registrar_venda(sistema["vendas"], venda), "(esperado: 1)")
    print("vendas ->", sistema["vendas"])
