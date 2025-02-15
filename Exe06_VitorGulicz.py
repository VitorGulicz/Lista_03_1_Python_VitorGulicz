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
    print("Não haverá segundo turno - Vitor Gulicz")
