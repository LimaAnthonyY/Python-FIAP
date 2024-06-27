## Introdução

nome = "Anthony"
empresa = "FIAP"
qtdeFuncionarios = 500
mediaMensalidade = 856.50

print(f"{nome} trabalha na empresa {empresa}")
print(f"Possui: {qtdeFuncionarios} funcionários.")
print(f"A média da mensalidade é de: {mediaMensalidade}\n\n\n")

# Atualizando os dados
nome = input("Digite o nome do funcionário: ")
empresa = input("Digite a instituição: ")
qtdeFuncionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(f"\n\n\n{nome} trabalha na empresa {empresa}")
print(f"Possui: {qtdeFuncionarios} funcionários.")
print(f"A média da mensalidade é de: {mediaMensalidade}\n\n\n")

print("==============Verificando os tipos de dados abaixo:==============")
print(f"O tipo de dado da variavel [nome] é: {type(nome)}")
print(f"O tipo de dado da variavel [empresa] é: {type(empresa)}")
print(f"O tipo de dado da variavel [qtde_funcionarios] é: {type(qtdeFuncionarios)}")
print(f"O tipo de dado da variavel [mediaMensalidade] é: {type(mediaMensalidade)}")

"""
    Outra forma de fazer isso é 
        print(nome + " trabalha na empresa " + empresa)
        print("Possui: ", qtde_funcionarios, " funcionarios.")
        print("A média da mensalidade é de: " + str(mediaMensalidade))
"""

print("\n\n\n------------Evento Secury Group-------------")
nomeFunc = input("Digite o seu nome: ")
nomeChef = input("Digite o nome do seu chefe: ")
nomeEven = input("Digite o nome do evento: ")
valEnt = float(input("Digite o valor gasto: "))

print(f"\n\nDeclaro para o senhor {nomeChef} que o senhor {nomeFunc} esteve presente no evento {nomeEven} e gastou o valor de R$ {valEnt} com a entrada.")

nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para sala AMARELA")
elif doenca_infectocontagiosa=="NAO":
    print("Encaminhe o paciente para sala BRANCA")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")

# SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero=="FEMININO" and idade>10:
        gravidez=input("A paciente está grávida? ").upper()
        if gravidez=="SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
        print("Paciente SEM prioridade")
        

nivel=input("Digite o nível de acesso: ").upper()
if nivel=="ADM" or nivel=="USR":
    genero=input("Digite o seu gênero: ").upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Olá administradora")
        else:
            print("Olá administrador")
    else:
        if genero=="FEMININO":
            print("Olá usuária")
        else:
            print("Olá usuário")
elif nivel=="GUEST":
    print("Olá visitante")
else:
    print("Olá desconhecido(a)")
