#prnte com meu nome completo
print('Bem vindos a empresa da Valeska Carvalho')

#variáveis globais
lista_funcionarios = []
id_global = 4873946

#pede dados do funcionario e salva na lista em memória
def cadastrar_funcionario(id):
    print('Escolheu cadastrar funcionário')
    print(f'ID do funcionário: {id}')
    nome = input('Digite o nome do funcionário: ')
    setor = input('Digite o setor do funcionário: ')
    #input e validação do salário
    while True:
        try:
            salario = float(input('Digite o salário do funcionário: '))
            if salario < 0:
                raise 'Salário não poder ser negativo'
            break
        except: 
            print('Valor digitado inválido')
    funcionario = {'id': id, 'nome': nome, 'setor': setor, 'salario': salario}
    #salvando funcionário
    lista_funcionarios.append(funcionario.copy())

def consultar_funcionario():
    print('Escolheu consultar funcionário. Escolha dentre as opções abaixo: ')
    while True:
        print('+-------+-----------------------+')
        print('| Opcao | Menu                  |')
        print('+-------+-----------------------+')
        print('|   1   | Consultar Todos       |')
        print('|   2   | Consultar por ID      |')
        print('|   3   | Consultar por Sertor  |')
        print('|   4   | Retornar ao Menu      |')
        print('+-------+-----------------------+\n')
        #controle de submenu
        try:
            opcao_menu = int(input('Escolha a opção Desejada: '))
            if opcao_menu == 1: #mostra todos
                for funcionario in lista_funcionarios:
                    print(funcionario)
            elif opcao_menu == 2: #busca por ID
                id_consultar = int(input('Digite o ID do funcionário: '))
                encontrou = False
                for funcionario in lista_funcionarios:
                    if funcionario['id'] == id_consultar:
                        encontrou = True
                        print(funcionario)
                        break
                if not encontrou: 
                    print('Funcionário não encontrado')    
            elif opcao_menu == 3: #busca por setor
                setor_consultar = input('Digite um setor para buscar: ')
                encontrou = False
                for funcionario in lista_funcionarios:
                    if funcionario['setor'] == setor_consultar:
                        encontrou = True
                        print(funcionario)
                if not encontrou: 
                    print('Nenhum funcionário não encontrado')
                
            elif opcao_menu == 4: #volta para o menu anterior
                return         
            elif opcao_menu > 4:
                raise 'Opção de menu inválida'
        except:
            print('Opção inválida. Tente novamente ')
   
def remover_funcionario():
    print('Escolheu remver funcionário')
    while True:
        id_remover = int(input('Digite o ID do funcionário a ser removido: '))
        encontrou = False
        #iteração sobre a lista de funcionários transformada em dicionário
        for i, funcionario in enumerate(lista_funcionarios):
            if funcionario['id'] == id_remover:
                del lista_funcionarios[i]
                encontrou = True
        if encontrou:
            print('Funcionário removido')
            return
        else: 
            print('ID inválido')        
            



while True:
    print('+-------+-----------------------+')
    print('| Opcao | Menu                  |')
    print('+-------+-----------------------+')
    print('|   1   | Cadasrar Funcionário  |')
    print('|   2   | Consultar Funcionário |')
    print('|   3   | Remover Funcionário   |')
    print('|   4   | Encerrar Programa     |')
    print('+-------+-----------------------+\n')
    try:
        opcao_menu = int(input('Escolha a opção Desejada: '))
        if opcao_menu == 1: #cadastrar funcionário
            id_global += 1
            cadastrar_funcionario(id_global)
        elif opcao_menu == 2: #consultar funcionario
            consultar_funcionario()
        elif opcao_menu == 3: #remover funcionário
            remover_funcionario() 
        elif opcao_menu == 4: #encerra programa
            break    
        elif opcao_menu > 4:
            raise 'Opção de menu inválida'
    except:
        print('Opção inválida. Tente novamente ')

