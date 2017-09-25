# -*- coding: utf-8 -*-
"""tkinter

Exemplo de utilização do Tkinter.
OBS: Não está sendo utilizada orientação a objeto (classes).
"""
from tkinter import *
import random


def gerar_senha():
    """Gerar senha.

    Função responsável por gerar uma senha aleatória com base
    na escolha que o usuário fizer na interface gráfica.
    """
    caracteres = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    valor = escolhaVar.get()
    if valor == 'Fácil':
        tamanho = 6
        senha = ''.join(random.sample(caracteres, tamanho))
        lb['text'] = '%s' % senha
    elif valor == 'Médio':
        tamanho = 12
        senha = ''.join(random.sample(caracteres, tamanho))
        lb['text'] = '%s' % senha
    else:
        tamanho = 18
        senha = ''.join(random.sample(caracteres, tamanho))
        lb['text'] = '%s' % senha


def sair():
    """Sair.

    Função fecha a janela da aplicação.
    """
    janela.quit()


# Janela principal do nosso programa
janela = Tk()

# Geometria da janela.
janela.geometry('400x200+200+200')

# Titulo da janela principal.
janela.title('Gerador de senha')

# A escolha feita na interface gráfica fica armazenada nesta variável.
escolhaVar = StringVar()
# Opção que será padrão quando a interface iniciar.
escolhaVar.set('Fácil')
# Escolhas que estão disponíveis.
escolhas = ('Fácil', 'Médio', 'Dificil')

# Criando os widgets.
# widget com as opções.
choicebox = OptionMenu(janela, escolhaVar, *escolhas)
# Botão que gera a senha.
bt1 = Button(janela, width=20, text='Gerar', command=gerar_senha)
# Botão para sair da interface.
bt2 = Button(janela, width=20, text='Sair', command=sair)
# Label que exibe a senha gerada.
lb = Label(janela, text='Sua senha será exibida aqui.')

# Colocando o widget na tela.
# Como estamos utilizando o pack os widget ficam na posição em que são lançados.
# Ele equivale ao boxlayout de outras interfaces gráficas.
choicebox.pack()
bt1.pack()
lb.pack()
bt2.pack()

# Mantem a janela principal aberta.
janela.mainloop()

