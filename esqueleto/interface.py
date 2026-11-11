"""
interface.py — TIME 1: TELA (prints)

Responsabilidade: tudo o que aparece na tela — título, menu, tabela,
recibo, relatório e mensagens. Não lê teclado e não altera dicionários.
Toda função devolve None (só imprime).

Prefixo: mostrar_
Depende de: calculos.py (T4) — formatar_dinheiro
            estoque.py  (T5) — situacao_produto
Usado por: coleta.py (T2) e main.py (T6)

Dica: nome.ljust(20) completa o texto com espaços até 20 letras (alinha à esquerda);
      texto.rjust(10) alinha à direita. É assim que a tabela fica alinhada.
"""

from calculos import formatar_dinheiro
from estoque import situacao_produto

LARGURA = 56


def mostrar_titulo():
    """Imprime o nome do sistema entre duas linhas."""
    # Dica: "=" * LARGURA desenha uma linha; "TEXTO".center(LARGURA) centraliza.
    pass  # TODO Time 1


def mostrar_menu():
    """Imprime as opções do menu principal (1 a 7 e 0 para sair)."""
    # 1 Cadastrar produto · 2 Listar produtos · 3 Vender · 4 Repor estoque
    # 5 Atualizar produto · 6 Remover produto · 7 Relatório · 0 Sair
    pass  # TODO Time 1


def mostrar_tabela_produtos(produtos):
    """Imprime uma tabela: código, nome, preço, quantidade e situação."""
    # Para cada codigo em produtos: monte a linha com ljust/rjust,
    # preço com formatar_dinheiro (T4) e situação com situacao_produto (T5).
    # Se o dicionário estiver vazio, avise "(nenhum produto cadastrado)".
    pass  # TODO Time 1


def mostrar_recibo(venda, produtos):
    """Imprime o recibo de uma venda: produto, quantidade, preço e total."""
    # venda = {"produto": codigo, "quantidade": int, "total": float}
    # O nome e o preço vêm de produtos[venda["produto"]].
    pass  # TODO Time 1


def mostrar_relatorio(resumo):
    """
    Imprime o relatório da cantina. Recebe o dicionário montado em fluxo_relatorio:
    {"quantidade_vendas", "total_vendas", "media_vendas", "unidades", "valor_estoque", "caixa"}
    """
    pass  # TODO Time 1


def mostrar_mensagem(texto, tipo):
    """Imprime o texto com um prefixo: tipo pode ser "ok", "erro", "aviso" ou "info"."""
    # Dica: um dicionário {"ok": "[OK] ", "erro": "[ERRO] ", ...} evita vários if.
    pass  # TODO Time 1


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python interface.py)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from dados import criar_sistema

    sistema = criar_sistema()
    mostrar_titulo()
    mostrar_menu()
    mostrar_tabela_produtos(sistema["produtos"])
    mostrar_recibo({"produto": 1, "quantidade": 2, "total": 12.0}, sistema["produtos"])
    mostrar_relatorio({
        "quantidade_vendas": 1, "total_vendas": 12.0, "media_vendas": 12.0,
        "unidades": 32, "valor_estoque": 165.0, "caixa": 12.0,
    })
    mostrar_mensagem("Produto cadastrado", "ok")
    mostrar_mensagem("Produto não encontrado", "erro")
    mostrar_mensagem("Estoque baixo", "aviso")
    mostrar_mensagem("Até logo", "info")
