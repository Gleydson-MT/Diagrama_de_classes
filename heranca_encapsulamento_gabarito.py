# Parte A = Encapsulamento

class Servico:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo):
        if novo > 0:
            self.__preco = novo
        else:
            print(" Preço inválido: precisa ser maior que zero.")

s = Servico("Corte", 35)
s.set_preco(-10)
print("A:", s.set_preco())
s.set_preco(40)
print("A", s.set_preco())


# PARTE B - HERANÇA

class Pessoa:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Cliente(Pessoa):
    def __init__(self, nome, telefone):
        super().__init__(nome, telefone)
        self.agendamentos = []



class Profisional(Pessoa):
    def __init__(self, nome, telefone, especializacao):
        super().__init__(nome, telefone, especializacao)
        self.especializacao = especializacao

c=Cliente("Ana", "85 99999-9999")
p=Profisional("Bruno", "85 99999-9999", "Cabeleleiro")
print("B:", c.nome, "-", p.nome, "-", p.especializacao)