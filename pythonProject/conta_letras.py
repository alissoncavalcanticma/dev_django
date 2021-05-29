def conta_letras(lista):
    contador = []
    for x in lista:
        contador.append(len(x))
    return contador

lista = ['Alisson', 'Fabiana']
print(conta_letras(lista))