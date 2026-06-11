print(f'{40 * '='}')
print(f'{'SISTEMA CONEXÃO 3D CRIATIVA'}'.center(40))
print(f'{40 * '='}')
while True:
    peso = float(input('Quantas gramas tem a peça: [Gramas]'))
    tempo = float(input('Quanto tempo de impressão: [Horas]'))
    tot = int(input('Quantas peças produzidas: '))
    res = str(input('Deseja continuar [S / N]: ')).capitalize().strip()
    if res == 'N':
        break
#Até 5 PEÇAS - VALOR NORMAL
#5 PEÇAS ATE 10 - 3% DESCONTO
#A PARTIR DE 10 PEÇAS - 8% DE DESCONTO

print('FIM DO PROGRAMA')