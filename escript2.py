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