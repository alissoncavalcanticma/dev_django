def escrever(texto):
    arquivo = open('/home/alisson/Documentos/file.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
    print("Arquivo criado!")
def atualizar(texto):
    arquivo = open('/home/alisson/Documentos/file.txt', 'a')
    arquivo.write(texto + '\n')
    arquivo.close()
    print("Arquivo atualizado com sucesso!")
def ler(file):
    arquivo = open(file, 'r')
    file = arquivo.read()
    print(file)

def ler_linhas(file):
    arquivo = open('/home/alisson/Documentos/file.txt', 'r')
    linhas = arquivo.read()
    linhas = linhas.split('\n')
    return linhas

    for x in linhas:
        notas_aluno = x.split(',')
        for y in notas_aluno:
            notas = []
            notas += notas[y]
            return notas

def copiar(file, diretorio):
    import shutil
    shutil.copy(file, diretorio)

def mover(file, diretorio):
    import shutil
    shutil.move(file, diretorio)

if __name__ == '__main__':
    #ler('file.txt')
    #escrever("Alisson\n")
    #atualizar("Galvão")
    linhas = ler_linhas('/home/alisson/Documentos/file.txt')
    print(linhas)
    notas = linhas[2][1]
    print(notas[0])

    copiar('/home/alisson/Documentos/file.txt', '/home/alisson/Documents/file.txt')
    mover('/home/alisson/Documents/file.txt', '/home/alisson/Documentos/file1.txt')