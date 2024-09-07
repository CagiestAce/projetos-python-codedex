altura = int(input('Digite sua altura em cm: '))
dinheiro = int(input('Quanto dinheiro você tem: '))

if altura >= 137 and dinheiro >= 10:
  print('Pode entrar!!!')
elif altura >= 137 and dinheiro <= 10:
  print('Pobre lixo')
elif altura <= 137 and dinheiro >= 10:
  print('Seu anão rebaixado')
else:
  print('Vaza daqui seu fudido!!!')