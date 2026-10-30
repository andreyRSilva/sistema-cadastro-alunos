# Roteiro prático de Git e GitHub

## 1. Criar o repositório
Uma pessoa cria no GitHub um repositório chamado `sistema-cadastro-alunos`, marca para incluir README e convida os outros três como colaboradores. Depois, substituam o README remoto pelos arquivos deste projeto ou façam upload dos arquivos.

## 2. Cada integrante clona o repositório
```bash
git clone URL_DO_REPOSITORIO
cd sistema-cadastro-alunos
git config --global user.name "Seu Nome"
git config --global user.email "SEU_EMAIL"
```

## 3. Criar branch e enviar alteração
Exemplo para cada pessoa (usar nomes de branch diferentes):
```bash
git switch main
git pull origin main
git switch -c feature/minha-tarefa
# editar arquivo e salvar
git status
git add arquivo_alterado.py
git commit -m "feat: descrever minha alteracao"
git push -u origin feature/minha-tarefa
```
No GitHub, abrir Pull requests > New pull request, escolher `main` como destino e sua branch como origem. Solicitar revisão de outro integrante e fazer merge após aprovação.

## 4. Sincronizar após um merge
```bash
git switch main
git pull origin main
```

## 5. Simular conflito intencional
Faça esta atividade em duas branches diferentes, ambas criadas a partir do mesmo commit da `main`. Não faça isso na branch principal.

1. Na branch `main`, crie `docs/mensagem-conflito.txt` com uma única linha:
   `Mensagem inicial do projeto.`
   Faça commit e envie para `main` antes de criar as duas branches.
2. Integrante A:
```bash
git switch main
git pull origin main
git switch -c demo/conflito-a
```
Altere a única linha para `Mensagem da equipe de cadastro.` e faça commit.
3. Integrante B, em sua cópia local, antes de a branch A ser integrada:
```bash
git switch main
git pull origin main
git switch -c demo/conflito-b
```
Altere a mesma linha para `Mensagem da equipe de listagem.` e faça commit.
4. Envie as duas branches para o GitHub.
5. Para provocar o conflito local, na branch A:
```bash
git switch demo/conflito-a
git merge demo/conflito-b
```
Se a branch B não existir localmente na máquina de A, busque-a primeiro:
```bash
git fetch origin
git merge origin/demo/conflito-b
```
6. O Git mostrará marcadores `<<<<<<<`, `=======` e `>>>>>>>` no arquivo. Edite para combinar as mensagens, por exemplo:
   `Mensagem do projeto: cadastro e listagem disponíveis.`
7. Remova os marcadores, salve e execute:
```bash
git add docs/mensagem-conflito.txt
git commit -m "fix: resolver conflito de mensagem"
git push origin demo/conflito-a
```
8. Abra Pull Request de `demo/conflito-a` para `main`, peça revisão e faça merge. Registre prints antes e depois da resolução.

Se o GitHub bloquear o merge do Pull Request por conflito, resolvam localmente conforme acima e enviem a branch atualizada.

## 6. Tags
Só criar tags depois de confirmar que a versão correspondente foi integrada e testada:
```bash
git switch main
git pull origin main
python -m unittest discover -s tests -v
git tag -a v1.0.0 -m "Versao 1.0.0 - primeira versao validada"
git push origin v1.0.0
```
Após integrar melhorias e testar novamente:
```bash
git switch main
git pull origin main
python -m unittest discover -s tests -v
git tag -a v2.0.0 -m "Versao 2.0.0 - melhorias integradas"
git push origin v2.0.0
```

## 7. Evidências
Tirar prints reais de: página do repositório, arquivos, branches, commits, Pull Requests, merge concluído, conflito antes/depois, tags e colaboradores.
