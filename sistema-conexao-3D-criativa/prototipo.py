from colorama import Fore
from time import sleep

print(f"{50 * '='}")
print(f"{Fore.LIGHTRED_EX}{'SISTEMA CONEXÃO 3D CRIATIVA'}{Fore.RESET}".center(50))
print(f"{50 * '='}")
preço_por_grama = 0.09

while True:
    peso = float(input('Quantas gramas tem a peça [Gramas] -> '))
    tempo = float(input('Quanto tempo de impressão [Horas] -> '))
    mao_de_obra = str(input('A peça requer mão de obra [S / N] -> ')).upper().strip()

    # 1. Custo de fabricação de UMA peça
    custo_base = preço_por_grama * peso + (0.84 * tempo) + (0.30 * tempo)
    if mao_de_obra == 'S':
        custo_unitario = custo_base + 2.03
    else:
        custo_unitario = custo_base

    print(f"{60 * '='}")
    print(f"O custo unitário é {Fore.YELLOW}R${custo_unitario:.2f}{Fore.RESET}".center(50))
    print(f"{60 * '='}")

    tot = int(input('Quantas peças produzidas -> '))
    
    # 2. Definição do desconto por quantidade
    if tot < 5:
        desconto = 0      # Até 4 peças: Sem desconto
    elif 5 <= tot <= 10:
        desconto = 3      # De 5 a 10 peças: 3%
    else:
        desconto = 8      # A partir de 10 peças: 8%

    
    # Preço de venda unitário (Custo x 4)
    preço_venda_unitario = custo_unitario * 4
    
    # Valor bruto total (Preço de venda x Quantidade de peças)
    valor_bruto_total = preço_venda_unitario * tot
    
    # Aplicação do desconto em cima do valor total de venda
    valor_desconto = valor_bruto_total * (desconto / 100)
    valor_final = valor_bruto_total - valor_desconto

    # 4. Exibição dos Resultados de Venda
    print(f"{50 * '~'}")
    print(f"Valor de Venda Unitário: {Fore.CYAN}R${preço_venda_unitario:.2f}{Fore.RESET}")
    print(f"Subtotal ({tot}x peças): {Fore.RED}R${valor_bruto_total:.2f}{Fore.RESET}")
    
    if desconto > 0:
        print(f"Desconto Aplicado ({desconto}%): {Fore.YELLOW}- R${valor_desconto:.2f}{Fore.RESET}")
        
    print(f"VALOR FINAL A COBRAR: {Fore.LIGHTGREEN_EX}R${valor_final:.2f}{Fore.RESET}")
    print(f"{50 * '~'}\n")
    
    res = str(input('Deseja continuar [S / N] -> ')).upper().strip()
    if res == 'N':
        print('FINALIZANDO SISTEMA . . .')
        sleep(1)
        print('>>>>>>>>')
        sleep(1)
        break

print('FIM DO PROGRAMA')