from colorama import Fore
from time import sleep

print(f'{40 * '='}')
print(f'{Fore.LIGHTRED_EX}{'SISTEMA CONEXÃO 3D CRIATIVA'}{Fore.RESET}'.center(50))
print(f'{40 * '='}')
preço_por_grama = 0.09

while True:
    peso = float(input('Quantas gramas tem a peça [Gramas] -> '))
    tempo = float(input('Quanto tempo de impressão [Horas] -> '))
    mao_de_obra = str(input('A peça requer mão de obra [S / N] -> ')).upper().strip()

    custo_por_peça = preço_por_grama * peso + (0.84 * tempo) + (0.30 * tempo)
    custo_mao_de_obra = custo_por_peça + 2.03

    if mao_de_obra == 'S':
        print(f'{40 * '='}')
        print(f'O valor total é {Fore.GREEN}R${custo_mao_de_obra:.2f}{Fore.RESET}'.center(50))
        print(f'{40 * '='}')
    else:
        print(f'{40 * '='}')
        print(f'O valor total é {Fore.GREEN}R${custo_por_peça:.2f}{Fore.RESET}'.center(50))
        print(f'{40 * '='}')

    tot = int(input('Quantas peças produzidas -> '))
    #VALOR NORMAL ATÉ 4 PEÇAS
    if tot <= 4 and mao_de_obra == 'S':
        print(f'O valor total Bruto é {Fore.GREEN}R${custo_mao_de_obra:.2f}{Fore.RESET}')
        print(f'{40 * '~'}')
        print(f'Valor final de {tot} peças é {Fore.LIGHTGREEN_EX}R${tot * (custo_mao_de_obra * 4):.2f}{Fore.RESET}')
        print('')
    else:
        print(f'O valor total Bruto é {Fore.GREEN}R${tot * custo_por_peça:.2f}{Fore.RESET}')
        print(f'{40 * '~'}')
        print(f'O valor total de {tot} peças é {Fore.LIGHTGREEN_EX}R${tot * (custo_por_peça * 4):.2f}{Fore.RESET}')
        print('')
    #VALOR COM 
        
    res = str(input('Deseja continuar [S / N] -> ')).capitalize().strip()
    
                        # 100g x 1 hora = R$9.00 ( CUSTO MATERIAL)
                        # CUSTO MÃO DE OBRA ( QUANDO HOUVER ) - R$2,03
                        # CUSTO HORA MAQUINA - R$0,84
                        # CUSTO DE ENERGIA - R$0,30

    if res == 'N':
        print('FINALIZANDO SISTEMA . . .')
        sleep(1)
        print('>>>>>>>>')
        sleep(1)
        break
    
                        #Até 5 PEÇAS - VALOR NORMAL
                        #5 PEÇAS ATE 10 - 3% DESCONTO
                        #A PARTIR DE 10 PEÇAS - 8% DE DESCONTO

print('FIM DO PROGRAMA')