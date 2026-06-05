import os

def limpar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def cor_terminal(color):
    os.system(f'color {color}')