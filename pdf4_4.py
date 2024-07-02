from Funcoes.pdf4_2 import *
import os

inventario = ler_arquivo("inventario_json.json")
opcao=chamarMenu()
while opcao:
    if opcao==1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao==2:
        exibir("inventario_json.json")
    else:
        print("Digite uma opção válida.")
        os.system('cls')
        opcao = chamarMenu()
    opcao = chamarMenu()