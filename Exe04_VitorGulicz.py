#No senailandia mulheres e homens podem servir o exercito do pais. o serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida. 
# Existe uma única restrição para o ingresso que é a idade da pessoa :
#a-	Para mulheres a idade aceita é entre 21 e 34 anos
#b-	Para homens a idade é entre 18 e 39 anos.

#Escreva um programa que leia três dados de entrada: Nome da pessoa, idade e sexo E informe se a pessoa será aceita ou não para o serviço

#OBS: Para o sexo deve ser lido apenas um caractere que pode ser f ou F, m ou M. Qualquer coisa diferente deve ser informado

nome=str(input("Digite o seu nome: "))
idade=int(input("Digite a sua idade: "))
genero=str(input("Digite o seu sexo(f - para mulheres | m - para homens): "))
if "f" in genero.lower():
 if 21<=idade<=34:
    print("Parabens {}, você foi aceita! - Vitor Gulicz".format(nome))
 else:
    print("Você foi negado - Idade Invalida {}! - Vitor Gulicz".format(nome))
elif "m" in genero.lower():
    if 18<=idade<=39:
        print("Parabens {}, você foi aceito! - Vitor Gulicz".format(nome))
    else:
        print("Você foi negado Idade Invalida {}! - Vitor Gulicz".format(nome))

else:
        print("Sexo invalido - Vitor Gulicz")