import random
import colorama

def matrix(count=20):    
  print(colorama.Fore.GREEN + '.')
  if count == 'infinite':
    y = -1
    count = 2
  elif count != 'infinite':
    y = 1
  try:
    while count >= 0:
      a = random.randint(1,9)
      b = random.randint(1,9)
      c = random.randint(1,9)
      d = random.randint(1,9)
      e = random.randint(1,9)
  
      print(a,b,c,d,e,a,c,d,e,c,a,d,e,b,c,a,b,c,d,e,a,a,b,c,d)

      count -= y
  except:
    print(colorama.Fore.GREEN + '.')
    count = int(count)
    while count >= 0:
      a = random.randint(1,9)
      b = random.randint(1,9)
      c = random.randint(1,9)
      d = random.randint(1,9)
      e = random.randint(1,9)
  
      print(a,b,c,d,e,a,c,d,e,c,a,d,e,b,c,a,b,c,d,e,a,a,b,c,d)
      count -= y
