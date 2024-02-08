voto = input('digite sua idade')

def Voto(idade):
    if idade < 16:
        print("Nao pode")
    elif idade >= 16 and idade < 18:
        print("voto opcional")
    elif idade >= 18 and idade < 70:
        print("Obrigatorio")
    else:
        print("opcional")

Voto(int(voto))