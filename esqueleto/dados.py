"""
dados.py — COMPARTILHADO POR TODOS OS TIMES

Dados de exemplo para todo mundo testar com o mesmo cenário.
Este arquivo já está pronto: NÃO precisa alterar.

Uso em qualquer arquivo:
    from dados import criar_sistema
    sistema = criar_sistema()
    print(sistema["produtos"][1]["nome"])   # Coxinha
"""


def criar_sistema():
    """Devolve o dicionário 'sistema' completo, com dados de exemplo."""
    return {
        "produtos": {
            1: {"nome": "Coxinha", "preco": 6.0, "quantidade": 20},
            2: {"nome": "Suco de laranja", "preco": 4.5, "quantidade": 10},
            3: {"nome": "Pão de queijo", "preco": 3.0, "quantidade": 4},
        },
        "vendas": {},
        "caixa": 0.0,
    }


def criar_sistema_vazio():
    """Devolve o dicionário 'sistema' sem nenhum produto (para testar cadastro do zero)."""
    return {
        "produtos": {},
        "vendas": {},
        "caixa": 0.0,
    }


if __name__ == "__main__":
    sistema = criar_sistema()
    print("Produtos cadastrados:", len(sistema["produtos"]))
    print("Vendas registradas:", len(sistema["vendas"]))
    print("Caixa inicial:", sistema["caixa"])
