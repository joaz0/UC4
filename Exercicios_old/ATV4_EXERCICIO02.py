ValorProduto = float(input("Informe o valor do produto: R$"))

if ValorProduto >= 100:
    ValorFinal = ValorProduto * 0.90
    print(f"o valor do produto com desconto é: ", ValorFinal)
else:
    print("produto sem desconto.")