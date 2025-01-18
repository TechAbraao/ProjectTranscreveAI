from .constructor.painel_option_ct import painel_option_ct
from .constructor.closure_program_ct import closure_program_ct
from .constructor.insert_url_ct import insert_url_ct

def start() -> None:
    while True:
        command = painel_option_ct()
        if command == '1': insert_url_ct()
        if command == '2': closure_program_ct()
        else: print("")