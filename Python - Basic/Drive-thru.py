itens = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda', '🍦 Ice Cream', '🍪 Cookie']

def welcome():
  for i in range(len(itens)):
    print(f'{i + 1} = {itens[i]}')

welcome()

resp = int(input("Digite o número do seu pedido: "))

def get_item(x): 
  if resp <= 5 and resp != 0:
    print(itens[x - 1])
  else:
    print("Invalid input")
  return x

get_item(resp)