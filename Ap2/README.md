# sisLoja
Contempla projeto da disciplina Programação Estruturada (com uso da linguagem Python) do IBMEC RJ, no contexto da primeira Avaliação Bimestral  (AP1)

## Requisitos 

### 1. Descrição Geral

O sistema sisLoja contempla os seguintes módulos:
1. gerenciar o estoque (GerEstoque); 
2. gerenciar clientes (GerClientes); e 
3. gerenciar o fluxo de caixa (GerCaixa). 

Após o cliente escolher uma opção e realizar a operação selecionada no **módulo principal**, o sistema deverá retornar à tela inicial. 

#### 1.1 Funcionalidades do Módulo GerEstoque

O módulo GerEstoque permite que o usuário possa **incluir** ou **excluir** itens no estoque, selecionando uma das duas opções.  
Portanto, o uso do módulo GerEstoque requer dois tipos de transação:   
- inclusão de itens; ou 
- exclusão de itens.

Em uma transação para **inclusão**, o usuário **pode incluir vários itens ao estoque em uma mesma transação**, informando preliminarmente quantos itens serão incluídos.  
Para incluir cada item no estoque o usuário deve digitar: 
1.	o código do item (cod_item) – um número inteiro; 
2.	uma descrição do item (desc_item); e
3.	o valor do item, em reais (valor_item).   

**Todos os itens deverão ser armazenados em uma lista nomeada listaEstoque**.  
Após realizada toda a transação de inclusão, **o sistema apresenta um relatório da transação com a média dos valores dos itens cadastrados; e o código do item de maior valor com o seu respectivo valor.**  

Em um acesso para **exclusão**, o usuário pode excluir vários componentes, item por item, digitando o código do item a ser excluído.   
Após o usuário digitar o código do item a ser excluído o sistema **emite uma mensagem: “TEM CERTEZA QUE DESEJA EXCLUIR O ITEM?”.**   
Se o usuário digitar **não**, a transação será finalizada. Caso o usuário digite **sim**, o sistema:
1.	verificará se o código é válido (códigos válidos possuem a soma dos dígitos superior a 30 e inferior a 100). 
2.	Se o código for inválido, o sistema apresentará uma mensagem “CÓDIGO INVÁLIDO” (códigos não cadastrados devem ser tratados como códigos inválidos) e encerrar a transação; e
3.	se o código for válido, o sistema lerá a quantidade de itens a excluir e, se houver saldo em estoque, excluirá o item solicitado e apresentar uma mensagem “OPERAÇÃO REALIZADA COM SUCESSO”.
4.	Caso não haja saldo em estoque, o sistema apresentará uma mensagem “NÃO HÁ SALDO EM ESTOQUE” e encerrará a transação.
5.	Após a exclusão bem sucedida de um item apresentará uma mensagem perguntando se o usuário deseja excluir um novo item.   
Após realizada toda a transação de exclusão de todos os itens, o sistema apresentar um **relatório com a relação dos itens excluídos e o respectivo saldo em estoque.** 

#### 1.2 Funcionalidades do Módulo GerClientes
O módulo GerClientes permite que o usuário possa cadastrar vários clientes, digitando o CPF do cliente (cpf) e a renda (renda_cliente).   
A operação poderá ser interrompida quando o usuário digitar um CPF de cliente igual a 0.  
O sistema verifica se o CPF do cliente é um número válido.   
Após cadastrar os clientes, o módulo apresenta uma mensagem “OPERAÇÃO REALIZADA COM SUCESSO”, seguida de uma mensagem com o número de clientes cadastrados e com o percentual de clientes com renda superior a R$ 10.000,00; entre R$ 5.000,00 e R$ 10.000,00; e inferior a R$ 5.000,00.   
Todos os clientes são armazenados em uma lista nomeada listaClientes.
 
#### 1.3 Funcionalidades do Módulo GerCaixa
O módulo GerCaixa permite que o usuário registre a movimentação financeira de um determinado dia.   
O módulo deve permitir que o usuário digite no início do lançamento dos dados:   
1.	a data (data), 
2.	o saldo inicial do caixa no dia (saldo_inicial) e 
3.	o número total (N) de vendas realizadas. 

O lançamento dos dados de vendas pelo usuário no sistema GerCaixa é realizado pela ordem das operações realizadas naquele dia.  
Em cada lançamento de venda, o usuário do sistema deve lançar:
1.	O CPF do cliente (cpf),
2.	o código de cada item (cod_item), 
3.	a quantidade de itens (quant_item) e 
4.	o valor unitário, em reais, (valor_un) do item. 
5.	O sistema deverá calcular o valor total (tot_venda) da venda. 

Após o lançamento de todas as vendas, **o sistema apresenta um relatório** com:
1.	a data da movimentação, 
2.	o saldo final do caixa, 
3.	o valor médio das vendas no dia e
4.	o total de itens vendidos.

Não é necessário dar baixa no estoque em cada venda realizada. Essa transação está no módulo de gestão do estoque.

### 2. Interface com o usuário

#### 2.1 Interface do módulo principal  
O módulo principal sem uso de interface gráfica deverá possuir a seguinte forma de tela
```
-----------------------------
SISTEMA DE GESTÃO DE LOJA (SisLoja)
Selecionar a opção desejada:
Gestão de estoque (1)
Gestão de clientes (2)
Gestão de fluxo de caixa (3)
------------------------------
```

#### 2.2 Interface do módulo   
Cada transação de inclusão do módulo GerEstoque gera um relatório com a seguinte interface:

```
-----------------------------
Valor médio dos itens cadastrados: R$ x,xx
Item de maior valor cadastrado: código xxx, valor R$ x,xx
------------------------------
Teclar 0 para retornar à tela principal
```

Cada transação de exclusão do módulo GerEstoque gera um relatório com a seguinte interface:

```
----------------------------------------
RELATÓRIO DE ITENS EXCLUÍDOS
ITEM          SALDO
12678         22
345699        12
----------------------------------------
Teclar 0 para retornar à tela principal
```

#### 2.3 Interface do módulo GerCliente  
Cada transação de cadastro de clientes do módulo GerCliente deverá gerar um relatório com a seguinte interface:

```
---------------------------------
OPERAÇÃO REALIZADA COM SUCESSO
Total de clientes cadastrados: 12
----------------------------------------------
FAIXA                             PORCENTAGEM
Abaixo de R$ 5.000,00                 15%
Entre R$ 5.000,00 e R$ 10.000,00      70%
Acima de R$ 5.000,00                  15%
----------------------------------------------
Teclar 0 para retornar à tela principal
```

#### 2.4 Interface do módulo GerCaixa  
Cada transação de cadastro de vendas do módulo GerCaixa deverá gerar um relatório com a seguinte interface:

```
---------------------------
RELATÓRIO DE VENDAS
Data da movimentação: 12/07/2023
Saldo: R$ x,xx
Valor médio das vendas: R$ x,xx
Total das vendas: 34 unidades
---------------------------
Teclar 0 para retornar à tela principal
```




