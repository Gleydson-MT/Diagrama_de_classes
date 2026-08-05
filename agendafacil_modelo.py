class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.agendamentos = []

    def __str__(self):
        return self.nome


class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return self.nome

class Agendamento:
    def __init__(self, cliente, servico, data_hora):
        self.cliente = cliente
        self.servico = servico
        self.data_hora = data_hora

    def resumo(self):
        return (f"{self.data_hora} | {self.cliente} | "
                f"{self.servico.nome} | R$ {self.servico.preco:.2f}")

ana = Cliente("Ana", "85 99999-9999")
corte = Servico("Corte", 35.00)
ag = Agendamento(ana, corte, "12/08 09:00")
print("Ex10:", ag.resumo())
