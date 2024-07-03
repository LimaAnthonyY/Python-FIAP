from geopy.geocoders import Nominatim

from Funcoes.pdf4_2 import gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes")

endereco=input("Digite um endereco com número e cidade: ")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    saida = resultado 
    print("Endereço completo.: ", resultado)
    print("\nBairro............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Regiao............: ", resultado[3])
    
gravar_arquivo(saida, "coordenadas.json")