class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.agendamentos = []

        def __str__(self):
            return self.nome


class Servicos:
    def __init__(self, nome, duracao_min, preco):
        self.nome = nome
        self.duracao_min = duracao_min
        self.preco = preco

    def __str__(self):
        return self.nome

class Agendamento:
    def __init__(self, cliente, servico, data_hora):
        self.nome = cliente
        self.servico = servico
        self.data_hora = data_hora


        cliente.agendamentos.append(self)
