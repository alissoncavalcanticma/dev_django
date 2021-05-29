conta_letras = lambda lista: [len(x) for x in lista]

lista = ['EU', 'Biquinho', 'Fabiana']

print(conta_letras(lista))

somar = lambda x, y: x + y

print("Valor da soma com Lambda é: {}".format(somar(5,43)))


#DICIONÁRIO DE FUNÇÕES LAMBDA

calculadora = {
    'soma':         lambda x,y:x+y,
    'multiplica':   lambda x,y:x*y,
    'subtrai':      lambda x,y:x-y,
    'divide':       lambda x,y:x/y
}

print(type(calculadora))

calc = calculadora['soma']
print(calc(10,3))

calc = calculadora['divide']
print(calc(4,2))


valida_numero = {
    'par': lambda a: True if a % 2 == 0 else False,
    'impar': lambda b: True if b % 2 == 0 else False
}
resultado = valida_numero['par'](10)