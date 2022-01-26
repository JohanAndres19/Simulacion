import random

ingresado = int(input())
for i in range(ingresado):
    lista=[]

    diferencia=0

    while diferencia !=3:
        cara_moneda = random.randint(0,99)
        if cara_moneda <50:
            lista.append('Ca')
        elif cara_moneda >=50:
            lista.append('Cr')
        if abs(lista.count('Ca')-lista.count('Cr'))==3:
            diferencia= abs(lista.count('Ca')-lista.count('Cr'))        
    else:
        print(len(lista),lista.count('Ca'),lista.count('Cr'),8-len(lista))    

