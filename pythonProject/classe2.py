class Calculadora:
    def __init__(self):
        pass
    def soma(self, x, y):
        return x + y
    def multiplica(self, x, y):
        return x * y
    def subtrai(self, x, y):
        return x - y
    def divide(self, x, y):
        return x / y

c = Calculadora()


if __name__ == '__main__':
    #print(c.x, c.y)
    print(c.soma(2,3))
    print(c.multiplica(2,3))
    print(c.subtrai(2,3))
    print(c.divide(2,3))
