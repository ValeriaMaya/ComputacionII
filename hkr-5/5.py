#Valeria Montserrat Maya
#The Power Sum

import math

x = int(raw_input())
n = int(raw_input())
mx = int(math.pow(x,(1/float(n))))
e = [math.pow(i,n) for i in range(mx+1)]
s = int(sum(e)/x)
print s
