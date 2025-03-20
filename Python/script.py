# x = [1, 2, 2, 3, 3]
# y = list(set(x)) # remove itens duplicados da variável x
# print(y)


# d = {"x": 2, "y": [True, False], "z": {1, 2, 3}} # criar um dicionário onde cada chave é composto por um valor seguido de ":"
# print(d["y"][0]) # exibir o dicionário criado

tabela = {"Alface": 6.00,
          "Tomate": 8.00,
          "Batata": 6.00,
          "Carne": 39.00,
          "Cenoura": 7.90
           }

produto = input("Digite o nome de um produto: ") # solicitar o nome de um produto
quanti = float(input("Qual a quantidade? ")) # converter a entrada para float
prodFinal = float(tabela.get(produto) * quanti)
pagamento = float(input(f"Total a pagar será de R$ {prodFinal:.2f}, Qual será a quantidade a ser paga? "))
if pagamento >= prodFinal:
    print(f"Pagamento efetuado com sucesso! Seu troco é de R${pagamento - prodFinal:.2f}")
elif pagamento < prodFinal:
    print(f"Pagamento insuficiente! Você precisa pagar R${prodFinal - pagamento:.2f}")
