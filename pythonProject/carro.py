class Carro:
    def __init__(self):
        self.status = False
    def ligadesliga(self):
        if self.status == False:
            self.status == True
        else:
            self.status == False


from classe2 import Calculadora
calc = Calculadora()
print(calc.subtrai(10,4))
print(calc.soma(3,7))