from abc import ABC, abstractmethod

class EmpDomestica(ABC):

    # construtor
    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def getNome(self):
        return self.__nome
    
    def getTelefone(self):
        return self.__telefone

    def setNome(self, nome):
        self.__nome = nome

    def setTelefone(self, telefone):
        self.__telefone = telefone

    @abstractmethod
    def getSalario(self):
        pass

class Horista(EmpDomestica):

    # construtor
    def __init__(self, nome, telefone, horasTrabalhadas, valorHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__valorHora = valorHora

    def getHorasTrabalhadas(self):
        return self.__horasTrabalhadas

    def getValorHora(self):
        return self.__valorHora

    def getSalario(self):
        return self.__valorHora * self.__horasTrabalhadas

class Diarista(EmpDomestica):

    # construtor
    def __init__(self, nome, telefone, diasTrabalhados, valorDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__valorDia = valorDia

    def getDiasTrabalhados(self):
        return self.__diasTrabalhados

    def getValorDia(self):
        return self.__valorDia

    def getSalario(self):
        return self.__valorDia * self.__diasTrabalhados

class Mensalista(EmpDomestica):

    #construtor
    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    def getValorMensal(self):
        return self.__valorMensal

    def getSalario(self):
        return self.__valorMensal

empregada1 = Horista('Ciclana', '98822-3321', 160, 12)
empregada2 = Diarista('Fulana', '99816-3154', 20, 65)
empregada3 = Mensalista('Beltrana', '98742-3162', 1200)
empregadas = [empregada1, empregada2, empregada3]

print('\nO valor de cada empregada é de: ')
menor = empregada1.getSalario()
for elemento in empregadas:
    print(elemento.getSalario())
    if(elemento.getSalario() < menor):
        menor = elemento.getSalario()
        nome = elemento.getSalario()
        telefone = elemento.getTelefone()

print()
print('A melhor opção financeira para a república será a:')
print('Mensalista: {} \nTelefone: {} \nValor Mensal: {}'.format(nome, telefone, menor))
print()