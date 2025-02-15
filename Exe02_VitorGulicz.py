#Escreva um programa para exibir na tela o nome e a categoria de um lutador o programa deve ler um string para o nome e um numero real para o peso. 
# Conforme o peso ocorrera o enquadramento na categoria
nome=str(input("Digite o nome do lutador: "))
peso=float(input("Digite o peso(kg): "))
print("LUTADOR: {}".format(nome))
print("CATEGORIA: ")
if peso<52:
    print("Invalido - Vitor Gulicz")
elif 52<=peso<65:
    print("Pena - Vitor Gulicz")
elif 65<=peso<72:
    print("Leve - Vitor Gulicz")
elif 72<=peso<79:
    print("Ligeiro - Vitor Gulicz")
elif 79<=peso<86:
    print("Meio Médio - Vitor Gulicz")
elif 86<=peso<90:
    print("Médio - Vitor Gulicz")
elif 90<=peso<100:
    print("Meio pesado - Vitor Gulicz")
elif peso>=100:
    print("Pesado Vitor - Gulicz")
