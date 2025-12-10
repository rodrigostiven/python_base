
"""Hello World Multi Linguas

Depedendo da lingua configurada no ambiente
o programa exibe a mensagem correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Rodrigo Stiven"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "env_US")[:5]

print(current_language)

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"

print(msg)