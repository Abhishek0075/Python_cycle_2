class Shapes:
  _volume=None
  _area=None
  def put_area(self):
      print("Area   : ",self._area)
  def put_volume(self):
    print("Volume : ",self._volume)
class sphere(Shapes):
  __radius=None
  def __init__(self,r):
    self.__radius=r
  def cal_area(self):
    self._area=(88/7)*self.__radius**2
  def cal_volume(self):
    self._volume=(4/3)*((22/7)*(self.__radius**3))
class cylinder(Shapes):
  __radius=None
  __height=None
  def __init__(self,r,h):
    self.__radius=r
    self.__height=h
  def cal_area(self):
    self._area=(44/7)*self.__radius*self.__height+44/7*(self.__radius**2)
  def cal_volume(self):
    self._volume=(22/7)*(self.__radius**2)*self.__height


print("Enter dimensions of cylinder : ")
a=int(input(">> Enter the radius of cylinder : "))
b=int(input(">> Enter the height of cylinder : "))
print("Enter dimensions of sphere : ")
c=int(input(">> Enter the radius of sphere : "))
c1=cylinder(a,b)
s1=sphere(c)
s1.cal_area()
c1.cal_area()
s1.cal_volume()
c1.cal_volume()
print("{:s}\n{:s}".format("The area and volume of Sphere : ",len("The area and volume of Sphere : ")*"-"))
s1.put_area()
s1.put_volume()
print("")
print("{:s}\n{:s}".format("The area and volume of Cylinder : ",len("The area and volume of Cylinder : ")*"-"))
c1.put_area()
c1.put_volume()
