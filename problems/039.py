#! /usr/bin/python

def count_solution(p):
    lower_bound = p / 3
    upper_bound = p / 2
    count = 0
    for c in range(lower_bound, upper_bound):
        b_lower_bound = (p - c)/2
        for b in range(b_lower_bound, c):
            a = p - c - b
            if c**2 == a**2 + b**2:
                count += 1
    return count

def foo():
    max_count = 0
    best_p = 0
    for p in range(3, 1000+1):
        count = count_solution(p)
        if max_count < count:
            max_count = count
            best_p = p
    return best_p

def main():
    print foo()

if __name__ == '__main__':
    main()
