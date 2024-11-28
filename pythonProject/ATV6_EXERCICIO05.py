num = int(input("informe um numero inteiro: "))
fatorial = 1

if num >= 0 :
    for i in range(num,0,-1):
        fatorial = fatorial * i

    print(f"o fatorial de {num} é {fatorial} ")

else:
    print("Não existe fatorial de numeros negativos")