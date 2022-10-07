lista = [18, 50, 210, 80, 145, 333, 70, 30]
for i in range(len(lista)):
    if lista[i] > 300:
        break
    if lista[i] % 10 == 0 and lista[i] < 200:
        print(lista[i])
