#!/bin/python
#Valeria Montserrat Maya
#Caesar Cipher

import sys

n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
for i in s:
    new_key = ord(i)+k
    if ord(i)>=65 and ord(i)<=90:
        if new_key<=90:
            s = s.replace(i,chr(new_key))
        else:
            nk = new_key
            while nk>90:
                nk = nk - 26
            s = s.replace(i,chr(nk))
    else:
        if ord(i)>=97 and ord(i)<=122:
            if new_key<=122:
                s = s.replace(i,chr(new_key))
            else:
                nk = new_key
                while nk>122:
                    nk = nk - 26
                s = s.replace(i,chr(nk))
print s
