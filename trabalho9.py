from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome, pontoMensalFunc):
        self.__codigo = codigo
        self.__nome = nome
        self.__pontoMensalFunc = pontoMensalFunc

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc

    def adicionaPonto(self, mes, ano, faltas, atrasos):
        return self.__adicionaPonto

    def lancaFaltas(self, mes, ano, faltas):
        return self.__faltas.append(PontoFunc(mes, ano, faltas))

    def lancaAtrasos(self, mes, ano, atrasos):
        return self.__atrasos.append(PontoFunc(mes, ano, atrasos))

    def imprimeFolha(self, mes, ano):
        return self.__imprimir.append(PontoFunc(mes, ano))

    @abstractmethod
    def calculaSalario(mes, ano):
        pass

    @abstractmethod
    def calculaBonus(mes, ano):
        pass

class Professor(Funcionario):
    def __init__(self, codigo, nome, pontoMensalFunc, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome, pontoMensalFunc)
        self.__titulacao = titulacao
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas

    @property
    def titulacao(self):
        return self.__titulacao

    @property
    def salarioHora(self):
        return self.__salarioHora

    @property
    def nroAulas(self):
        return self.__nroAulas

    def calculaSalario(self, mes, ano):
        return (self.__salarioHora * self.__nroAulas) - (self.__salarioHora * self.__nroFaltas)
        
    def calculaBonus(self, mes, ano):
        return (self.nroAulas * self.salarioHora) * (10/100)

class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, pontoMensalFunc, funcao, salarioMensal):
        super().__init__(codigo, nome, pontoMensalFunc)
        self.__funcao = funcao
        self.__salarioMensal = salarioMensal

    @property
    def funcao(self):
        return self.__funcao

    @property
    def salarioMensal(self):
        return self.__salarioMensal

    def calculaSalario(self, mes, ano):
        return (self.__salarioMensal -(self.__salarioMensal/30) * self.__nroFaltas)

    def calculaBonus(mes, ano):
        self.__salarioMensal - (self.__salarioMensal)

class PontoFunc:
    def __init__(self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos

    @property
    def mes(self):
        return self.__mes

    @property
    def ano(self):
        return self.__ano

    @property
    def nroFaltas(self):
        return self.__nroFaltas

    @property
    def nroAtrasos(self):
        return self.__nroAtrasos

    def lancaFaltas(nroFaltas):
        return nroFaltas

    def lancaAtrasos(nroAtrasos):
        return nroAtrasos

if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()