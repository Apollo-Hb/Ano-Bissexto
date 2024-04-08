"""
    Criar uma aplicação para indentificar se um ano é bissexto.
-   vai solicitar para o usuario informar o ano.
-   retornar se o abo é bissexto ou não.

-   para ser bissexto tem que ser:
-   MULTIPLO DE 4
-   não pode ser divisivel por 100 a nao ser que seja por 400.
"""

ano = int(input("Informe o ano"))

if ano % 4==0 or ano % 400==0:
    print("esse ano é bissexto")
    
else:
    print("esse ano não é bissexto")



