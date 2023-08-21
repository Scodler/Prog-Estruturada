estoque = {}


def ger_estoque():
    # Função para validar o código do item
    def valida_cod(x):
        res = sum(int(i) for i in str(x))
        if res <= 20:
            return False
        else:
            return True

    # Função para confirmar a exclusão do item
    def confirma_excl(x):
        print('TEM CERTEZA QUE DESEJA EXCLUIR O ITEM?')
        resp = input('')
        if resp == 'sim':
            del estoque[x]
            print(f'Item excluído: {x}')

    # Função para atualizar um item
    def alterar_item(x):
        if x in estoque:
            desc_item = input('Informe a nova descrição do item: ')
            valor_item = float(input('Informe o novo valor do item: '))
            saldo_item = int(input('Informe o novo saldo em estoque: '))
            estoque[x] = [desc_item, valor_item, saldo_item]
            print(f'Item alterado: {x}')
        else:
            print(f'O item {x} não está cadastrado.')

    def natureza_estoque():
        print('Selecionar a opção desejada:')
        print('1. Incluir itens')
        print('2. Excluir item')
        print('3. Alterar item')

    def conclu_excl():
        print('----------------------------------------')
        print('RELATÓRIO DE ITENS EXCLUÍDOS')
        print('ITEM     SALDO')
        for item, info in estoque.items():
            if info[2] == 0:
                print(item, "    ", info[2])
        print('----------------------------------------')
        input('Pressione Enter para retornar à tela principal')

    def conclu_incl():
        soma = 0
        maior = 0
        maior_cod = None

        for item, info in estoque.items():
            soma += info[1]
            if info[1] > maior:
                maior = info[1]
                maior_cod = item

        media_valor = soma / len(estoque)
        print('-----------------------------')
        print(f'Valor médio dos itens cadastrados: R$ {media_valor}')
        print(f'Item de maior valor cadastrado: código {maior_cod}, valor R$ {maior}')
        print('-----------------------------')
        input('Pressione Enter para retornar à tela principal')

    natureza_estoque()
    natureza = int(input('Selecionar a opção desejada: '))

    if natureza == 1:
        N = int(input('Informe o número de itens que deseja adicionar: '))

        for _ in range(N):
            x = True
            while x:
                cod_item = input('Informe o código do item: ')

                if not valida_cod(cod_item):
                    print('Código inválido')
                else:
                    desc_item = input('Informe a descrição do item: ')
                    valor_item = float(input('Informe o valor do item: '))
                    saldo_item = int(input('Informe o saldo em estoque do item: '))
                    estoque[cod_item] = [desc_item, valor_item, saldo_item]
                    x = False

        conclu_incl()

    elif natureza == 2:
        cod_excl = input('Informe o código do item a ser excluído: ')
        if cod_excl in estoque:
            confirma_excl(cod_excl)
        else:
            print(f'O item {cod_excl} não está cadastrado.')
        conclu_excl()

    elif natureza == 3:
        cod_alt = input('Informe o código do item a ser alterado: ')
        alterar_item(cod_alt)


ger_estoque()
