class CadastroAlunos:
    """Gerencia o cadastro de alunos em memória."""

    def __init__(self):
        self._alunos = []

    def adicionar(self, nome, matricula):
        nome = str(nome).strip()
        matricula = str(matricula).strip()

        if not nome:
            raise ValueError("o nome não pode ficar vazio")
        if not any(letra.isalpha() for letra in nome):
            raise ValueError("o nome deve conter pelo menos uma letra")
        if not matricula:
            raise ValueError("a matrícula não pode ficar vazia")
        if any(a["matricula"] == matricula for a in self._alunos):
            raise ValueError("já existe um aluno com essa matrícula")

        self._alunos.append({"nome": nome, "matricula": matricula})

    def listar(self):
        return [aluno.copy() for aluno in self._alunos]

    def remover(self, matricula):
        matricula = str(matricula).strip()
        for aluno in self._alunos:
            if aluno["matricula"] == matricula:
                self._alunos.remove(aluno)
                return True
        return False
