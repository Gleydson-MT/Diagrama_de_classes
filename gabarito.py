class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def aplicar_desconto(self, pct):
        self.preco = self.preco - self.preco * pct / 100 # tira pct por cento

teclado = Produto("Teclado", 100)
teclado.aplicar_desconto(10)
print("Ex4", teclado.preco) #

class ContaBancaria:
    def __init__(self):
        self.saldo = 0
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print("SALDO INSULFICIENTE")

conta = ContaBancaria()
conta.depositar(50)
conta.sacar(20)
print("Exs",conta.saldo) #


class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []
    def adicionar_nota(self, n):
        self.notas.append(n)
    def medias(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len (self.notas)

bia = Aluno("Bia")
bia.adicionar_nota(8)
bia.adicionar_nota(6)
print("Ex6:", bia.medias())