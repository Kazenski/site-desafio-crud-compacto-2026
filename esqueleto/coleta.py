"""
coleta.py — TIME 2: TECLADO (inputs)

Responsabilidade: todos os input() do sistema. A missão é nunca deixar o
programa quebrar por causa do que foi digitado: se vier letra onde é número,
ou nada onde é obrigatório, avisa e pergunta de novo.

Prefixos: ler_, perguntar_
Depende de: interface.py (T1) — mostrar_mensagem
Usado por: main.py (T6)

Padrão de todas as funções ler_:
    while True:
        resposta = input(mensagem)
        if <a resposta é válida>:
            return <valor convertido>
        mostrar_mensagem("...", "erro")    # e o while repete a pergunta

Dica: "123".isdigit() é True; "12a".isdigit() é False; "".isdigit() é False.
"""

from interface import mostrar_mensagem


def ler_texto(mensagem):
    """Lê um texto obrigatório. Repete enquanto estiver vazio. Devolve sem espaços nas pontas."""
    pass  # TODO Time 2


def ler_inteiro(mensagem, minimo):
    """Lê um número inteiro maior ou igual a 'minimo'. Repete até dar certo."""
    # Dica: resposta.isdigit() and int(resposta) >= minimo
    pass  # TODO Time 2


def ler_decimal(mensagem):
    """Lê um número com casas decimais (aceita 4,50 ou 4.50). Repete até dar certo."""
    # Dica: troque a vírgula por ponto com .replace(",", ".").
    # Para conferir se é um número válido: resposta.replace(".", "", 1).isdigit()
    # (tira UM ponto e vê se sobraram só dígitos: "4.50" -> "450" ok; "4.5.0" -> "4.50" não)
    pass  # TODO Time 2


def ler_opcao(mensagem, opcoes):
    """Lê um texto que precisa estar na lista 'opcoes' (ex.: ["0", "1", "2"]). Repete até estar."""
    pass  # TODO Time 2


def perguntar_sim_nao(mensagem):
    """Pergunta (s/n). Devolve True para s/S/sim e False para qualquer outra coisa."""
    # Dica: .strip().lower() na resposta antes de comparar.
    pass  # TODO Time 2


def ler_dados_produto():
    """Pergunta nome, preço e quantidade e devolve {"nome", "preco", "quantidade"} (sem código)."""
    # Use ler_texto, ler_decimal e ler_inteiro (quantidade mínima 0).
    pass  # TODO Time 2


# ---------------------------------------------------------------------------
# Testes do próprio time (rode: python coleta.py e digite valores errados de propósito)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Teste 1: tente dar Enter sem digitar nada.")
    print("ler_texto ->", ler_texto("Digite um nome: "))

    print("Teste 2: tente digitar 'abc' e depois '0'.")
    print("ler_inteiro ->", ler_inteiro("Digite um inteiro >= 1: ", 1))

    print("Teste 3: tente digitar 'x' e depois '4,50'.")
    print("ler_decimal ->", ler_decimal("Digite um valor: "))

    print("Teste 4: tente digitar '9'.")
    print("ler_opcao ->", ler_opcao("Escolha 0, 1 ou 2: ", ["0", "1", "2"]))

    print("perguntar_sim_nao ->", perguntar_sim_nao("Está funcionando?"))
    print("ler_dados_produto ->", ler_dados_produto())
