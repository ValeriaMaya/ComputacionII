import math as m

class point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.initial = [x,y]

  def move(self,x1,y1):
    self.x = x1
    self.y = y1
    print "The point has moved to x=",self.x,", y=",self.y

  def reset(self):
    self.x = self.initial[0]
    self.y = self.initial[1]
    print "The point has moved to the their initial values x=",self.x,", y=",self.y

  def calculate_distance(self,otherPoint):
    distance = m.sqrt(m.pow((self.x-otherPoint.x),2)+m.pow((self.y-otherPoint.y),2))
    print distance

entrada = raw_input('').split()
n_puntos = entrada.pop(0)
points = []
for i in range(len(entrada)/2):
  new_point = point(int(entrada.pop(0)),int(entrada.pop(0)))
  points.append(new_point)


points[0].calculate_distance(points[1])
