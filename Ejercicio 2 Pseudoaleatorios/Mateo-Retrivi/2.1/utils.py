from os import system, name


def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
