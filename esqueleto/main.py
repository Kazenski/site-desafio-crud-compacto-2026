"""
main.py — TIME 6 (parte 2): LIGAR TUDO

Responsabilidade: o menu principal e os fluxos completos (cada opção do menu),
chamando as funções dos outros cinco times na ordem certa.

Prefixos: fluxo_, executar_
Depende de: TODOS os arquivos
Para rodar:  python main.py

Já vêm prontos (servem de modelo): fluxo_cadastrar_produto, fluxo_listar_produtos,
fluxo_repor_estoque, fluxo_relatorio e executar_sistema.
O Time 6 escreve: fluxo_vender, fluxo_atualizar_produto e fluxo_remover_produto.
Siga o passo a passo da seção 8 do site e troque os comentários por código.
"""

from dados import criar_sistema

import interface
import coleta
import cadastro
import calculos
import estoque
import atualizacao


# ===========================================================================
# PRONTOS — modelos de como ligar as peças
# ===========================================================================

def fluxo_cadastrar_produto(sistema):
    """Opção 1. Passo a passo 8.1 do site."""
    dados = coleta.ler_dados_produto()                              # T2
    codigo = cadastro.cadastrar_produto(sistema["produtos"], dados)  # T3
    interface.mostrar_mensagem(f"Produto {codigo} cadastrado!", "ok")  # T1


def fluxo_listar_produtos(sistema):
    """Opção 2."""
    interface.mostrar_tabela_produtos(sistema["produtos"])


def fluxo_repor_estoque(sistema):
    """Opção 4. Modelo para o fluxo_vender: mostra → pergunta → busca → altera → avisa."""
    produtos = sistema["produtos"]
    interface.mostrar_tabela_produtos(produtos)
    codigo = coleta.ler_inteiro("Código do produto: ", 1)
    produto = cadastro.buscar_produto(produtos, codigo)
    if produto is None:
        interface.mostrar_mensagem("Produto não encontrado", "erro")
        return
    quantidade = coleta.ler_inteiro("Quantas unidades chegaram? ", 1)
    estoque.repor_estoque(produtos, codigo, quantidade)
    interface.mostrar_mensagem(f"{produto['nome']} agora tem {produto['quantidade']} unidades", "ok")


def fluxo_relatorio(sistema):
    """Opção 7. Junta os números dos Times 4 e 5 num dicionário e manda o Time 1 mostrar."""
    produtos = sistema["produtos"]
    vendas = sistema["vendas"]
    resumo = {
        "quantidade_vendas": len(vendas),
        "total_vendas": calculos.calcular_total_vendas(vendas),
        "media_vendas": calculos.calcular_media_vendas(vendas),
        "unidades": estoque.contar_unidades(produtos),
        "valor_estoque": calculos.calcular_valor_estoque(produtos),
        "caixa": sistema["caixa"],
    }
    interface.mostrar_relatorio(resumo)
    em_falta = estoque.produtos_em_falta(produtos)
    if len(em_falta) > 0:
        interface.mostrar_mensagem("Produtos para repor:", "aviso")
        interface.mostrar_tabela_produtos(em_falta)


# ===========================================================================
# TIME 6 — fluxos para escrever
# ===========================================================================

def fluxo_vender(sistema):
    """Opção 3. Passo a passo 8.2 do site — o fluxo que usa todos os times."""
    produtos = sistema["produtos"]

    # 1. escolher o produto (igual ao começo de fluxo_repor_estoque)
    #    interface.mostrar_tabela_produtos(produtos)
    #    codigo = coleta.ler_inteiro("Código do produto: ", 1)
    #    produto = cadastro.buscar_produto(produtos, codigo)
    #    se produto is None -> mostrar_mensagem erro e return

    # 2. quantidade e estoque
    #    quantidade = coleta.ler_inteiro("Quantidade: ", 1)
    #    se not estoque.verificar_estoque(produtos, codigo, quantidade) -> erro e return

    # 3. total e confirmação (até aqui NADA mudou no sistema)
    #    total = calculos.calcular_subtotal(produto["preco"], quantidade)
    #    interface.mostrar_mensagem("Total: " + calculos.formatar_dinheiro(total), "info")
    #    se not coleta.perguntar_sim_nao("Confirmar venda?") -> aviso "Venda cancelada" e return

    # 4. pagamento
    #    valor_pago = coleta.ler_decimal("Valor recebido (R$): ")
    #    while valor_pago < total: avisar e perguntar de novo
    #    troco = calculos.calcular_troco(total, valor_pago)

    # 5. efeitos: estoque, venda, caixa
    #    estoque.baixar_estoque(produtos, codigo, quantidade)
    #    venda = {"produto": codigo, "quantidade": quantidade, "total": total}
    #    cadastro.registrar_venda(sistema["vendas"], venda)
    #    atualizacao.atualizar_caixa(sistema, total)

    # 6. recibo
    #    interface.mostrar_recibo(venda, produtos)
    #    interface.mostrar_mensagem("Troco: " + calculos.formatar_dinheiro(troco), "info")
    pass  # TODO Time 6


def fluxo_atualizar_produto(sistema):
    """Opção 5. Passo a passo 8.3 do site."""
    produtos = sistema["produtos"]
    # 1. mostrar tabela, ler código, buscar produto (se None -> erro e return)
    # 2. campo = coleta.ler_opcao("O que alterar (nome/preco)? ", atualizacao.CAMPOS_EDITAVEIS)
    # 3. se campo == "preco": novo_valor = coleta.ler_decimal(...)  senão: coleta.ler_texto(...)
    # 4. atualizacao.atualizar_produto(produtos, codigo, campo, novo_valor)
    # 5. interface.mostrar_mensagem("Produto atualizado", "ok")
    pass  # TODO Time 6


def fluxo_remover_produto(sistema):
    """Opção 6."""
    produtos = sistema["produtos"]
    # 1. mostrar tabela, ler código, buscar produto (se None -> erro e return)
    # 2. se coleta.perguntar_sim_nao(f"Remover '{produto['nome']}'?"):
    #        atualizacao.remover_produto(produtos, codigo) e mensagem ok
    #    senão: mensagem aviso "Nada foi removido"
    pass  # TODO Time 6


# ===========================================================================
# MENU PRINCIPAL (pronto)
# ===========================================================================

def executar_sistema(sistema):
    """Laço do menu: mostra (T1) → lê (T2) → chama o fluxo. Termina com 0."""
    interface.mostrar_titulo()
    while True:
        interface.mostrar_menu()
        opcao = coleta.ler_opcao("Opção: ", ["0", "1", "2", "3", "4", "5", "6", "7"])
        if opcao == "1":
            fluxo_cadastrar_produto(sistema)
        elif opcao == "2":
            fluxo_listar_produtos(sistema)
        elif opcao == "3":
            fluxo_vender(sistema)
        elif opcao == "4":
            fluxo_repor_estoque(sistema)
        elif opcao == "5":
            fluxo_atualizar_produto(sistema)
        elif opcao == "6":
            fluxo_remover_produto(sistema)
        elif opcao == "7":
            fluxo_relatorio(sistema)
        else:
            interface.mostrar_mensagem("Até logo!", "info")
            return


if __name__ == "__main__":
    sistema = criar_sistema()
    executar_sistema(sistema)
