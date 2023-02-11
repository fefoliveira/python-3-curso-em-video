"""Crie um código em Python que teste se o site Pudim está acessível pelo computador usado."""

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[31mO site pudim.com.br não está acessível no momento.\033[m')
else:
    print('\033[32mO site pudim.com.br está acessível no momento.\033[m')
    print(site.read())
