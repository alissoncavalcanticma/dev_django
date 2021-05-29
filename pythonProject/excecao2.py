class Error(Exception):
    pass
class numeroError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input("Digite um número de 0 a 10: "))
        print("Nota digitada: {}".format(x))
        if x > 10:
            raise numeroError("Numero não pode ser maior que 10!")
        elif x < 0:
            raise numeroError("Numero não pode ser menor que 0!")
        break
    except ValueError as v:
        print(v)
    except numeroError as num:
        print(num)