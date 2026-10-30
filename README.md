# Sistema de Cadastro de Alunos

Projeto acadêmico para praticar Gerência de Configuração de Software (GCS) com Git e GitHub.

## Funcionalidades
- Cadastrar alunos
- Listar alunos cadastrados
- Validar nomes e matrículas
- Remover aluno por matrícula

## Requisitos
- Python 3.10 ou superior

## Como executar
```bash
python main.py
```

## Como executar os testes
```bash
python -m unittest discover -s tests -v
```

## Fluxo de colaboração
- `main`: versão estável.
- `feature/*`: novas funcionalidades.
- `fix/*`: correções.
- Toda alteração deve passar por Pull Request e revisão antes do merge em `main`.

## Padrão de commits
- `feat: ...` nova funcionalidade
- `fix: ...` correção
- `docs: ...` documentação
- `test: ...` testes
- `refactor: ...` reorganização interna

## Versionamento
Usar `MAJOR.MINOR.PATCH`, por exemplo `v1.0.0`, `v1.1.0` e `v2.0.0`.

## Integrantes
O grupo é composto por cinco integrantes. Preencher os nomes reais no relatório e no GitHub. A divisão de tarefas está em `docs/divisao-integrantes.md`.
