dinheiro_inicial = 10000
aposta = int(input("digite a quantidade a apostar: "))

if aposta > dinheiro_inicial:
    print("Sua aposta é superior ao valor que você tem! Digite uma quantia válida.")
    aposta = int(input("digite a quantidade a apostar: "))
elif aposta <= 0:
    print("Quantia inválida. Digite um valor de aposta maior!")
    aposta = int(input("digite a quantidade a apostar: "))