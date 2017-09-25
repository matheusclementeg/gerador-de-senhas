import random


def menu():
    print("========================")
    print("     Gerador de Senha    ")
    print("========================")
    print("[1] - Senha Dificil")
    print("[2] - Senha Média ")
    print("[3] - Senha Fácil")
    print("[0] - Sair")
    print(" ")


loop = True
while loop:
    menu()
    res = int(input("Opção: "))
    if res == 1:
        senha = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        tamanho = 16
        pe = "".join(random.sample(senha, tamanho))
        print(pe)
    elif res == 2:
        senha = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
        tamanho = 8
        pe = "".join(random.sample(senha, tamanho))
        print(pe)
    elif res == 3:
        senha = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        tamanho = 8
        pe = "".join(random.sample(senha, tamanho))
        print(pe)
    elif res == 0:
        print("Até mais!")
        loop = False
