lado1 = float(print("informe o valor do lado: "))
lado2 = float(print("informe o valor do lado: "))
lado3 = float(print("informe o valor do lado: "))

if lado1 + lado2 < lado3 :
    print("seu triangulo é : não é um triangulo")

elif lado1 == lado2 == lado3 :
    print("seu triangulo é : equilátero")

elif (lado1 == lado2) or lado1 == lado3 or lado2 == lado3 :
    print("seu triangulo é : isósceles")

else:
    print("seu triangulo é : escaleno")
