#Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o primeiro colocado não tenha mais de 50% dos votos
#Escreva um programa que leia o nome do município, a quantidade de votos do candidato mais votado. E informe s haverá segundo turno ou não


nomeMunicipio=str(input("Digite o nome do Municipio: "))
populaçao=int(input("Digite o numero da população do municipio:"))
votos=int(input("Digite o numero de votos que recebeu o candidato mais votado: "))
populaçaoVotos=populaçao/2
print("MUNICIPIO: {}".format(nomeMunicipio))
if populaçao>=200000 and votos>populaçaoVotos:
    print("Não haverá o segundo turno - Vitor Gulicz")
elif populaçao>=200000 and votos<populaçaoVotos:
    print("Haverá segundo turno - Vitor Gulicz")
else:
    print("População menor de 200 mil - Vitor Gulicz")
