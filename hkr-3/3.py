#Valeria Montserrat Maya
#Sumatoria

a = raw_input().split()
b = []
for i in range(len(a)):
    b.append(int(a[i]))
n_columnas = 3
n_filas = 4
bp = []
ic = 0
fc = n_columnas
f = n_filas
while f!=0:
    c = b[ic:fc]
    bp.append(c)
    fc = fc + n_columnas
    ic = ic + n_columnas
    f = f -1
l_suma = []
for n in range(n_columnas):
    s = [i[n] for i in bp]
    suma = sum(s)
    l_suma.append(suma)
print l_suma[0],l_suma[1],l_suma[2]
