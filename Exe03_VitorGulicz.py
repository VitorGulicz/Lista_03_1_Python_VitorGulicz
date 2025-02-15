#Uma emprensa financeira consegue empréstimos a pessoas físicas até 8% do salario da pessoa
# escreva um programa que leia dois números reais e o valor da parcela e informe se o empréstimo será concedido ou não

nome=input("Digite o seu nome: ")
salario=float(input("Digite o seu salario: "))
valorParcela=float(input("Digite o valor da parcela: "))
salarioPorCento=salario*0.08
if salarioPorCento>=valorParcela:
    print("Emprestimo de {} aceito {}! - Vitor Gulicz".format(valorParcela,nome))
else:
    print("Emprestimo de {} negado {}! - Vitor Gulicz".format(valorParcela,nome))