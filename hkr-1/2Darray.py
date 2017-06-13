import sys
import string

arr = []

def revisar_por_fila(arr,n):
  sum_partial = []
  s=0
  for i in range(len(arr)/2):
    if arr[n][s]!=0 and arr[n][s+1]!=0 and arr[n][s+2]!=0:
      sum_temp = arr[n][s] + arr[n][s+1] + arr[n][s+2] + arr[n+1][s+1] + arr[n+2][s] + arr[n+2][s+1] + arr[n+2][s+2]
      sum_partial.append(sum_temp)
      s = s+1
    else:
      s = s+1
  return sum_partial

for arr_i in xrange(6): #Falta genralizar para matrices de mayor tamaño
    arr_temp = map(int,raw_input("Introduce la matriz").strip().split(' '))
    arr.append(arr_temp)

sum = []

for i in range(0,5):
  s = revisar_por_fila(arr,i)
  sum.append(s)

print max(sum)[0]

#hay una fomrma de contar las lineas de código que se introducen como entrada?
