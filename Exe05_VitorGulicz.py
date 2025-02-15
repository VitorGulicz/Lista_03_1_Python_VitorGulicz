preco=float(input("Digite o preço do produto: "))

if preco<=100:
    precoMargem=preco+(preco*0.45)
    print("Preço do produto com margem bruta R$: {} - Vitor Gulicz".format(precoMargem))
else:
    precoMargem=preco+(preco*0.25)
    print("Preço do produto com margem bruta R$: {} - Vitor Gulicz".format(precoMargem))