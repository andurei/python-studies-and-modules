

# Classes


class Eletronico:
    def __init__(self):
        self.ligado = False    
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def esta_ligado(self):
        return self.ligado
                            
class Tv(Eletronico):
    def __init__(self):
        Eletronico.__init__(self)
        self.volume = 0
    def aumentarVolume(self):
        if (self.volume < 100):
            self.volume += 1 
    def diminuirVolume(self):
        if (self.volume > 0):
           self.volume -= 1 
    def obterVolume(self):
        return self.volume
           
    def pressHoldPlus(self, number):
        for i in range(number):
            if (self.volume < 100):
                self.aumentarVolume()
    def pressHoldMinus(self, number):
        for i in range(number):
            if (self.volume > 0):
                self.diminuirVolume()    
tv = Tv()
print('Tv esta ligada?', tv.esta_ligado())
tv.ligar()
print('Tv esta ligada?', tv.esta_ligado())
tv.pressHoldPlus(5)
print('Volume da tv: ', tv.obterVolume())





class Dog():
    def __init__(self,nome, cor): # método construtor
        self.nome = nome
        self.cor = cor
        self.qualquer_coisa = True

    def latir(self):
        print('auauauauauau')
    
#catioro = Dog('Rex', 'preto')

#print(catioro.cor) # atributos não precisam de parênteses no final

#catioro.latir() # métodos precisam de parênteses no final

class SuperClass():
    def __init__(self, coisa3, coisa4):
        self.coisa3 = coisa3
        self.coisa4 = coisa4
        self.coisa5 = True
        
class MyClass(SuperClass):
    def __init__(self, coisa1, coisa2, coisa3, coisa4):
        SuperClass.__init__(self, coisa3,coisa4)
        self.coisa1 = coisa1
        self.coisa2 = coisa2
                
#classe = MyClass('coisa1', 'coisa1', 'coisa2', 'coisa2')

# print(classe.coisa5)


class Funcionario():
        
    def __init__(self, nome, cargo, valor_hora):
        self.nome =nome
        self.cargo = cargo
        self.valor_hora = valor_hora
        self.__horas_trabalhadas = 0
        self.__salario = 0
    
    @property
    
    def salario(self):
        return self.__salario
    
    def registra_hora(self):
        self.horas_trabalhadas += 1
    def CalculaSalario(self):
        self.__salario = self.__horas_trabalhadas + self.valor_hora



class Mamifero():
    def __init__(self, cor, genero, qtd_patas):
        self.cor = cor
        self.genero = genero
        self.qut_patas = qtd_patas
    
    def amamentar(self):
        if (self.genero.lower()[0] == 'm'):
            print('Machos não amamentam')
            return 
        print('estou amamentando o meu filhote')

class Cachorro(Mamifero):
    
    def amamentar(self):
        if (self.genero.lower()[0] == 'm'):
            print('machos não amamentam')
            return
        print('Amamentando o filhote') 

rex = Cachorro('Azul', 'masculino', 4)

rex.amamentar()






     
            