import Murilo
import Juan
import Renato

while True:
  try:
    a = int(input('Número 1: '))
    b = int(input('Número 2: '))
    break
  except ValueError:
    print('Valor inválido')
    print()

while True:
  try:
    print("'1' Multiplicação | '2' Divisão")
    ops = int(input())
    if ops == 1:
      print(Juan.mult(a, b))
      break
    elif ops == 2:
      print(Juan.div(a, b))
      break
    else:
      raise ValueError()
  except ValueError:
    print('Valor inválido')
    print()



print("Você deseja fazer uma Soma ou Subtração?")
print("\n1 - Somar \n2 - Subtrair\n3 - Potência\n4 - Resto da divisão")
while True:
  try:
      resp = int(input("Digite qual vc deseja: "))
      if resp < 5 and resp > 0:
        break
  except ValueError:
    print("Valor Invalido!")
    print()


if resp == 1:
  print("Soma")
  while True:
    try:
      a = int(input("Digite o 1° valor: "))
      b = int(input("Digite o 2° valor: "))
      break
    except ValueError:
      print("Valor Invalido")

  soma = Murilo.soma(a, b)
  print(soma)

elif resp == 2:
  print("Subtração")
  while True:
    try:
        a = int(input("Digite o 1° valor: "))
        b = int(input("Digite o 2° valor: "))
        break
    except ValueError:
      print("Valor Invalido")
  sub = Murilo.sub(a, b)
  print(sub)

elif resp == 3:
  print("Potência")
  while True:
    try:
        a = int(input("Digite o 1° valor: "))
        break
    except ValueError:
      print("Valor Invalido")
  poten = Renato.pot(a)
  print(poten)

elif resp == 4:
  print("Resto da divisão")
  while True:
    try:
        a = int(input("Digite o 1° valor: "))
        b = int(input("Digite o 2° valor: "))
        break
    except ValueError:
      print("Valor Invalido")
  resto = Renato.resto(a, b)
  print(resto)




