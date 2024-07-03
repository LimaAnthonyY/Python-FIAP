usuarios = {}

usuarios = {"Chaves": ["Chaves Silva", "17/06/1975", "Recep_01"], "Quico": ["Enrico Flores", "03/06/1976", "Raiox_03"],
            "Florinda": ["Florinda Flores", "26/11/2016", "Recep_01"]}

print(usuarios)
print("##############========#########")

print(f"Dados: {usuarios.get('Chaves')}")


"""
ITEMS()
# [(“ologin”,[“nome”,”data”,”estacao”]),(“login2”,[“nome2”, “data2”,”est2”])]

VALUES()
# [ [“nome”,”data”,”estacao”],[“nome2”, “data2”,”est2”]]

KEYS()
# [“ologin”, “login2”]

HAS_KEY()
# Este método permitirá que você tenha a resposta se a chave existe ou não dentro do dicionário, ele irá retornar True (1) ou False (0).

CLEAR()
# Esvazia completamente o dicionário. 

POPITEM()
# Este é um método próprio para quem deseja montar algum dicionário que contenha elementos que serão executados, 
de maneira aleatória, individualmente e, na sequência, deverão ser eliminados do dicionário. 
Poderíamos pensar em um dicionário com dicas, e à medida que cada dica fosse exibida, 
automaticamente ela deveria ser retirada do dicionário. 
                         
"""