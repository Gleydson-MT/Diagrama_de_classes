class Aluno:
    def __init__(self, matricula:(int), nome:(str), altura:(float), peso:(float)):
        self.matricula = matricula
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def calcular_imc(self: (float)):

        return  self.peso / (self.altura ** 2)

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso


aluno = Aluno(1001, "Thiago", 1.75, 80.0)


class PlanoAssinatura:
    def __init__(self, plano, mensalidade, meses):
        self.plano = plano
        self.mensalidade = mensalidade
        self.meses = meses

    def reajuste(self, percentual:(float)):
        self.percentual = percentual
        return self.mensalidade * self.percentual


# class Treino:
#     def __init__(self, treino, nivel, series):
#         self.treino = treino
#         self.nivel = nivel
#         self.series =series
#         pass