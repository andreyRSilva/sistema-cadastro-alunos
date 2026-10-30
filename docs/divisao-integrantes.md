# Divisão das tarefas — 5 integrantes

Substituam Integrante 1–5 pelos nomes reais. Cada pessoa deve usar sua própria conta GitHub e fazer contribuições reais no repositório compartilhado.

## Integrante 1 — Desenvolvedor principal e responsável pelo repositório
- Criar o repositório no GitHub e convidar os outros quatro integrantes.
- Enviar a estrutura inicial do projeto.
- Conferir o README e garantir que o programa inicia com `python main.py`.
- Trabalhar em `feature/menu-principal` e realizar uma melhoria real no menu.
- Commit sugerido: `feat: organizar menu principal`.

## Integrante 2 — Cadastro e validação
- Trabalhar em `feature/validacao-cadastro`.
- Melhorar as validações em `cadastro.py` (por exemplo, impedir nomes formados apenas por números).
- Criar ou atualizar testes para a validação.
- Abrir Pull Request para `main`.
- Commit sugerido: `feat: validar nome do aluno`.

## Integrante 3 — Busca e listagem
- Trabalhar em `feature/busca-alunos`.
- Implementar uma busca por matrícula ou uma melhoria na listagem.
- Criar testes para a funcionalidade.
- Abrir Pull Request para `main`.
- Commit sugerido: `feat: buscar aluno por matricula`.

## Integrante 4 — Testes e qualidade
- Trabalhar em `test/melhorar-cobertura`.
- Conferir os testes existentes e acrescentar casos para cadastro, duplicidade, remoção e entradas inválidas.
- Executar `python -m unittest discover -s tests -v` e registrar o resultado.
- Abrir Pull Request para `main`.
- Commit sugerido: `test: ampliar testes do cadastro`.

## Integrante 5 — Gestor de configuração e documentação
- Trabalhar em `docs/planejamento-gcs`.
- Conferir `docs/planejamento-gcs.md`, `README.md`, convenção de commits e política de branching.
- Coordenar a simulação de conflito e registrar como foi resolvido.
- Revisar os Pull Requests dos colegas e conferir o histórico.
- Depois de todas as melhorias integradas e testadas, coordenar a criação das tags `v1.0.0` e `v2.0.0`.
- Commit sugerido: `docs: documentar politica de configuracao`.

## Regras para todos
1. Cada integrante deve trabalhar em sua própria branch, criada a partir da `main` atualizada.
2. Cada pessoa deve fazer pelo menos um commit identificável usando sua própria conta GitHub.
3. Cada Pull Request deve ser revisado por outro integrante antes do merge.
4. Não fazer alterações diretamente na `main`.
5. Não criar tags de versões antes de integrar e testar a versão correspondente.
6. Os nomes de branch e commits acima são sugestões; registrem no relatório o que realmente foi feito.
