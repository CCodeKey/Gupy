entrada = str(input("Digite uma palavra: "))
qtd = 0
for i in range(len(entrada)):
    if entrada[i] == 'a' or entrada[i] == 'A':
        qtd = qtd + 1

print("NOME = ", entrada)
print("Aa = ", qtd)