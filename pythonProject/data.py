from datetime import date, time, datetime, timedelta

def usandoDate():
    hoje = date.today()
    #print("Hoje é: {}".format(hoje.strftime('%d/%m/%Y')))
    #print("Hoje é: {}".format(hoje.strftime('%A, %B de %Y')))
    return hoje

def usandoTime():
    tempo = time(hour=15, minute=30, second=30)
    print(tempo)

def usandoDatetime():
    return datetime.now()


if __name__ == "__main__":
    usandoDate()
    usandoTime()
    dtime = usandoDatetime()
    print(dtime.strftime('%d/%m/%Y %H:%M:%S'))
    print(dtime.day)
    print(dtime.month)
    print(dtime.year)
    print(dtime.weekday())

    tupla = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    print(tupla[dtime.weekday()])

    agora = usandoDatetime()
    idade = agora - timedelta()
