import datetime
x = datetime.datetime.now()
movimientos = [[(01, 01, 2004), 123, 500, 'Deposito'],[(01, 01, 2004), 800, 2, 'Extraccion'],[(01, 02, 2004), 124, 600, 'Deposito'],[(01, 02, 2004), 125, 5060, 'Deposito'],[(01, 02, 2004), 123, 8000, 'Extraccion'],[(01, 06, 2004), 123, 500, 'Deposito'],[(01, 01, 2014), 126, 600, 'Extraccion']]

def movimiento(n_cuenta,monto,tipo,movimientos):
  fecha = x.day,x.month,x.year
  movimiento = []
  movimiento.append(fecha)
  movimiento.append(n_cuenta)
  movimiento.append(monto)
  movimiento.append(tipo)
  movimientos.append(movimiento)
  print "Ultimo movimiento: ", x.day,"/",x.month,"/",x.year,". ",tipo," de monto: ", monto, ", al N° de cuenta: ", n_cuenta,". Gracias por su preferencia."

def contar_depositos(movimientos):
  print "Se le pediran los datos de fecha de inicio y fin del periodo donde quiera contar los movimientos."
  desde = raw_input("Ingrese la fecha de inicio del conteo, ejemeplo: dd/mm/aaaa").split("/")
  hasta = raw_input("Ingrese la fecha de fin del conteo, ejemeplo: dd/mm/aaaa").split("/")
  desde_int = tuple([int(i) for i in desde])
  hasta_int = tuple([int(i) for i in desde])
  cuenta = []
  total_depositos = []
  for movimiento in movimientos:
    if desde_int[0]==movimiento[0][0] and desde_int[1]==movimiento[0][1] and desde_int[2]==movimiento[0][2]:
      cuenta.append(movimientos.index(movimiento))
    if hasta_int[2]==movimiento[0][2] and hasta_int[1]==movimiento[0][1] and hasta_int[0]==movimiento[0][0]
      cuenta.append((movimientos.index(movimiento)))
  for i in cuenta:
    if movimiento[3]=='Deposito':
      total_depositos.append(i)
  print "Estan registrados ", len(total_depositos), "depositos en las fechas indicadas."

  def contar_extracciones(movimientos):
  print "Se le pediran los datos de fecha de inicio y fin del periodo donde quiera contar los movimientos."
  desde = raw_input("Ingrese la fecha de inicio del conteo, ejemeplo: dd/mm/aaaa").split("/")
  hasta = raw_input("Ingrese la fecha de fin del conteo, ejemeplo: dd/mm/aaaa").split("/")
  desde_int = tuple([int(i) for i in desde])
  hasta_int = tuple([int(i) for i in desde])
  cuenta = []
  total_extracciones = []
  for movimiento in movimientos:
    if desde_int[0]==movimiento[0][0] and desde_int[1]==movimiento[0][1] and desde_int[2]==movimiento[0][2]:
      cuenta.append(movimientos.index(movimiento))
    if hasta_int[2]==movimiento[0][2] and hasta_int[1]==movimiento[0][1] and hasta_int[0]==movimiento[0][0]
      cuenta.append((movimientos.index(movimiento)))
  for i in cuenta:
    if movimiento[3]=='Extraccion':
      total_extracciones.append(i)
  print "Estan registradas ", len(total_extracciones), "extracciones en las fechas indicadas."

def saldo(movimientos):
  n_cuenta = int(raw_input("Ingrese el N° de cuenta"))
  year = int(raw_input("Ingrese el year"))
  depositos = []
  retiros = []
    for i in movimientos:
      if year==movimiento[0][2] and n_cuenta == movimiento[1] and movimiento[3]=='Deposito':
        depositos.append(movimiento[2])
      elif year==movimiento[0][2] and n_cuenta == movimiento[1] and movimiento[3]=='Extraccion':
        retiros.append(movimiento[2])
  saldo = sum(depositos)-sum(retiros)
  print "El saldo de la cuenta: ",n_cuenta,", en el year ", year, ", es de: ", saldo

def main():
  print "Si realizara un Deposito, ingrese 1. Para una Extraccion, ingrese 2."
  tipo = int(input())
  if tipo == 1:
    tipo = "Deposito"
    n_cuenta = int(raw_input("Ingrese el numero de cuenta"))
    monto = int(raw_input("Ingrese el monto"))
    movimiento(n_cuenta,monto,tipo,movimientos)
  else:
    if tipo == 2:
      tipo = "Extraccion"
      n_cuenta = int(raw_input("Ingrese el numero de cuenta"))
      monto = int(raw_input("Ingrese el monto"))
      movimiento(n_cuenta,monto,tipo,movimientos)
    else:
      main()
