clientes = {}


def ger_clientes():
    # Função para checar a validade do CPF
    def checa_cpf(x):
        if len(str(x)) != 11:
            return False

        res = sum(int(i) for i in str(x))
        if (res % 11) == 0:
            return True
        else:
            return False

    # Mensagem ao final da operação
    def mensagem_cliente():
        print('---------------------------------')
        print('OPERAÇÃO REALIZADA COM SUCESSO')
        print(f'Total de clientes cadastrados: {len(clientes)}')
        print('----------------------------------------------')
        print('FAIXA                              PORCENTAGEM')
        print(f'Abaixo de R$ 5.000,00             {calc_porcentagem(0)}%')
        print(f'Entre R$ 5.000,00 e R$ 10.000,00   {calc_porcentagem(5000)}%')
        print(f'Acima de R$ 10.000,00             {calc_porcentagem(10000)}%')
        print('----------------------------------------------')
        print('Teclar 0 para retornar à tela principal')

    def calc_porcentagem(valor):
        count = 0
        for cliente in clientes.values():
            if cliente[1] > valor:
                count += 1
        porcentagem = (count / len(clientes)) * 100
        return round(porcentagem, 2)

    while True:
        cpf = input("Informe o CPF: ")
        if cpf == '0':
            break

        if checa_cpf(cpf):
            renda_cliente = float(input("Informe a renda do cliente: "))
            clientes[cpf] = [cpf, renda_cliente]
        else:
            print('CPF inválido')

    mensagem_cliente()
