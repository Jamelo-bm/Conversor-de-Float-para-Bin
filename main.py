# Faça um programa em Python que converta o número decimal 15,25 para sua representação em ponto flutuante com base 2

import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# =============================================

def Coleta():

  valor = input("\n Digite um número de ponto flutuante: ")

  try:

    valor = float(valor)
    clear()
    Conversão(valor)

  except ValueError:

    clear()
    print("\n " + valor + " não corresponde às exigências.")
    Coleta()


# =============================================


def Conversão(valor):

  global valor_inicial
  valor_inicial = valor
  
  partes = str(valor).split(".")

  # ===========================================

  if int(partes[0]) >= 0:
    sinal = 0

  else:
    sinal = 1
    x, partes[0] = str(partes[0]).split("-")

  # ===========================================

  parte_inteiro = partes[0]
  parte_decimal = float("0." + partes[1])

  # ===========================================

  decimal = int(parte_inteiro)
  bin_inteiro = bin(decimal)[2:]

  # ===========================================

  bin_decimal = ""

  for i in range(64):
    
    parte_decimal *= 2
    inteiro = int(parte_decimal)
    bin_decimal += str(inteiro)
    parte_decimal -= inteiro

    if parte_decimal == 0:
      break
  
  Normalização(sinal, str(bin_inteiro), str(bin_decimal))

# =============================================

def Normalização(sinal, bin_inteiro, bin_decimal):

  global base, deslocamento

  mantissa = str(bin_inteiro + ".")

  notação = '{:e}'.format(float(mantissa))

  base, deslocamento = notação.split('e')
  deslocamento = int(deslocamento)

  mantissa = bin_inteiro[1:] + bin_decimal
  
  Expoente(sinal, mantissa[:52])

# =============================================

def Expoente(sinal, mantissa):

  decimal = int(1023 + deslocamento)
  expoente = bin(decimal)[2:]

  Combinação(sinal, expoente, mantissa)

# =============================================

def Combinação(sinal, expoente, mantissa):

  print("\n · Sinal: " + str(sinal))
  print(" · Expoente: " + str(expoente))
  print(" · Mantissa: " + str(mantissa))

  resultado = str(sinal) + str(expoente) + str(mantissa)

  diferença = 64 - len(resultado)

  for i in range(diferença):
    resultado += "0"

  print("\n Resultado: " + resultado + "\n ")

  ReConversão(sinal, expoente, mantissa)
  
# =============================================

def ReConversão(sinal, expoente, mantissa):

  expoente = int(expoente, 2) - 1023

  num_bin = str(mantissa)
  num_dec = 0
  posição = -1
  
  for digito in num_bin:
    if digito == "1":
      num_dec += 2 ** posição
    posição += -1
  
  mantissa = 1 + num_dec
  
  valor = (-1) ** int(sinal) * float(mantissa) * 2 ** float(expoente)

  print(" ---------------\n")
  
  print(" Valor Inserido: " + str(valor_inicial))
  print(" Valor Re-feito: " + str(valor))

  print("\n Margem de Erro: " + str(float(valor_inicial) - float(valor)) + "\n")

  
  
# =============================================

Coleta()

