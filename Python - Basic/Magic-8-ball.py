import random

num = random.randint(0, 9)

input('Qual a sua dúvida: ')

if num == 8:
  print('Magic 8 ball: Sim, definitivamente')
elif num == 7:
  print('Magic 8 ball: É decididamente assim')
elif num == 6:
  print('Magic 8 ball: Sem dúvidas')
elif num == 5:
  print('Magic 8 ball: Resposta nebulosa, tente novamente')
elif num == 4:
  print('Magic 8 ball: Pergunte novamente mais tarde')
elif num == 3:
  print('Magic 8 ball: Melhor eu não lhe dizer')
elif num == 2:
  print('Magic 8 ball: Meus recursos dizem não')
elif num == 1:
  print('Magic 8 ball: Perspectiva não tão boa')
else:
  print('Magic 8 ball: Questionável')