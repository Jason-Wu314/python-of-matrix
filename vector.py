import math
from Fraction import Fraction



class Vector:
    """
    這是一個向量的物件，裡面定義了有關向量的相關操作
    """
    def __init__(self, *matrix):
        if type(matrix[0]) == list:
            self.vector = matrix[0]
        else:
            self.vector = list(matrix)
        self.dimension = len(self.vector)
        self.length = self.len()
    
    def __str__(self):
        a = []
        for i in self.vector:
            if isinstance(i,Fraction): 
                a.append(i.toString())
            else :
                a.append(i)
            # print(a)
        return str(a)
    
    def len(self):
        a = self.vector
        b = 0
        for i in a:
            b = (i**2) + b
        if type(b) == Fraction:
            c = Fraction(round(math.sqrt(b.numerator),2),round(math.sqrt(b.numerator),2))
            return c
        return math.sqrt(b)
    
    def __add__(self, other):
        if isinstance(other, Vector) and self.dimension == other.dimension:
            a = self.vector
            b = self.vector
            c = [(a[i]+b[i])  for i in range(self.dimension)]
            return c
        elif not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for +")
        elif not self.dimension == other.dimension:
            print("Error: 向量相加兩維度要相同")
            exit()

    def __sub__(self, other):
        if isinstance(other, Vector) and self.dimension == other.dimension:
            a = self.vector
            b = self.vector
            c = [(a[i]-b[i])  for i in range(self.dimension)]
            return c
        elif not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for +")
        elif not self.dimension == other.dimension:
            print("Error: 向量相減兩維度要相同")
            exit()


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            a = self.vector
            b = [i*other for i in a]
            return b
        elif isinstance(other, Fraction):
            a = self.vector
            b = [other*i for i in a]
            return b
        elif not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for *")


    # 做向量內積 a dot b
    def dot(self,other): return self**other
    def __pow__(self, other):
        if isinstance(other, Vector) and self.dimension == other.dimension:
            a = self.vector
            b = other.vector
            final = 0
            for i in range(len(a)):
                final += a[i]*b[i]
            return final
        elif not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for *")
        elif not self.dimension == other.dimension:
            print("Error: 向量做內積兩維度要相同")
            exit()


    # 做向量外積 a cross b
    def cross(self,other): return self^other
    def __xor__(self, other):
        def det(array = []):
            a = int(math.sqrt(len(array)))
            if a==1: return array[0]
            b = 0
            for i in range(a):
                downarry = []
                for j in range(a,len(array)): 
                    if (j % a != i): 
                        downarry.append(array[j])
                b += (1 if i%2==0 else -1) * array[i] * det(downarry)
            return b
        if isinstance(other, Vector) and self.dimension == other.dimension == 3:
            a = self.vector
            b = other.vector
            a=list(a+[a[0],a[1]])[1:]
            b=list(b+[b[0],b[1]])[1:]
            c=[det([a[0],a[1],b[0],b[1]]),det([a[1],a[2],b[1],b[2]]),det([a[2],a[3],b[2],b[3]])]
            return Vector(c)
        elif not isinstance(other, Vector):
            raise TypeError("Unsupported operand type for **")
        elif not self.dimension == other.dimension == 3:
            print("Error: 向量cross兩向量維度皆須為三維向量")
            exit()


    # 取得向量a在b上的正射影向量 a>>b
    def orthoprojection(self, other): return self >> other
    def __rshift__(self, other):
        if isinstance(other, Vector):
            a = round((self**other)/other.len(),2)
            if a % 1 != 0: c = Vector(other*a)
            else : c = Vector(other*int(a))
            return c
        else:
            raise TypeError("Unsupported operand type for >>")
        

    #向量相等==
    def Equl(self, other): return self == other
    def __eq__(self, other):
        if isinstance(other, Vector):
            a = self.vector
            b = other.vector
            if len(a) == len(b):
                for i in range(len(a)):
                    if a[i]!=b[i]:
                        return False
                return True
            else:
                print("Error: 向量相等兩維度要相同")
        else:
            raise TypeError("Unsupported operand type for ==")


    #同向向量 a>=b （兩向量平行）
    def isParallel(self, other: object): return self >= other
    def isSameDirection(self, other: object): return self >= other
    def __ge__(self, other: object):
        if isinstance(other, Vector):
            a = self.vector
            b = other.vector
            if len(a) == len(b):
                c = a[0]/b[0]
                if c < 0: return False
                for i in range(len(a)):
                    if a[i]/b[i] != c: return False
                return True
            else:
                print("Error: 向量相等兩維度要相同")
        else:
            raise TypeError("Unsupported operand type for >=")


    #反向向量 a<=b （兩向量平行但方向相反）
    def isReverse(self, other: object): return self <= other
    def __le__(self, other: object):
        if isinstance(other, Vector):
            a = self.vector
            b = other.vector
            if len(a) == len(b):
                c = a[0]/b[0]
                if c > 0: return False
                for i in range(len(a)):
                    if a[i]/b[i] != c: return False
                return True
            else:
                print("Error: 向量相等兩維度要相同")
        else:
            raise TypeError("Unsupported operand type for >=")


    #向量不相等!=
    def notEqual(self, other): return self != other
    def __ne__(self, other):
        if isinstance(other, Vector):
            a = self.vector
            b = other.vector
            if len(a) == len(b):
                for i in range(len(a)):
                    if a[i]==b[i]:
                        return False
                return True
            else:
                print("Error: 向量不相等兩維度要相同")
        else:
            raise TypeError("Unsupported operand type for !=")


    #向量垂直a|b
    def isVertical(self, other): return self | other
    def __or__(self, other):
        if isinstance(other, Vector):
            a = self.vector
            b = other.vector
            if len(a) == len(b):
                return self**other == 0
            else:
                print("Error: 向量垂直兩維度要相同")
        else:
            raise TypeError("Unsupported operand type for |")


    #回傳x,y,z,w
    def __getattribute__(self, name):
        if name == 'x':
            return self.vector[0]
        elif name == 'y':
            try:
                return self.vector[1]
            except:
                raise IndexError("This vector only has one dimension.")
        elif name == 'z':
            try:
                return self.vector[2]
            except:
                raise IndexError("This vector only has two dimension.")
        elif name == 'w':
            try:
                return self.vector[3]
            except:
                raise IndexError("This vector only has three dimension.")

        return object.__getattribute__(self, name)


