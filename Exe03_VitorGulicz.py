nome=input("Digite o seu nome: ")
salario=float(input("Digite o seu salario: "))
valorParcela=float(input("Digite o valor da parcela: "))
salarioPorCento=salario*0.08
if salarioPorCento>=valorParcela:
    print("Emprestimo de {} aceito {}! - Vitor Gulicz".format(valorParcela,nome))
else:
    print("Emprestimo de {negado {}! - Vitor Gulicz".format(valorParcela,nome))