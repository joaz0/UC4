idade = int(input("Informe qual é sua idade: "))

if idade >= 4 and idade <= 5 :
    print("Você deve estar na pré-escola ")

elif idade >= 6 and idade <= 10 :
    print("Você deve estar no ensino fundamental I")

elif idade >= 11 and idade <= 14 :
    print("Você deve estar no ensino fundamental II")

elif idade >= 15 and idade <= 17 :
    print("Você deve estar no ensino medio ")

elif idade >= 18 :
    print("Você deve estar na educação superior ou fora da educação regular ")

else :
    print("Você não precisa estudar ")
