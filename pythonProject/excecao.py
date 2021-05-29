

lista = [1, 10]
try:
    divisao = 10 / 1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
except IndexError:
    print("Erro de Indexação!")
except BaseException as ex:
    print("Erro de base: {}".format(ex))


    