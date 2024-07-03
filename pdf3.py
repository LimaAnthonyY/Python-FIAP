
## Manipulação de lista, funções e modulos

#lista preenchida estaticamente
lista_estatica = ["xpto", True]

#lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]

#lista vazia
lista_vazia=[]

inventario=[]

resposta="S"
while resposta=="S":
  inventario.append(input("Equipamento: "))
  inventario.append(float(input("Valor: ")))
  inventario.append(int(input("Número Serial: ")))
  inventario.append(input("Departamento: "))
  resposta=input("Digite 'S' para continuar: ").upper()

print(lista_dinamica)

for elemento in inventario:
    print(elemento)

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite 'S' para continuar: ").upper()

for equipamento in equipamentos:
  print("Equipamento: ", equipamento)
  
# Indices

equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
  
## busca
    
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])
    
    """
    
        Todos os equipamentos “impressora” receberão uma depreciação
        (desvalorização após certo período) de 10%. Monte o 
        código que seria responsável por alterar o valor de 
        todos os equipamentos “impressora”.
          
    """
    
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
  if depreciacao==equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])
    
    """
    
            Um equipamento com um determinado número serial 
            foi danificado e será descartado. Precisamos 
            eliminar esse equipamento. 
            
            dica:
             para eliminar um item de uma lista, 
             você utilizará o comando “del”. 
             Exemplo: del lista[<indice>]

    """
    
serial=int(input("Digite o serial do equipamento" 
                 " que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])
  
  
## lista dentro de listas
inventario=[]
resposta = "S"
while resposta == "S":
  equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite 'S' para continuar: ").upper()

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])
  
# Funcoes para listas numericas

valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print(f"O equipamento mais caro custa: {max(valores)}")
  print(f"O equipamento mais barato custa: {min(valores)}")
  print(f"O total de equipamentos é de: {sum(valores)}")