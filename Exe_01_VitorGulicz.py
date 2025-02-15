gar=str(input("Qual o grau de risco de aceitação de risco? (bx ou al): "))
vlr=float(input("Digite o valor a ser investido: "))
if "bx" in gar and vlr<1000.00:
    print("Invista em poupança")
elif"bx" in gar and vlr>=1000.00:
        print("Invista em Renda fixa")
elif "al" in gar and vlr<1000.00:
            print("Invista em bitcoin")
elif "al" in gar and vlr>=1000.00:
                print("Invista em ações")
else:
                print("Dado fornecido errado")