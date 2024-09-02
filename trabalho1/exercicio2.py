#print com o nome completo
print('Bem vindos a loja de marmitas da Valeska Carvalho')

#Apresentação do menu para o usuário
print('Menu da loja:')
print('+---------+---------------------+---------------------+')
print('| Tamanho | Bife acebolado (BA) | Filé de Frango (FF) |')
print('+---------+---------------------+---------------------+')
print('|    P    |      R$ 16.00       |      R$ 15.00       |')
print('|    M    |      R$ 18.00       |      R$ 17.00       |')
print('|    G    |      R$ 22.00       |      R$ 21.00       |')
print('+---------+---------------------+---------------------+\n')

#Inicialização do valor total
total = 0
while True:
    #input e validação do sabor. Ignora case sensitive 
    sabor = input('Escolha o sabor da marmita [BA|FF]: ').upper()
    if sabor != "BA" and sabor != "FF":
        print('Sabor inválido. Tente novamente')
        continue

    #input e validação do tamanho. Ignora case sensitive 
    tamanho = input('Escolha o tamanho da marmita [P|M|G]: ').upper()
    if tamanho != "P" and tamanho != "M" and tamanho != "G":
        print('Tamanho inválido. Tente novamente')
        continue
    
    #definição aninhada do preço e feedback para o usuário
    if sabor == "BA":
        if tamanho == "P":
            preco = 16
            print(f'Você pediu um Bife Acebolado pequeno: R$ {preco:.2f}')
        elif tamanho == "M":
            preco = 18
            print(f'Você pediu um Bife Acebolado médio: R$ {preco:.2f}')
        elif tamanho == "G":
            preco = 22
            print(f'Você pediu um Bife Acebolado grande: R$ {preco:.2f}')
    elif sabor == "FF":
        if tamanho == "P":
            preco = 15
            print(f'Você pediu um Filé de Frango pequeno: R$ {preco:.2f}')
        elif tamanho == "M":
            preco = 17
            print(f'Você pediu um Filé de Frango médio: R$ {preco:.2f}')
        elif tamanho == "G":
            preco = 21
            print(f'Você pediu um Filé de Frango grande: R$ {preco:.2f}')
    
    #acumulador do total
    total += preco

    #input e validação se o usuário quer mais algum item. Ignora case sensitive 
    mais_algo = input('Deseja algo mais? [S|N]').upper()
    if mais_algo != 'S':
        break

print(f'O valor total do pedido é: R$ {total:.2f}')   



                
