num = int(input("Informe um número"))

if num > 0 :
    for i in range(1,num+1,2):
        print(f"os numero impares de 1 ate {num} é {i}")

else:
    print("informe um numero inteiro e positivo")