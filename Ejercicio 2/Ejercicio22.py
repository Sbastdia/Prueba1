list1=["PEP 8", "PEP 248", "PEP 257"]

def numero_caracteres(list):
    contador=0
    for i in list:
        contador+=len(i)
    return contador

print(numero_caracteres(list1))