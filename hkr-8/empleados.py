import random

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

empleados = {}
id_empleados = [i for i in range(200,208)]
tareas = ['a','b','c','d','e','f']
for i in range(len(id_empleados)):
  empleados.setdefault(id_empleados[i],[Stack(),0])

def nueva_tarea(id_empleado,tareas,empleados):
  caract_empleado = empleados.get(id_empleado)
  caract_empleado[0].push(random.choice(tareas))
  N_tareas = caract_empleado[0].size()
  empleados[id_empleado] = N_tareas


def comprobar(empleados,id_empleados):
  s = []
  for id_empleado in id_empleados:
    s.append([empleados.get(id_empleado)[1],i])
  s.sort()
  return s[0][1]


for i in range(30):
  nueva_tarea(comprobar(empleados,id_empleados),tareas,empleados)
