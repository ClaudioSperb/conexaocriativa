print(f'{40 * '='}')
print(f'{'SISTEMA CONEXÃO 3D CRIATIVA'}'.center(40))
print(f'{40 * '='}')
while True:
    peso = float(input('Quantas gramas tem a peça: [Gramas]'))
    tempo = float(input('Quanto tempo de impressão: [Horas]'))
    res = str(input('Deseja continuar [S / N]: ')).capitalize().strip()
    if res == 'N':
        break
print('FIM DO PROGRAMA')