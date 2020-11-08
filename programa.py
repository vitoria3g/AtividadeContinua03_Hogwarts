class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.casas = []

    def incluir_casa(self, casa):
        self.casas.append(casa)


class Casa:
    def __init__(self, nome):
        self.nome = nome
        self.__diretor = None
        self.__monitor = None

    def set_diretor(self, diretor):
        self.__diretor = diretor

    def set_monitor(self, monitor):
        self.__monitor = monitor

    def get_diretor(self):
        return self.__diretor

    def get_monitor(self):
        return self.__monitor


class Professor:
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento
        self.disciplinas = []

    def incluir_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)


class Aluno:
    def __init__(self, nome, nascimento, tipo):
        self.nome = nome
        self.nascimento = nascimento
        self.tipo = tipo
        self.__casa = None
        self.__triunfos = 0
        self.__mau_feitos = 0

    def set_casa(self, casa):
        self.__casa = casa

    def get_casa(self):
        return self.__casa

    def incluir_triunfo(self, triunfo):
        self.__triunfos = self.__triunfos + triunfo

    def incluir_mau_feito(self, mau_feito):
        self.__mau_feitos = self.__mau_feitos + mau_feito

    def get_triunfo(self):
        return self.__triunfos

    def get_mau_feito(self):
        return self.__mau_feitos


class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def incluir_aluno(self, aluno):
        self.alunos.append(aluno)
