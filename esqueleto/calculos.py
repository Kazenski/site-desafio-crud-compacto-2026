"""
calculos.py — TIME 4: CÁLCULOS

Responsabilidade: toda conta do sistema. As funções só recebem números
(ou dicionários), calculam e devolvem o resultado. Não usam print nem input.

Prefixos: calcular_, formatar_
Depende de: ninguém
Usado por: interface.py (T1) e main.py (T6)

Combinados:
- Todo valor em dinheiro passa por round(valor, 2) antes de ser devolvido.
- Nenhuma função altera o dicionário que recebe.
"""


def calcular_subtotal(preco, quantidade):
    """Devolve preco × quantidade, com 2 casas decimais."""
    pass  # TODO Time 4


def calcular_troco(total, valor_pago):
    """Devolve valor_pago − total, com 2 casas decimais."""
    pass  # TODO Time 4


def calcular_total_vendas(vendas):
    """Soma o campo 'total' de todas as vendas."""
    # Dica: for codigo in vendas: soma = soma + vendas[codigo]["total"]
    pass  # TODO Time 4


def calcular_media_vendas(vendas):
    """Devolve o valor médio por venda. Se não houver vendas, devolve 0.0."""
    # Cuidado: dividir por zero dá erro. Teste len(vendas) == 0 antes.
    pass  # TODO Time 4


def calcular_valor_estoque(produtos):
    """Soma preco × quantidade de todos os produtos (quanto vale o que está na prateleira)."""
    pass  # TODO Time 4


def formatar_dinheiro(valor):
    """Transforma 6.5 em 'R$ 6,50' (texto)."""
    # Dica: f"{valor:.2f}" dá "6.50"; depois troque o ponto por vírgula com .replace()
    pass  # TODO Time 4


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python calculos.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    produtos = sistema["produtos"]
    vendas = {
        1: {"produto": 1, "quantidade": 2, "total": 12.0},
        2: {"produto": 2, "quantidade": 1, "total": 4.5},
    }

    print("calcular_subtotal(6.0, 3) ->", calcular_subtotal(6.0, 3), "(esperado: 18.0)")
    print("calcular_troco(12.0, 20.0) ->", calcular_troco(12.0, 20.0), "(esperado: 8.0)")
    print("calcular_total_vendas ->", calcular_total_vendas(vendas), "(esperado: 16.5)")
    print("calcular_media_vendas ->", calcular_media_vendas(vendas), "(esperado: 8.25)")
    print("calcular_media_vendas({}) ->", calcular_media_vendas({}), "(esperado: 0.0)")
    print("calcular_valor_estoque ->", calcular_valor_estoque(produtos), "(esperado: 177.0)")
    print("formatar_dinheiro(6.5) ->", formatar_dinheiro(6.5), "(esperado: R$ 6,50)")
    print("formatar_dinheiro(177) ->", formatar_dinheiro(177), "(esperado: R$ 177,00)")
