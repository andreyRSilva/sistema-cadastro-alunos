# Planejamento de Gerência de Configuração de Software

## Itens de configuração
- `main.py`: interface de terminal.
- `cadastro.py`: regras do cadastro.
- `tests/`: testes automatizados.
- `README.md`: instruções e descrição.
- `docs/`: documentação do projeto.
- `.gitignore` e `requirements.txt`: configuração do ambiente.

## Nomeação
- Novas funcionalidades: `feature/nome-curto`
- Correções: `fix/nome-curto`
- Documentação: `docs/nome-curto`
- Testes: `test/nome-curto`

## Commits
Usar `feat:`, `fix:`, `docs:`, `test:` e `refactor:` seguido de uma descrição objetiva.

## Branching
- `main`: versão estável.
- Cada tarefa é feita em branch separada.
- Integrar por Pull Request, com revisão de outro integrante.
- Não enviar diretamente para `main`.

## Versionamento
Formato `MAJOR.MINOR.PATCH`. Criar `v1.0.0` para a primeira versão estável e `v2.0.0` após integrar e validar melhorias relevantes.

## Backup e recuperação
O repositório remoto no GitHub e as cópias locais permitem recuperar o histórico. Usar `git clone`, `git pull`, `git log` e tags para recuperar o estado necessário. Manter também uma cópia independente do projeto periodicamente.

## Resolução de conflitos
Ao ocorrer conflito, abrir os arquivos indicados pelo Git, comparar os trechos, decidir com o grupo qual conteúdo deve permanecer, remover marcadores, testar e registrar a resolução em commit.

## Participação da equipe

O projeto foi dividido entre quatro integrantes:

- Andrey: desenvolvimento do menu principal.
- Pietro: cadastro e validação.
- Fabrício: busca e testes.
- Gustavo: documentação e gerenciamento de configuração.

Todos os integrantes utilizam branches individuais,
commits padronizados e pull requests para integrar alterações.
