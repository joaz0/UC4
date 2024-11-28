nota1 = float(input("informe uma nota: "))
nota2 = float(input("informe uma nota: "))
nota3 = float(input("informe uma nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 :
    print("Aprovado")

elif media > 5 :
    print("Recuperação")

else:
    print("Reprovado")

