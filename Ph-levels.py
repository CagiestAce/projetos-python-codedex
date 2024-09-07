ph = int(input('Digite o número do PH: '))

if ph < 6.8:
  print('Ácido')
elif ph > 7:
  print('Básico')
else:
  print('Neutro')