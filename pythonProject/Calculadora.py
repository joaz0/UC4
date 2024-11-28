def soma():
    resultado = num1 + num2
    return print(f"O resultado da soma entre {num1} e {num2} é :{resultado}" )


def subtracao():
    resultado = num1 - num2
    return print(f"O resultado da subtração entre {num1} e {num2} é :{resultado}" )


def mutiplicacao():
    resultado = num1 * num2
    return print(f"O resultado da mutiplicação entre {num1} e {num2} é :{resultado}" )


def divisao():
    resultado = num1 / num2
    return print(f"O resultado da divisao entre {num1} e {num2} é :{resultado}" )


def saida():
    return print(f"saida" )


num1 = int(input("Informe um número: "))
num2 = int(input("Informe um número: "))

while True:
    escolha = input("Escolha entre \n 1 - soma \n 2 - subtração \n 3 - mutiplicação \n 4 - divisão \n 5 - todas as alternativas \n 0 - saida :")

    match escolha :
        case "1":
            soma()
        case "2":
            subtracao()
        case "3":
            mutiplicacao()
        case "4":
            divisao()
        case "5":
            soma()
            subtracao()
            mutiplicacao()
            divisao()
        case"0":
            saida()
            break
        case _:
            print("Opção invalida")



