#! /usr/bin/python

def has_duplicate_number(num_str):
    arr = [0 for i in range(10)]
    for ch in num_str:
        idx = ord(ch) - ord('0')
        arr[idx] += 1
        if arr[idx] > 1:
            return True
    return False

def expand_list(candidate_coll, prime_num):
    result = []
    for i in candidate_coll:
        for n in '0123456789':
            if i.count(n) == 0:
                num = int(n+i[:2])
                if num % prime_num == 0:
                    result.append(n+i)
    return result
def foo():
    divided_by_17 = []
    for i in range(10, 1000):
        if i % 17 == 0:
            s = str(i)
            if len(s) < 3:
                s = '0'+s
            if not has_duplicate_number(s):
                divided_by_17.append(s)
    result = divided_by_17

    for prime_num in [13, 11, 7, 5, 3, 2, 1]:
        result = expand_list(result, prime_num)
    print result
    return sum([ int(i) for i in result])

def main():
    print foo()

if __name__ == '__main__':
    main()
