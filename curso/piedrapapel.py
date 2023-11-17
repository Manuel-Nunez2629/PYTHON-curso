import random

def play():
    user = input("Elige \n'R' para piedra\n'T'para tijeras\n'P'para papel: ")
    computer = random.choice (['r','t','p'])
    print("Cpu ha elegido: "+computer)

    if user == computer:
        print('Elegiste: '+user+' \nY tu oponente: '+computer+ '\nEmpate')
    
    if sigana(user,computer):
       print('Elegiste: '+user+' \nY tu oponente: '+computer+ '\nGanaste')
    if sigana(computer,user):
        print('Elegiste: '+user+' \nY tu oponente: '+computer+ '\nPerdiste')

def sigana (jugador,oponente):
    if jugador=='r'and oponente == 't' or jugador =='t' and oponente =='p'  or jugador == 'p' and oponente == 'r':
        return True

print(play()) 