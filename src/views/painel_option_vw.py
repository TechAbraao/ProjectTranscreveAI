import os



def introduction_interface():
    # os.system("cls||clear")
    message = '''
    === Transcreve.Ai ===

    [1] URL do Youtube
    [2] Encerrar programa

    =====================
'''
    print(message)
    command = input(" * Opção: ")

    return command


