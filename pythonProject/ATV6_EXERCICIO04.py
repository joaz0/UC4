num = int(input("informe um número"))

if num > 0 :
    for i in range (1,11):
        tabuada = i * num
        print(f"a tabuada de {num} é {num} * {i} = {tabuada}")

else:
    print("informe um numero inteiro e positivo")