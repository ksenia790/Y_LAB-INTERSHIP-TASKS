'''Задача №1.
Написать метод domain_name, который вернет домен из url адреса.'''


from urllib.parse import urlparse


url_1: str = "http://github.com/carbonfive/raygun"
url_2: str = "http://www.zombie-bites.com"         
url_3: str = "https://www.cnet.com" 
url_4: str = "www.xakep.ru"


def domain_name(url: str) -> str:
    if "http" in url or "https" in url:
        result = urlparse(url).netloc
        if url.count('.') > 1:
            dom_name  = ''.join(result.split('.')[1])
            return dom_name
        else:
            dom_name = ''.join(result.split('.')[0])
            return dom_name
    else:
        dom_name = ''.join(url.split('.')[1])
        return dom_name

print(domain_name(url_3))


''' Задача №2. 
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса.'''


num_1: int = 2154959208
num_2: int = 32
num_3: int = 0
int32: str = "{:032b}".format(num_1)


def int32_to_ip(int32: str) -> str:
    ip_addr = [str(int(int32[i:i+8], 2)) for i in range(0,32,8)]
    result = '.'.join(ip_addr)
    return result

print(int32_to_ip(int32))


'''Задача №3. 
Написать метод zeros, который принимает на вход целое число (integer) и
возвращает количество конечных нулей в факториале (N! = 1 * 2 * 3 * ... * N) 
заданного числа'''


n: int = 10 #int(input())

def zeros(n: int) -> int:
    if (n < 0):
        return -1
 
    count = 0
    while(n >= 5):
        n //= 5
        count += n
    return count

print(zeros(n))


'''Задача №4. 
Написать метод bananas, который принимает на вход строку и
возвращает количество слов «banana» в строке.'''




'''Задача №5.
Написать метод count_find_num, который принимает на вход 
список простых множителей (primesL) и целое число,
предел (limit), после чего попробуйте сгенерировать по порядку все числа.
Меньшие значения предела, которые имеют все и только простые 
множители простых чисел primesL.'''

import itertools
import math


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