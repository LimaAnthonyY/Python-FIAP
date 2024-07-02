from geopy.geocoders import Nominatim
from Funcoes.pdf4_2 import ler_arquivo, gravar_arquivo

# Inicializa o geolocalizador
geolocator = Nominatim(user_agent="wazeyes")

# Lê o arquivo JSON de entrada
dicionario = ler_arquivo("entrada.json")
lista = dicionario["endereco"]

# Constrói o endereço completo com diferentes formatações
enderecos = [
    f"{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}",
    f"{lista[0]} {lista[1]}, {lista[2]}, {lista[3]} - {lista[4]}",
    f"{lista[0]} {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}, Brasil"
]

location = None
for endereco in enderecos:
    print(f"Tentando geocodificar: {endereco}")
    location = geolocator.geocode(endereco)
    if location:
        break

if location:
    saida = {"coordenadas": (location.latitude, location.longitude)}
else:
    saida = {"coordenadas": None, "erro": "Endereço não encontrado"}

# Grava o resultado no arquivo JSON de saída
gravar_arquivo(saida, "coordenadas.json")
