# Faça uma função que recebe um parâmetro de número e retorna se esse número é positivo, negativo ou neutro.

numero = int(input("Digite um número: "))

def tipoNum(numero):
    if numero > 0:
        return f"O número {numero} é positivo"
    elif numero < 0:
        return f"O número {numero} é negativo"
    elif numero == 0:
        return f"O número {numero} é neutro"
    else:
        return "Número inválido!"

print(tipoNum(numero))