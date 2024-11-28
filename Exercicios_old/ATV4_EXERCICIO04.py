salario = float(input("informe seu salário: R$"))

if salario < 1500 :
    salario = salario * 0.80

else:
    salario = salario * 0.90

print("seu salario com aumento é: R$", salario)