# Desafio CRUD Compacto 2026 — Cantina da Escola

Sistema de **cadastro, venda e estoque** da cantina da escola, construído pelos alunos em Python
usando **apenas funções e dicionários**, rodando no terminal.

Versão compacta do [Desafio CRUD Completo 2026](https://github.com/Kazenski/site-desafio-crud-completo-2026),
pensada para uma turma de 1º ano do Ensino Médio Técnico que já aprendeu Python até funções e dicionários
(sem `try/except`, sem classes).

O site apresenta o sistema em desenhos simples (o que faz, arquivos, quem precisa de quem, dados,
passo a passo, fluxogramas, situação do produto, roteiro de teste), o contrato de funções de cada time
e o plano de montagem. A pasta `esqueleto/` traz os arquivos `.py` já com nomes, parâmetros e docstrings
para cada time preencher.

## Como funciona a divisão

- **6 times × 6 alunos × 6 funções** — cada aluno é dono de uma função e a apresenta no final.
- Menu único com 7 opções: cadastrar, listar, vender, repor, atualizar, remover, relatório.
- Um só dicionário `sistema` com `produtos`, `vendas` e `caixa`.

| Time | Arquivo | Prefixos | Depende de |
|------|---------|----------|------------|
| 1 · Tela | `interface.py` | `mostrar_` | T4, T5 |
| 2 · Teclado | `coleta.py` | `ler_`, `perguntar_` | T1 |
| 3 · Cadastro | `cadastro.py` | `cadastrar_`, `buscar_`, `registrar_` | — |
| 4 · Cálculos | `calculos.py` | `calcular_`, `formatar_` | — |
| 5 · Estoque | `estoque.py` | `verificar_`, `baixar_`, `repor_` | T3 |
| 6 · Ligar tudo | `atualizacao.py`, `main.py` | `atualizar_`, `remover_`, `fluxo_` | todos |

## Estrutura

```
site-desafio-crud-compacto-2026/
├── index.html          # o site (página única)
├── css/style.css
├── js/main.js          # renderiza os diagramas Mermaid e o zoom
├── img/                # opcional: foto do quadro
├── esqueleto/          # contrato de funções em código, um arquivo por time
│   ├── dados.py        # pronto: dados de exemplo (3 produtos)
│   ├── interface.py    # Time 1 — tela
│   ├── coleta.py       # Time 2 — teclado
│   ├── cadastro.py     # Time 3 — cadastro
│   ├── calculos.py     # Time 4 — cálculos
│   ├── estoque.py      # Time 5 — estoque
│   ├── atualizacao.py  # Time 6 — atualizar e remover
│   └── main.py         # Time 6 — menu pronto, 3 fluxos a preencher
└── README.md
```

## Ver o site localmente

Os diagramas são renderizados pela biblioteca Mermaid carregada via CDN, então basta abrir
`index.html` no navegador. Se o navegador bloquear o módulo JS em `file://`, suba um servidor simples:

```bash
python -m http.server 8000
# abra http://localhost:8000
```

## Publicar no GitHub Pages

No GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch →
Branch: `main` / `(root)` → Save**. Em alguns minutos o site estará em
`https://kazenski.github.io/site-desafio-crud-compacto-2026/`.

## Rodar o esqueleto

```bash
cd esqueleto
python main.py          # menu principal (cadastrar, listar, repor e relatório já funcionam
                        # quando os Times 1 a 5 terminarem; vender/atualizar/remover são do Time 6)
python cadastro.py      # testes isolados do Time 3 (idem para os outros arquivos)
```

Cada arquivo tem um bloco `if __name__ == "__main__":` com testes e os valores esperados,
para o time conferir a própria entrega antes da montagem.
