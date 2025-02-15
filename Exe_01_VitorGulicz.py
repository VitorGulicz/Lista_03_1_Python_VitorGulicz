#Escreva um programa que forneça o tipo de aplicação financeira adequado a um investidor a partir de dois dados fornecidos:O grau de aceitação de risco. E o valor a ser investido.
#O grau de aceitação de risco deve ser lido no teclado na forma bx para baixo ou al para alto se for fornecido algo diferente disso o programa deve mostrar uma mensagem  
# informando que foi fornecido o dado invalido.Para o valor deve ser um numero real

gar=str(input("Qual o grau de risco de aceitação de risco? (bx para baixo e al para alto): "))
vlr=float(input("Digite o valor a ser investido: "))
if "bx" in gar.lower() and vlr<1000.00:
    print("Invista em poupança - Vitor Gulicz")
elif"bx" in gar.lower() and vlr>=1000.00:
        print("Invista em Renda fixa - Vitor Gulicz")
        #Investimento alto
elif "al" in gar.lower() and vlr<1000.00:
            print("Invista em bitcoin - Vitor Gulicz")
elif "al" in gar.lower() and vlr>=1000.00:
                print("Invista em ações - Vitor Gulicz")
else:
                print("Dados fornecido errado - Vitor Gulicz")