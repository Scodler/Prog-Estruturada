def ger_caixa():  # modulo GerCaixa

    vendas = []  # Lista de vendas

    # Resumo do total do cliente
    # x = código do cliente | y = valor gasto
    def relatorio_cliente(x, y):
        print('------------------------------------------')
        print(f'Cliente {x} Total de vendas: R$ {y}')
        print('------------------------------------------')

    # Valida o código do cliente (cpf)
    def checaCpf(x):
        # Checa o tamanho do cpf
        if len(str(x)) != 11:
            return 0
        # Valida o cpf
        res = sum(int(i) for i in str(x))
        if (res % 11) == 0:
            return 1
        else:
            return 0

    # Valida o código do produto
    def valida_cod(x):
        res = sum(int(i) for i in str(x))
        if res <= 20:
            return 0
        else:
            return 1

    # Relatório do caixa com
    # x = data | y = Saldo | z = valor médio
    # k = unidades vendidas | w = código do cliente que mais gastou
    def relatorio_caixa(x, y, z, k, w):
        print('---------------------------')
        print('RELATÓRIO DE VENDAS')
        print(f'Data da movimentação: {x}')
        print(f'Saldo: R$ {y:.2f}')
        print(f'Valor médio das vendas: R$ {z:.2f}')
        print(f'Total das vendas: {k} unidades')
        print(f'Cliente de maior consumo: código {w}')
        print('---------------------------')
        print('Teclar 0 para retornar à tela principal')

    # Relatório de movimentação financeira
    # x = data | y = saldo | z = valor médio | k = total vendas
    def relatorio_movimentacao(x, y, z, k):
        print('---------------------------')
        print('RELATÓRIO DE MOVIMENTAÇÃO FINANCEIRA')
        print(f'Data da movimentação: {x}')
        print(f'Saldo: R$ {y:.2f}')
        print(f'Valor médio das vendas: R$ {z:.2f}')
        print(f'Total das vendas: {k} unidades')
        print('---------------------------')
        print('Teclar 0 para retornar à tela principal')

    # Cadastrar venda na lista de vendas
    def cadastrar_venda(data, cpf, cod_item, quantidade):
        venda = {
            'data': data,
            'cpf': cpf,
            'cod_item': cod_item,
            'quantidade': quantidade
        }
        vendas.append(venda)

    data = input('Insira a Data (dd/mm/aa): ')
    saldo_inicial = float(input('Informe o saldo inicial do dia: '))
    N = int(input('Informe o número de vendas do dia: '))
    vendas_tot = N
    tot_saldo = 0
    maior = 0
    unidades = 0
    maior_cliente = 0

    while N != 0:
        cpf = int(input('Informe o código do cliente: '))
        tot_cliente = 0

        if checaCpf(cpf) == 1:  # So decrementa o contador quando o código é verdadeiro
            n_compras = int(input('Informe o número de compras desse cliente no dia: '))
            if N - n_compras >= 0:
                N -= n_compras
                for compra in range(n_compras):
                    n_itens_compra = int(input('Informe o número de itens distintos na compra: '))

                    while n_itens_compra != 0:
                        # Loop while que só permite códigos de itens válidos
                        cod_item = int(input('Informe o código do item: '))

                        if valida_cod(cod_item) == 1:
                            # Após validar o código, coleta a quantidade de itens, o valor unitário,
                            # calcula o tot_cliente, soma às unidades e diminui um ciclo do loop
                            quant_item = int(input('Informe a quantidade de itens: '))
                            valor_un = float(input('Informe o valor unitário: '))
                            tot_cliente += quant_item * valor_un
                            unidades += quant_item
                            n_itens_compra -= 1  # Só decrementa o contador quando o código é verdadeiro
                            cadastrar_venda(data, cpf, cod_item, quant_item)
                        else:
                            print('Código inválido!')

                    relatorio_cliente(cpf, tot_cliente)

            else:
                print('Número de compras inválido')

        else:
            print('Código do cliente inválido!')

        # A cada loop, compara o total do cliente com a variável maior,
        # caso o primeiro seja maior, atualiza as variáveis maior_cliente e maior
        if tot_cliente > maior:
            maior_cliente = cpf
            maior = tot_cliente
        tot_saldo += tot_cliente

    # X   |     Y = Saldo       | Z = Média de compra
    relatorio_caixa(data, (tot_saldo + saldo_inicial), (tot_saldo / vendas_tot), unidades, maior_cliente)

    # K      |    W

    relatorio_movimentacao(data, (tot_saldo + saldo_inicial), (tot_saldo / vendas_tot), unidades)


# Exemplo de uso
ger_caixa()

