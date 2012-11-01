#! /usr/bin/python

def find_all_coin_combination(coin_coll, end, target, cache):
    result = 0
    if target == 0:
        return 1

    if end == 0:
        if target >= coin_coll[end] and target % coin_coll[end] == 0:
            return 1
        else:
            return 0

    if (end, target) in cache:
        return cache[(end, target)]

    val = coin_coll[end]
    while target >= val:
        result += find_all_coin_combination(coin_coll, end-1, target - val, cache)
        val += coin_coll[end]

    cache[(end, target)] = result + find_all_coin_combination(coin_coll, end-1, target, cache)
    return cache[(end, target)]

def foo():
    coin_coll = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    coin_combination_cache = {}
    return find_all_coin_combination(coin_coll, len(coin_coll)-1, target, coin_combination_cache)

def main():
    print foo()

if __name__ == '__main__':
    main()
