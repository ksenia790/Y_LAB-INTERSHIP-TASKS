'''Задача №1.
Написать метод domain_name, который вернет домен из url адреса.'''
import re


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


''' Задача №2. 
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса.'''


num: int = 32


def int32_to_ip(num: int) -> str:
    int32: str = "{:032b}".format(num)
    ip_addr = [str(int(int32[i:i+8], 2)) for i in range(0,32,8)]
    result = '.'.join(ip_addr)
    return result

print(int32_to_ip(num))


'''Задача №3. 
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) 
заданного числа'''


n: int = 10 #int(input())


def zeros(n: int) -> int:
    count = 0
    while(n >= 5):
        n //= 5
        count += n
    return count

print(zeros(n))


'''Задача №4. 
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.'''


from itertools import combinations


s = 'bbanananas'


def bananas(s):
    result = []
    for i in combinations(range(len(s)), len(s)-6):
        x = list(s)
        for j in i:
            x[j] = '-'
        x = ''.join(x)
        if x.replace('-', '') == 'banana':
            result.append(x)
    return result

print(bananas(s))

'''Задача №5.
Написать метод count_find_num, который принимает на вход 
список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые 
множители простых чисел primesL.'''

import itertools
import math


primesL: list = [2, 5, 7]
limit: int = 500


def count_find_num(primesL: list, limit: int) -> list:
    result = []
    for i in range(len(primesL), 30):
        for v in itertools.combinations_with_replacement(primesL, i):
            if set(primesL) == set(v):
                num = math.prod(v)
                if num <= limit:
                    result.append(num)
    if len(result) == 0:
        return []
    else:
        return [len(result), max(result)]

print(count_find_num(primesL, limit))
