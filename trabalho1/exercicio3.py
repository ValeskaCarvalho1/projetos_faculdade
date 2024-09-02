#print do meu nome completo
print('Bem vindos a Fábrica de Camisetas da Valeska Carvalho')

#função de input e validação de camiseta
def escolha_modelo():
    while True:
        
        print('Opções de camiseta:')
        print('Camiseta Manga Curta Simples (MSC)')
        print('Camiseta Manga Longa Simples (MLC)')
        print('Camiseta Manga Curta Com Estampa (MSE)')
        print('Camiseta Manga Longa Com Estampa (MLE)')

        #input e validação do modelo. Ignora case sensitivee
        modelo = input('Digite o modelo desejado: ').upper() 
        
        if modelo == 'MSC':
            return 1.80
        elif modelo == 'MLC':
            return 2.10
        elif modelo == 'MSE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else: 
            print('O valor digitado é inválido!\n')

#função de input e validação de quantidade de camisetas
def num_camisetas():
    while True:
        try:
            quantidade = int(input('Digite a quantidade de camisetas (Menor que Vinte Mil): '))
            if quantidade < 20:
                return quantidade
            elif quantidade >= 20 and quantidade < 200:
                return 5/100 * quantidade
            elif quantidade >= 200 and quantidade < 2000:
                return 7/100 * quantidade
            elif quantidade >= 2000 and quantidade < 20000:
                return 12/100 * quantidade
            else:
                #força a entrada no except
                raise 'Não é aceito pedidos nessa quantidade' 
        except: 
            print('O valor digitado é invalido\n')
#input e validação para cálculo do frete
def frete():
    while True:
        try:

            print('Escolha o tipo de frete: ')
            print('1 - Transportadora')
            print('2 - Sedex')
            print('0 - Retirar na Fábrica')

            opcao = int(input('Digite a sua opcao: '))
            if opcao == 1:
                return 100
            elif opcao == 2:
                return 200
            elif opcao == 0:
                return 0
            else:
                raise 'Opcao inválida'
        except:
            print('Opção inválida\n')

#função principal e cálculo do valor total
modelo = escolha_modelo()
qtd = num_camisetas()
vl_frete = frete()
total = (modelo * qtd) + vl_frete 
print(f'O valor total do pedido: R$ {total:.2f}')

 


            







    
