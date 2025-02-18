#No comercio o conceito de margem bruta é uma % que é aplicada a preço de custo para se obter o preço de venda. Uma loja tem como politica comercial de aplicar uma margem bruta 
# de 45% quando o preço de custo é menor ou igual a 100 reais se o produto custa mais que isso a margem bruta e de 35%	
#Escreva um programa que leia a margem de custo de um produto e mostre qual é seu preço de venda com duas casas decimais

preco=float(input("Digite o preço do produto: "))

if preco<=100:
    precoMargem=preco+(preco*0.45)
    print("Preço do produto com margem bruta de 45% R$: {} - Vitor Gulicz".format(precoMargem))
else:
    precoMargem=preco+(preco*0.35)
    print("Preço do produto com margem bruta de 35% R$: {} - Vitor Gulicz".format(precoMargem))