#Imprimir meu nome completo. Satisfaz letras A e G do exercício
print('Bem-vindos ao atelier da Valeska Carvalho')

#pedir inputs do usuário
valorDoPedido = float(input('Digite o valor do pedido (Somente números): '))
quantidadeDeParcelas = int(input('Digite o valor de parcelas: '))
taxadeJuros = 0

#cálculo da taxa de juros
if quantidadeDeParcelas < 4:
    taxadeJuros = 0
elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6:
    taxadeJuros = 4/100
elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas < 9:
    taxadeJuros = 8/100
elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13:
    taxadeJuros = 16/100
else:
    taxadeJuros = 32/100

#cálculo do valor da parcela e total parcelado
valorDaParcela = valorDoPedido * (1+taxadeJuros) / quantidadeDeParcelas
valorTotalParcelado = valorDaParcela * quantidadeDeParcelas

if quantidadeDeParcelas >= 4:
    print(f'O valor das parcelas é de: R$ {valorDaParcela:.2f}')
    print(f'O valor total parcelado é de: R$ {valorTotalParcelado:.2f}')




