#Q.1. Create a class animal and tiger and using inheritance method to solve it.
class animal:
    def animal_attribute(self):
        print("Animal")
class tiger(animal):
    pass
a=tiger()
a.animal_attribute()

#Q.2.What will be the output of the above code.
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())
     #output=A B
            #A B
#Q.3.create acop and mission class and using inheritance method for mission details.

class cop:
    def __init__(self,work,name,age,desigation):
        self.name=name
        self.age=age
        self.work=work
        self.desigation=desigation
    def getdisplay(self):
        print(self.name,self.age,self.work,self.desigation)
    def update(self,name,work,age,desigation):
        self.name=name
        self.age=age
        self.work=work
        self.desigation=desigation
class mission(cop) :
    def add_mission_details(self,msn):
        self.mission=msn
        print("mission is",self.mission)
c=mission("tom",18,"investigation","mission impossible")
c.getdisplay()
c.update("jerry",18,"detective","searching tom")
c.getdisplay()
c.add_mission_details("success")
#Q.4. create a shape class and initialize it area of rectangle and square.
class shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        print("area =",self.length*self.breadth)
class rec(shape):
    def rectangle(self):
        pass
r=rec(5,9)
r.area()
class squ (shape):
    def square(self):
        pass
s=squ(6,6)
s.area()
