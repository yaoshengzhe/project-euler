import math

def miller_rabin_prime_test(a, d, n, s):
    x = pow(a, d, n)
    if x == 1:
      return False
    for r in range(s):
      if x == n-1:
        return False
      x = x*x%n
    return True

def is_prime(n):
  if n < 19:
      return n in [2, 3, 5, 7, 11, 13, 17]

  if not n % 2:
      return False
  if not n % 3: return False
  if not n % 5: return False
  if not n % 7: return False
  if not n % 11: return False
  if not n % 13: return False
  if not n % 17: return False
  if n < 361: return True

  if not n%37: return False
  if not n%97: return False
  if n<31621:
    return pow(2, n-1, n)==1 and pow(3, n-1, n)==1

  for p in [19, 31, 41, 43, 73]:
    if not n%p: return False

  if n<721801:
    return pow(2, n-1, n)==1 and pow(3, n-1, n)==1 and pow(5, n-1, n)==1

  if n<1373653:
    temoins={2,3}
  elif n<9080191:
    temoins={31, 73}
  elif n<4759123141:
    temoins={2, 7, 61}
  elif n<2152302898747:
    temoins={2, 3, 5, 7, 11}
  elif n<3474749660383:
    temoins={2, 3, 5, 7, 11, 13}
  elif n<341550071728321:
    temoins={2, 3, 5, 7, 11, 13, 17}
  else: temoins=set(range(2, int(2*math.log(n)**2)))

  s = 0
  d = n-1
  while not d%2:
    d>>=1
    s+=1

  for p in temoins:
    if (not n%p): return False

  for p in temoins:
    if miller_rabin_prime_test(p, d, n, s): return False
  return True
