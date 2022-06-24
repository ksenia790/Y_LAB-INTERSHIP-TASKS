'''Задача №1.
Написать метод domain_name, который вернет домен из url адреса.'''

from urllib.parse import urlparse


url1: str = "http://github.com/carbonfive/raygun"
url2: str = "http://www.zombie-bites.com"         
url3: str = "https://www.cnet.com" 
url4: str = "www.xakep.ru"


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

print(domain_name(url3))


''' Задача №2. 
Написать метод int32_to_ip, который принимает на вход 32-битное целое число
(integer) и возвращает строковое представление его в виде IPv4-адреса.'''


num1: int = 2154959208
num2 = 32
num3 = 0
int32: str = "{:032b}".format(num1)


def int32_to_ip(int32: str) -> str:
    ip_addr = [str(int(int32[i:i+8], 2)) for i in range(0,32,8)]
    result = '.'.join(ip_addr)
    return result

print(int32_to_ip(int32))


