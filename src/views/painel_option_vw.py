import os
import threading


def introduction_interface():
    # timer = threading.Timer(5, lambda: os.system("cls||clear"))
    # timer.start()
    message = '''
    === Transcreve.Ai ===

    [1] URL do Youtube
    [2] Encerrar programa

    =====================
'''
    print(message)
    command = input(" * Opção: ")

    return command


