tabela = {
    "Alface": 5.00,
    "Batata": 4.55,
    "Tomate": 9.80,
    "Feijão": 7.30
}

valor_total = 0

while True:
    produto = input("Qual o produto? (digite 'sair' para encerrar) ").capitalize()
    
    if produto == "Sair":
        print("Bye!")
        break

    if produto not in tabela:
        print("Produto não encontrado!")
        continue

    quantidade = int(input("Quantidade: "))
    
    item = (produto, quantidade, tabela[produto] * quantidade)
    print(f"{item[0]} x{item[1]} = R${item[2]:.2f}")
    
    valor_total += item[2]

print(f"\nValor total das compras foi de: R${valor_total:.2f}")
