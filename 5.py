def ficha(nome='zé', gols=0):
    print('O jogador', nome, "marcou", gols ,"gols")

jogador = input('Digite o nome do jogador: ')
gols = int(input('Digite a quantidade de gols marcados: '))

ficha(jogador, gols)
