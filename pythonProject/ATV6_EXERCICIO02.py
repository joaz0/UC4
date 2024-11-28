num = int(input("informe um numero inteiro: "))
soma = 0

if num > 0:

    for i in range(1,num+1):
        soma = soma + i
        print(f"As somas de {i} até {num} é {soma}")

else:
    print("informe um numero inteiro e positivo")