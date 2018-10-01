import math
import random
def check_prime(num, primes):
    for i in primes:
        if num % i == 0:
            return False
    return True

def get_primes(total_primes):
    primes = [2]
    i = 2
    j = 3
    while i < total_primes:
        is_prime = check_prime(j, primes)
        if is_prime:
            primes.append(j)
            i += 1
        j += 1
    return primes

def get_suffix(num, p):
    possible_values = []
    for i in range(1, 10):
        if (num * 10 + i) % p == 0:
            possible_values.append(i)
    if len(possible_values) == 0:
        return -1
    else:
        return possible_values

'''
def get_number(primes, init):
    for p in primes:
        num = int(init[-2:])
        suffix = get_suffix(num, p)
        print(p, num, suffix)
        init += str(suffix)
    return init
'''

def get_number(primes, init):
    if len(primes) == 0:
        return init
    p = primes[0]
    num = int(init[-2:])
    suffixes = get_suffix(num, p)
    if suffixes == -1:
        return -1
    else:
        for suffix in suffixes:
            init_ = get_number(primes[1:], init + str(suffix))
            if init_ != -1:
                return init_
    return -1


def main():
    n = int(input('Write total number of digits\n'))
    primes = get_primes(n - 2)
    num = -1
    i = 0
    for i in range(5000):
        print('Number of iterations:', i + 1)
        init = str(i * 2)
        pad = 4 - len(init)
        init = '0' * pad + init
        num = get_number(primes[1:], init)
        if num != -1:
            break
    if num == -1:
        print('Sorry there is no possible solution for', n, 'digits')
    else:
        print('Number is :', num)
    

if __name__ == '__main__':
    main()
