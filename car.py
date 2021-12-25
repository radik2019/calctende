<<<<<<< HEAD
=======


import time
import random
class Employe:
    USERS = 0
    def __new__(cls, *args):
        cls.USERS += 1
        print(f"aggiunta un instanza {cls.__name__} e sono rimasti {cls.USERS}")
        return object.__new__(cls)
    def __del__(self):
        self.__class__.USERS -= 1
        print(f'e stato eliminata l`instanza {self.__class__.__name__} sono rimaste {self.__class__.USERS}')
    def pull(self):

        self.weight += random.randint(3, 40)

        
class Camionista(Employe):
    
    @classmethod
    def gas(cls):
        print(f"  {cls.__name__}  sto corendo!")
        
class Smorzo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @classmethod
    def gas(cls):
        print(f"chiamo dalla classe {cls.__name__}")
    
    
class Cartongessista(Smorzo, Camionista):
    def __init__(self, weight, number, x, y):
        super().__init__(x, y)
        self.weight = weight
        self.number = number
        
    def work(self):
        return ("monta il cartongesso")
        
    def pop(self) -> None:
        self.number += random.randint(3, 40)
        
    def run(self):
        if self.weight == self.number:
            super().gas()
            self.number += 5
        if self.weight < self.number:
            self.pull()
            print("*  pulled")
        else:
            self.pop()
            print(" poped")
#         print("   ", self.weight, self.number)
        



df = Cartongessista(23, 45, 5, 8)

df1 = Cartongessista(23, 45, 5, 8)
cm = Camionista()
cm2 = Camionista()
del df1
df2 = Cartongessista(23, 45, 5, 8)
cm3 = Camionista()

cm4 = Camionista()
df3 = Cartongessista(23, 45, 5, 8)
cm5 = Camionista()
df4 = Cartongessista(23, 45, 5, 8)

print(df4.USERS)
print(cm4.USERS)

>>>>>>> origin/NewOOP
