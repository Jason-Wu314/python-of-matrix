import math


# 定義分數的物件
class Fraction:
    """
    這是一個分數的物件，裡面定義了有關分數的相關操作
    """
    def __init__(self, numerator = int, denominator = int):
        a,b = numerator,denominator
        while b != 0:
            a, b = b, a % b
        self.numerator = numerator//a
        self.denominator = denominator//a
        self.fraction = f"{self.numerator}/{self.denominator}"
    
    def __str__(self):
        return self.fraction
    
    def toString(self):
        return self.fraction
    
    def tonumber(self):
        if (self.numerator/self.denominator)%1 != 0:
            return self.numerator/self.denominator
        else:
            return self.numerator//self.denominator
    
    def simplest(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            a, b = b, a % b
        return Fraction(self.numerator//a, self.denominator//a)
    
    def __eq__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() == __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for ==")
        
    def __ge__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() >= __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for >=")
        
    def __gt__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() > __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for >")
    
    def __ne__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() != __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for !=")
    
    def __le__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() <= __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for <=")

    def __lt__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() < __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for <")
    
    def __gt__(self, __value: object):
        if isinstance(__value, Fraction):
            return self.tonumber() > __value.tonumber()
        else:
            raise TypeError("Unsupported operand type for >")
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            self.simplest()
            other.simplest()
            a,b = self.denominator,other.denominator
            while b != 0:
                a, b = b, a % b
            c = (self.denominator * other.denominator)//a
            d = (c//self.denominator)*self.numerator + (c//other.denominator)*other.numerator
            self.numerator = (c//self.denominator)*self.numerator
            other.numerator = (c//other.denominator)*other.numerator
            return Fraction(d,c).simplest()
        elif isinstance(other, int):
            return Fraction(self.numerator + other*self.denominator,self.denominator).simplest()
        else:
            raise TypeError("Unsupported operand type for +")
        
    def __sub__(self, other):
        if isinstance(other, Fraction):
            self.simplest()
            other.simplest()
            a,b = self.denominator,other.denominator
            while b != 0:
                a, b = b, a % b
            c = (self.denominator * other.denominator)//a
            d = (c//self.denominator)*self.numerator - (c//other.denominator)*other.numerator
            self.numerator = (c//self.denominator)*self.numerator
            other.numerator = (c//other.denominator)*other.numerator
            return Fraction(d,c).simplest()
        elif isinstance(other, int):
            return Fraction(self.numerator - other*self.denominator,self.denominator).simplest()
        else:
            raise TypeError("Unsupported operand type for -")
        
    def __mul__(self, other):
        if isinstance(other, Fraction):
            self.simplest()
            other.simplest()
            return Fraction(self.numerator*other.numerator,self.denominator*other.denominator).simplest()
        elif isinstance(other, int):
            return Fraction(self.numerator*other,self.denominator).simplest()
        else:
            raise TypeError("Unsupported operand type for *")
        
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            self.simplest()
            other.simplest()
            other.denominator,other.numerator = other.numerator,other.denominator
            return Fraction(self.numerator*other.numerator,self.denominator*other.denominator).simplest()
        elif isinstance(other, int):
            return Fraction(self.numerator,self.denominator*other).simplest()
        else:
            raise TypeError("Unsupported operand type for /")
    
    def __floordiv__(self, other):
        if isinstance(other, Fraction):
            self.simplest()
            other.simplest()
            other.denominator,other.numerator = other.numerator,other.denominator
            return Fraction(self.numerator*other.numerator,self.denominator*other.denominator).tonumber()
        elif isinstance(other, int):
            return Fraction(self.numerator,self.denominator*other).tonumber()
        else:
            raise TypeError("Unsupported operand type for //")
        
    def __pow__(self, other):
        if isinstance(other, int):
            return Fraction(self.numerator**other,self.denominator**other).simplest()
        else:
            raise TypeError("Unsupported operand type for **")
