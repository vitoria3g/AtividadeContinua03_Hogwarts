#from ac03 import Escola, Casa, Professor, Aluno, Disciplina

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




# Criação da Escola
hogwarts = Escola("Escola de Magia e Bruxaria de Hogwarts")

# Criação das Casas
grifinoria = Casa("Grifinória")
sonserina = Casa("Sonserina")
corvinal = Casa("Corvinal")
lufalufa = Casa("Lufa-Lufa")

# Criação das Disciplinas
herbologia = Disciplina("Herbologia")
transfiguracao = Disciplina("Transfiguracao")
pocoes = Disciplina("Poções")
defesa = Disciplina("Defesa contra as artes das trevas")

# Criação dos Professores
minerva = Professor("Minerva McGonagall", "19351004")
filio = Professor("Fílio Flitwick", "19301017")
pomona = Professor("Pomona Sprout", "19410515")
severo = Professor("Severo Snape", "19600109")

# Criação dos Alunos
draco = Aluno("Draco Malfoy", "19800605", "puro-sangue")
ernesto = Aluno("Ernesto Macmillan", "19800901", "puro-sangue")
hermione = Aluno("Hermione Granger", "19790919", "trouxa")
harry = Aluno("Harry Potter", "19800731", "mestiço")
luna = Aluno("Luna Lovegood", "19810213", "puro-sangue")

# inclui as casas na escola
hogwarts.incluir_casa(grifinoria)
hogwarts.incluir_casa(sonserina)
hogwarts.incluir_casa(corvinal)
hogwarts.incluir_casa(lufalufa)

# definição dos diretores das casas
grifinoria.set_diretor(minerva)
sonserina.set_diretor(severo)
corvinal.set_diretor(filio)
lufalufa.set_diretor(pomona)

# definicao dos monitores das casas
grifinoria.set_monitor(hermione)
sonserina.set_monitor(draco)
corvinal.set_monitor(ernesto)
lufalufa.set_monitor(luna)

# definição das casas dos alunos
draco.set_casa(sonserina)
ernesto.set_casa(corvinal)
hermione.set_casa(grifinoria)
harry.set_casa(grifinoria)
luna.set_casa(lufalufa)

# definicao dos professores das disciplinas
severo.incluir_disciplina(defesa)
severo.incluir_disciplina(transfiguracao)
minerva.incluir_disciplina(herbologia)
filio.incluir_disciplina(transfiguracao)
pomona.incluir_disciplina(pocoes)

# Definição dos alunos que cursam as disciplinas
herbologia.incluir_aluno(harry)
herbologia.incluir_aluno(hermione)
transfiguracao.incluir_aluno(draco)
transfiguracao.incluir_aluno(hermione)
pocoes.incluir_aluno(ernesto)
defesa.incluir_aluno(harry)
defesa.incluir_aluno(draco)
defesa.incluir_aluno(ernesto)
defesa.incluir_aluno(hermione)
defesa.incluir_aluno(luna)

# Inclui triunfos e mau_feitos
harry.incluir_triunfo(3)
harry.incluir_mau_feito(1)
draco.incluir_mau_feito(5)
draco.incluir_triunfo(1)
draco.incluir_mau_feito(2)
hermione.incluir_triunfo(4)
harry.incluir_triunfo(2)


# REALIZAÇÃO DE TESTES
# Verifica o valor correto dos atributos e retorno de métodos

erros = 0
acertos = 0

try:
    assert hogwarts.nome == 'Escola de Magia e Bruxaria de Hogwarts'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Escola de Magia e Bruxaria de Hogwarts')

try:
    assert len(hogwarts.casas) == 4
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 4')

try:
    assert sonserina.nome == 'Sonserina'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Sonserina')

try:
    assert grifinoria.get_diretor().nome == 'Minerva McGonagall'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Minerva McGonagall')

try:
    assert grifinoria.get_monitor().nome == 'Hermione Granger'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Hermione Granger')

try:
    assert minerva.nome == 'Minerva McGonagall'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Minerva McGonagall')

try:
    assert severo.nascimento == '19600109'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 19600109')

try:
    assert severo.disciplinas[1].nome == 'Transfiguracao'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Transfiguracao')

try:
    assert defesa.nome == 'Defesa contra as artes das trevas'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Defesa contra as artes das trevas')

try:
    assert len(defesa.alunos) == 5
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 5')

try:
    assert defesa.alunos[0].nome == 'Harry Potter'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Harry Potter')

try:
    assert luna.nome == 'Luna Lovegood'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Luna Lovegood')

try:
    assert luna.nascimento == '19810213'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 19810213')

try:
    assert draco.tipo == 'puro-sangue'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: puro-sangue')

try:
    assert draco.get_casa().nome == 'Sonserina'
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: Sonserina')

try:
    assert hermione.get_triunfo() == 4
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 4')

try:
    assert draco.get_triunfo() == 1
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 1')

try:
    assert draco.get_mau_feito() == 7
    print('CORRETO')
    acertos += 1
except AssertionError:
    print('ERRO:')
    print(' Resultado esperado: 7')

print('-'*30)
print('ACERTOS..:', acertos)
print('ERROS....:', 18 - acertos)
print('-'*30)
