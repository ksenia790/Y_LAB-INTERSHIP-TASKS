# Задача №1.
# Написать метод domain_name, который вернет домен из url адреса.
from urllib.parse import urlparse


url1 = "http://github.com/carbonfive/raygun"
url2 = "http://www.zombie-bites.com"         
url3 = "https://www.cnet.com" 
url4 = "www.xakep.ru"


def domain_name(url):
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