salario = float(input("Informe seu salário: R$"))

if salario < 1901 :
    print("Isento de imposto de renda.")

elif salario <= 2800:
    salario = salario * 0.075
    print("o valor do seu imposto de renda é", salario)

elif salario <= 3700 :
    salario = salario * 0.15
    print("o valor do seu imposto de renda é", salario)

else:
    salario = salario * 0.225
    print("o valor do seu imposto de renda é", salario)