class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.agendamentos = []

        def __str__(self):
            return self.nome


class Servicos:
    def __init__(self, nome, preco, duracao_min):
        self.nome = nome
        self.preco = preco
        self.duracao_min = duracao_min
        pass