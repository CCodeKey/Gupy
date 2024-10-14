entrada = int(input("Digite um numero: "))
c = 0
a = 0
b = 1
for i in range(entrada-1):
    print(c)
    c = b + a 
    a = b
    b = c
    if entrada == c:
        print(f"Parabéns, sua resposta está correta, o valor {c} que voce digitou está na sequência de fibonacci.")
        quit()

print()
print("Valor não encontrado na sequência de fibonacci!")
print()