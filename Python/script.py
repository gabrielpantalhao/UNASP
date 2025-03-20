# x = [1, 2, 2, 3, 3]
# y = list(set(x)) # remove itens duplicados da variável x
# print(y)


# d = {"x": 2, "y": [True, False], "z": {1, 2, 3}} # criar um dicionário onde cada chave é composto por um valor seguido de ":"
# print(d["y"][0]) # exibir o dicionário criado

tabela = {"Alface": 6.00,
          "Tomate": 8.00,
          "Batata": 6.00,}

i = input("Digite o nome de um produto: ")

print(tabela.get(i))