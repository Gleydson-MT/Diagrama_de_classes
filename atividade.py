class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual:float):
         return self.preco * (1+ percentual / 100)

    def reduzir_preco(self, percentual):
        self.preco = self.preco - (1+ percentual /100)


class ContaBancaria:
    def __init__(self, titular):
        self.titular =titular
        self.__saldo = 0.0
# __saldo, serve para se referir a conta que esta sendo ultilizada na quele momento, para dificultar o acesso por fora da classe.
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print (f"Deposito de R$ {valor:.2f}, realizado com sucesso.")
        else:
            print("Valor invalido para deposito.")

                # Essa linha foi a que mais me confundiu, seria interresante dar uma olhada em video para poder ter mais intimidade com o código, ficar sem saber oque está acontecendo me IRRITA.................!!!!!!!
    def sacar(self, valor):
        if 0 > valor <= self.__saldo:
            # Essa linha diz que se o valor de saque for maior que 0 e menor ou igual ao saldo, então fara o que a segunda linha de codigo diz.
            self.__saldo -= valor
            # Aqui a linha diz que caso a condição da primeira linha seja cumprida, então o valor de saque séra débitado da conta.
            print(f"Saldo de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insulficiente ou valor inválido.")
            # Caso não séra exibida uma mensagem de erro como à que esta em cima.

    def ver_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

class Aluno:
    def __init__(self, nome, nota: float):
        self.nome = nome
        self.nota = nota
        self.medias = []

    def adicionar_nota(self, n1: float, n2: float, n3: float, n4: float):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        soma_das_notas = (n1 + n2 + n3+ n4)

    # def media(self):
    #     # Minha dúvida aqui seria se devo por "(self, media)", ou se apenas deixo como está e sigo para a divisão.



