qnthrs = float(input("Informe quanto você ganha por hora: "))
hrstrab = float(input("Informe quantas horas você trabalha: "))

salariobruto = qnthrs * hrstrab

inss = salariobruto * 0.8
sindicato = salariobruto * 0.5
IR = salariobruto * 0.11

salarioliquido = salariobruto - (salariobruto * 0.24)

print(f" + salario bruto: R${salariobruto} \n -IR (11%): R${IR} \n -INSS (8%): R${inss} \n - sindicato (5%) : R${sindicato} \n = salário liquido : R${salarioliquido}")
