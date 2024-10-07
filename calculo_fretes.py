import os
from collections import defaultdict

entregas = []

def print_menu():
    print('CÁLCULO DE TAXAS')
    print('-' * 30)
    print('1. Adicionar venda\n2. Tabela taxa/motorista\n3. Alterar valores\n4. Fechar programa\n')
    
def escolher_opcao():
    
    try:
        opcao_menu = int(input('Escolha uma das opções: '))
        if opcao_menu == 1:
            os.system('cls')
            pedir_informacoes()
        
        if opcao_menu == 2:
            os.system('cls')
            mostrar_tabela()
            calcular_taxa()
            
        if opcao_menu == 3:
            os.system('cls')
            alterar_valores()
        if opcao_menu == 4:
            encerrar_programa()
            
    except:
        main()

def main():
    os.system('cls')
    print_menu()
    escolher_opcao()
    input('Clique para retornar')
    main()

def pedir_informacoes():
    
    print('ADICIONAR VENDA\n')
    cliente = str(input('Qual é o nome do cliente? ')).title().strip()
    entregador = str(input('Qual é o entregador? ')).strip().title()
    taxa = int(input('Qual é a taxa? R$ '))
    
    if taxa < 10:
        print('Valor inválido, tente novamente.')
        pedir_informacoes()
        
    else:
        
        gratis = str(input('A entrega é grátis?[S/N] ')).lower()
        
        if gratis in ['n', 'nao', 'não']:
            gratis = False
            nova_entrega = {'Cliente': cliente,'Entregador': entregador, 'Taxa': taxa, 'Grátis': gratis}
            entregas.append(nova_entrega)
            
        elif gratis in ['s', 'sim']:
            gratis = True
            nova_entrega = {'Cliente': cliente, 'Entregador': entregador, 'Taxa': taxa, 'Grátis': gratis}
            entregas.append(nova_entrega)
            
        else:
            print("Resposta inválida. Por favor, digite S ou N.")
            pedir_informacoes()
           
def mostrar_tabela():
    
    print('TABELA DE ENTREGAS\n')
    for numero_entrega, entrega in enumerate(entregas):
        
        print(f'Venda {numero_entrega + 1}:\n')
        
        for chave, valor in entrega.items():
            if valor == True:
                valor = 'sim'
            elif valor == False:
                valor = 'não'
            print(f'{chave}: {valor}')
            
        print('-' * 20)
            
def calcular_taxa():
    
    #taxa por vendedor, taxa paga pelo cliente(10)*, taxa paga pega lusca(todas)*, taxa gratis*
    contador_cliente = soma_diferenca = contador_gratis = total_taxa_gratis = total_taxa_cliente = 0
    entregas_por_entregador = defaultdict(int)
    
    
    for entrega in entregas:
        #taxa paga pela lusca(diferença)
        diferenca_lusca = entrega['Taxa'] - 10
        soma_diferenca += diferenca_lusca
        #taxa cliente
        if not entrega['Grátis']: 
            contador_cliente += 1
            total_taxa_cliente = contador_cliente * 10
        #taxa gratis
        if entrega['Grátis']:
            contador_gratis += 1
            total_taxa_gratis = contador_gratis * 10
        #entregas por entregador
        entregas_por_entregador[entrega['Entregador']] += entrega['Taxa']
    
        
    for nome_entregador, taxa_entrega in entregas_por_entregador.items():
        print(f'{nome_entregador}: R${taxa_entrega},00')
    print('=' * 35)
    print(f'Taxa paga por clientes: R${total_taxa_cliente},00')
    print('=' * 35)
    print(f'Diferença paga pela Lusca: R${soma_diferenca},00')
    print('=' * 35)
    print(f'Total de taxas grátis: R${total_taxa_gratis},00')
    print('=' * 35)
    soma_total = (total_taxa_gratis + total_taxa_cliente + int(soma_diferenca))
    print(f'Total de vendas: {soma_total}')
    print('=' * 35)
    input()
    
def alterar_valores():
    
    print('ALTERAR VALORES DAS VENDAS\n')
    try:
        opcao_alteracao = int(input('Digite o número da venda que gostaria de alterar: '))
        
        cliente = str(input('\nQual é o nome do cliente? ')).strip().title()
        entregador = str(input('Qual é o entregador? ')).strip().title()
        taxa = int(input('Qual é a taxa? R$ '))
        
        if taxa < 10:
            print('Valor inválido, tente novamente.')
            alterar_valores()
            
        else:
                
            gratis = str(input('A entrega é grátis?[S/N] ')).lower()
            
            if gratis in ['n', 'nao', 'não']:
                gratis = False
                entregas[opcao_alteracao - 1].update({'Cliente': cliente, 'Entregador': entregador, 'Taxa': taxa, 'Grátis': gratis})
                
            elif gratis in ['s', 'sim']:
                gratis = True
                entregas[opcao_alteracao - 1].update({'Cliente': cliente, 'Entregador': entregador, 'Taxa': taxa, 'Grátis': gratis})
                
            else:
                print("Resposta inválida. Por favor, digite S ou N.")
                alterar_valores()
    except:
        main()

def encerrar_programa():
    os.system('cls')
    print('Programa encerrado')
    
    
main()

if __name__ == '__main__':
    main()
    
