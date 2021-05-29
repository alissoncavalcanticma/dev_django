class Calculadora:
    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2
    def soma(self):
        return self.x + self.y
    def multiplica(self):
        return self.x * self.y
    def subtrai(self):
        return self.x - self.y
    def divide(self):
        return self.x / self.y

c = Calculadora(2, 3)

#print(c.x, c.y)
print(c.soma())
print(c.multiplica())
print(c.subtrai())
print(c.divide())

