class Aluno:
    def __init__(self, matricula:int, nome:str, altura:float, peso:float):
        self.matricula = matricula
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.plano = plano
        self.treinos = []

    def calcular_imc(self: (float)):

        return  self.peso / (self.altura ** 2)

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso


class Plano:
    def __init__(self, plano:(str), valor_mensalidade:(float), duracao_meses:(int)):
        self.plano = plano
        self.valor_mensalidade = valor_mensalidade
        self.duracao_meses = duracao_meses

    def reajuste(self, percentual:(float)):
        self.valor_mensalidade = self.valor_mensalidade * (1 + percentual / 100)

plano = Plano("Básico", 150, 12)

plano.reajuste(10)

print(plano.mensalidade)


# class Treino:
#     def __init__(self, treino, nivel, series):
#         self.treino = treino
#         self.nivel = nivel
#         self.series =series
#         pass