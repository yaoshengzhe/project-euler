#! /usr/bin/python

import math
from math import log

def is_prime(n):
  if n<19: return n in [2, 3, 5, 7, 11, 13, 17]

  if not n%2: return False
  if not n%3: return False
  if not n%5: return False
  if not n%7: return False
  if not n%11: return False
  if not n%13: return False
  if not n%17: return False
  if n<361: return True

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
  else: temoins=set(range(2, int(2*log(n)**2)))

  s = 0
  d = n-1
  while not d%2:
    d>>=1
    s+=1

  def test(a):
    "test de miller_rabin"
    x = pow(a, d, n)
    if x == 1:
      return False
    for r in range(s):
      if x == n-1:
        return False
      x = x*x%n
    return True

  for p in temoins:
    if (not n%p): return False

  for p in temoins:
    if test(p): return False
  return True

def is_truncatable_prime(num):
    if not is_prime(num):
        return False
    n = num
    length = len(str(num))
    # remove right
    while num > 0:
        num = num / 10
        if num > 0 and not is_prime(num):
            return False
    return num == 0

def foo():
    last_n_digit_coll = {1: [2, 3, 5, 7]}
    result = {}
    i = 1
    total_left_truncated_prime = 4
    total_right_truncated_prime = 0
    while True:
        for p in last_n_digit_coll[i]:
            for n in [1, 2, 3, 5, 7, 9]:
                num = n*10**i+p

                if is_prime(num):
                    if last_n_digit_coll.get(i+1, None) is None:
                        last_n_digit_coll[i+1] = []
                    last_n_digit_coll[i+1].append(num)

        if last_n_digit_coll.get(i+1, None) is None:
            break

        result[i+1] = [ k for k in last_n_digit_coll[i+1] if is_truncatable_prime(k)]
        total_left_truncated_prime += len(last_n_digit_coll.get(i+1, []))
        total_right_truncated_prime += len(result.get(i+1, []))
        print total_left_truncated_prime, total_right_truncated_prime

        i += 1
    return sum([ sum(i) for i in result.values()] )

def main():

    print foo()

if __name__ == '__main__':
    main()
