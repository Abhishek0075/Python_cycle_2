class Box:
    __length=None
    __breadth=None
    __height=None
    __area=None
    __volume=None
    def __init__(self,*p):
        if(len(p)==1):
            self.__length=p[0]
            self.__breadth=p[0]
            self.__height=p[0]
        elif(len(p)==2):
            self.__length=p[0]
            self.__breadth=p[0]
            self.__height=p[1]
        elif(len(p)==3):
            self.__length=p[0]
            self.__breadth=p[1]
            self.__height=p[2]

    def find_area(self):
        self.__area =2*((self.__length*self.__breadth)+(self.__height*self.__breadth)+(self.__length*self.__height))
        return (self.__area)    
    def find_volume(self):
        self.__volume =self.__length*self.__breadth*self.__height
        return (self.__volume)
    
    def details(self):
        print("--------Details---------")
        print("Lenght  : ",self.__length)
        print("Breadth : ",self.__breadth)
        print("Height  : ",self.__height)
        print("Area    : ",self.find_area())
        print("Volume  : ",self.find_volume())
        print("Ratio : ",self.ratio())
    def ratio(self):
        ratio=self.find_volume()/self.find_area()
        return ratio
def order(*t):
    new_t=[]
    for i in t:
        new_t.append(i.ratio())
    new_t.sort()
    return new_t
a=Box(20)
a.details()
b=Box(30,40)
b.details()
c=Box(20,10,55)
c.details()
t=(a,b,c)
print(order(t))

        