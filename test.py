
lista_nomes = ['caetano', 'mateus', 'Alves', 'porto']
lista_fodase = [1,23,42,124,53,315,5315,135,9]

for i in lista_nomes:
    for j in lista_fodase:
        if(len(i) > 5):
            print(j)
        else:
            print('nome pequeno hehehehe')
            break
