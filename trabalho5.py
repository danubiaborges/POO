from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, numero, nome, saldo):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo
        self.__listaTransacoes = []

    def setNumero(self):
        return self.__numero

    def setNome(self):
        return self.__nome

    def setSaldo(self):
        return self.__saldo

    def getNumero(self):
        return self.__numero

    def getNome(self):
        return self.__nome

    def getSaldo(self):
        return self.__saldo

    def deposito(self, valor):
        operacao = transacao(valor)
        self.__saldo += valor
        self.__listaTransacoes.append(operacao)

    def retirada(self, valor):
        if(self.__saldo > valor):
            operacao = transacao(valor)
            self.__saldo -= valor
            self.__listaTransacoes.append(operacao)
        else: ("Saldo insuficiente!")

    def getTransacao(self):
        return self.__listaTransacoes

    @abstractmethod
    def ImprimirExtrato(self):
        pass

class Comum(Conta):
    def __init__(self, numero, nome, saldo):
        super().__init__(numero, nome, saldo)
        
class Limite(Conta):
    def __init__(self, numero, nome, saldo, valorLimite):
        super().__init__(numero, nome, saldo)
        self.__valorLimite = valorLimite

    def setValorLimite(self):
        return self.__valorLimite

    def getValorLimite(self):
        return self.__valorLimite

class Poupanca(Conta):
    def __init__(self, numero, nome, saldo, aniversario):
        super().__init__(numero, nome, saldo)
        self.__aniversario = aniversario

    def setAniversario(self):
        return self.__aniversario

    def getAniversario(self):
        return self.__aniversario

class Transacao:
    def __init__(self, data, valor, descricao):
        self.__data = data
        self.__valor = valor
        self.__descricao = ""

    def setData(self):
        return self.__data

    def setValor(self):
        return self.__valor

    def setDescricao(self):
        return self.__descricao

    def getData(self):
        return self.__data

    def getValor(self):
        return self.__valor

    def getDescricao(self):
        return self.__descricao

if __name__ == "__main__":
