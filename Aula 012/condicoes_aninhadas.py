nome = str(input("Qual o seu nome?"))
if (nome == "Gustavo"):
    print("Que nome bonito")
elif nome == "Pedro" or nome == "Maria" or nome == "Ana":
    print("Seu nome é bem popular no Brasil")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}!".format(nome))