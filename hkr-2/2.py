#!/bin/python
#Valeria Montserrat Maya
#camelCase

import sys


s = raw_input().strip()
suma = 1
def contar(S,suma):
    for i in range(len(s)):
        if s[i].isupper()==True:
            suma = suma + 1
    print suma
contar(s,suma)
