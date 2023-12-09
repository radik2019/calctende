
class Integer:

    @classmethod
    def type_checker(cls, value):
        if type(value) != int:
            raise TypeError(" Deve essere un integer")

    def __set_name__(self, owner, name):
        print("__set_name__")
        self.name = '_' + name
    def __get__(self, instance, owner):
        print("__get__")
        return instance.__dict[self.name]
    def __set__(self, instance, value):
        print("__set__")
        instance.__dict__[self.name] = value


class Rectangle:
    
    def __repr__(self):
        s = f'altezza         = {self.h}\n'\
        f'lato corto      = {self.c_corto}\n'\
        f'lato lungo      = {self.c_lungo}\n'\
        f'ipotenusa corta = {self.ipotenusa_corta}\n'\
        f'ipotenusa lunga = {self.ipotenusa_lunga}\n'
        return s
    
    def __init__(self, h, c_corto, c_lungo):
        self.h = h
        self.c_corto = c_corto
        self.c_lungo = c_lungo
        self.ipotenusa_corta = self.pitagora(self.h, self.c_corto)
        self.ipotenusa_lunga = self.pitagora(self.h, self.c_lungo)
    
    @staticmethod
    def pitagora(cateta1, cateta2):
        return (cateta1 ** 2 + cateta2 ** 2) ** 0.5
    
    @staticmethod
    def percentage(intero, percentuale):
        if  percentuale > intero:
            return (percentuale * 100 / intero) - 100
        else:
            return percentuale * 100 / intero
        
    def due_ipotenuse(self):
        return self.pitagora(self.h, self.c_corto), self.pitagora(self.h, self.c_lungo)
    
    def increment_percent(self, incr):
        self.h += incr
        ipc, ipl = self.due_ipotenuse()
        print(f"{round(self.percentage(self.ipotenusa_corta, ipc), 7)}".ljust( 14, " "), end="")
        print(f"{round(self.percentage(self.ipotenusa_lunga, ipl), 7)}".ljust( 14, " "))
        self.ipotenusa_lunga = ipl
        self.ipotenusa_corta = ipc




