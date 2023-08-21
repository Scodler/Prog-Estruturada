# Fernando Mendonça | 202208935079 | TA
# Lorran Porto | 202303219962 | TA
# André Casemiro | 202303100418 | TA
# Vitor Ribeiro | 202301215145 | TA
# Pedro Caravellos | 202302174264 | TA

from GerCaixa import ger_caixa
from GerCliente import ger_clientes
from GerEstoque import ger_estoque


def sis_loja():
  print(
    '-----------------------------\nSISTEMA DE GESTÃO DE LOJA (SisLoja)\nSelecionar a opção desejada:\nGestão de estoque (1)\nGestão de clientes (2)\nGestão de fluxo de caixa (3)\n------------------------------'
  )
  escolha = int(input(''))
  if escolha == 1:
    ger_estoque()
    tela_princ()
  elif escolha == 2:
    ger_clientes()
    tela_princ()
  elif escolha == 3:
    ger_caixa()
    tela_princ()
  else:
    print(
      "-----------------------------\nOperação inválida! \nTente Novamente!")
    sis_loja()


def tela_princ():  #retorna a tela principal
  x = int(input(' '))
  if x == 0:
    sis_loja()


clientes = []
estoque = []
sis_loja()
