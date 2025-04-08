# x = [1, 2, 2, 3, 3]
# y = list(set(x)) # remove itens duplicados da variável x
# print(y)


# d = {"x": 2, "y": [True, False], "z": {1, 2, 3}} # criar um dicionário onde cada chave é composto por um valor seguido de ":"
# print(d["y"][0]) # exibir o dicionário criado

# tabela = {"Alface": 6.00,
#           "Tomate": 8.00,
#           "Batata": 6.00,
#           "Carne": 39.00,
#           "Cenoura": 7.90
#            }

# produto = input("Digite o nome de um produto: ") # solicitar o nome de um produto
# quanti = float(input("Qual a quantidade? ")) # converter a entrada para float
# prodFinal = float(tabela.get(produto) * quanti)
# pagamento = float(input(f"Total a pagar será de R$ {prodFinal:.2f}, Qual será a quantidade a ser paga? "))
# if pagamento >= prodFinal:
#     print(f"Pagamento efetuado com sucesso! Seu troco é de R${pagamento - prodFinal:.2f}")
# elif pagamento < prodFinal:
#     print(f"Pagamento insuficiente! Você precisa pagar R${prodFinal - pagamento:.2f}")


# def eh_par(x):
#     if x % 2 == 0:
#         return f"{x} é par"
#     # else:
#     #     return "impar"
#     elif x % 2 != 0:
#         return f"{x} é impar"
# print(eh_par(1224))

# novo_salario("junior", 2000)
#     tabela = {}
# def new_pay(cargo, salario):
#     cargo = cargo.lower()
    
#     if cargo == "junior":
#         return f"Seu cargo é {cargo}, e seu novo salário é de R${salario * 1.1:.2f}"
#     elif cargo == "pleno":
#         return f"Seu cargo é {cargo}, e seu novo salário é de R${salario * 1.15:.2f}"
#     elif cargo == "senior":
#         return f"Seu cargo é {cargo}, e seu novo salário é de R${salario * 1.2:.2f}"
#     else:
#         return "Cargo não encontrado"
    
# print(new_pay("Pleno", 5000))

# def somar_lista(lista):
#     soma = 0
#     for j, i in enumerate(lista):
#         if j > 2:
#             soma += i
#     return soma

# print(somar_lista([4, 5, 6, 7, 8]))

# def media_lista(lista):
#     soma = 0
#     n = 0
#     for i in lista:
#             soma += i
#             n += 1
#     return soma/n

# print(media_lista([4, 5, 6, 7, 8]))

# a = "teste1"
# def f():
#     a = "teste2"
#     return a
# print(f())
# print(a)

# try:
#     x = y + 1
#     print(x)
# except Exception as e:
#     print(e)
# try:
#     [1, 2][3]
#     print(x)
# except NameError:
#     print("Erro de nome")
# except TypeError:
#     print("Erro de tipo")
# except Exception as e:
#     print("Outro erro ", e)

i = 0
while i < 10:
    print(i)
    i += 1
    