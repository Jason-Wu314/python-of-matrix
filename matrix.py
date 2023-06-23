import math
from Fraction import Fraction
from vector import Vector



def TransTo2DArray(List = list,column = None,row = None):
    matrix = List.copy()
    isOneDim = False
    for i in List:
        if not isinstance(i, list):
            isOneDim = True
            break
    if not isOneDim: raise TypeError("It is not an 1D array.")
    if column is None: raise TypeError("Can not transfer to 2DArray because column is Null")
    if not isinstance(column, int): raise TypeError("column must be an integer.")
    if row is None: row = len(matrix)/column
    if row%1!=0: raise TypeError("Can not transfer to 2DArray")
    if len(matrix) != column * row : raise TypeError("Can not transfer to 2DArray")
    c = column
    r = int(row)
    DownMatrix = []
    for j in range(c):
        e = []
        for k in range(r):
            e.append(matrix[j*r+k])
        DownMatrix.append(e)
    matrix = DownMatrix
    return matrix



class Matrix:
    '''
這是一個矩陣的物件，裡面定義了有關矩陣的相關操作，你可以調用doc()來知道有什麼功能，輸入一個二階陣列，這個物件可以幫你轉成矩陣\n
This is a matrix object that defines various operations related to matrices. You can use the "doc()" function 
to know its functionalities. By inputting a 2D array, this object can assist you in converting it into a matrix.\n
self.matrix：矩陣陣列內容  (Matrix array content.)\n
self.isPhalanx：是否為方陣  (Is it a square matrix)\n
self.column : 列數（直） (Number of column (vertical).)\n
self.row ：行數（橫） (Number of row (horizontal).)
    '''

    # self.matrix：矩陣陣列內容
    # self.isPhalanx：是否為方陣
    # self.column : 列數（直）
    # self.row ：行數（橫）


    # 初始化矩陣-------------------------------------------------------  


    def __init__(self, Matrix = object, column = int,row = int):
        _matrix = list
        _isPhalanx = bool
        _column = int
        _row = int
        isOneDim = False
        if isinstance(Matrix, list):
            matrix = list(Matrix.copy())
            del Matrix
            for i in matrix:
                if not isinstance(i, list):
                    isOneDim = True
                    break
                for j in i:
                    if isinstance(j, list):
                        raise TypeError("the given array is not a 2D array, it cannot be considered as a matrix. A matrix should have two dimensions, with rows and columns.")
            if isOneDim :
                matrix = TransTo2DArray(matrix,column,row)
            b = len(matrix[0])
            for i in matrix:
                if len(i) != b:
                    raise IndexError("This array is not in matrix form as the number of elements in each row is not equal.")
            a = len(matrix) == len(matrix[0])
            _matrix = matrix
            _isPhalanx = a
            _column = len(matrix)
            _row = len(matrix[0])
        elif isinstance(Matrix, str):
            matrix = str(Matrix)
            del Matrix
            # 回傳乘法單位元素 I      # 回傳零矩陣 O
            if matrix[0] == 'I' or matrix[0] == 'O':
                try:
                    a = int(matrix[1:])
                except:
                    if matrix[0] == 'I':
                        raise ValueError(f"Error: 製作乘法單位元素格式不符 \"{matrix[0]}x\" => x是你要的階數")
                    elif matrix[0] == 'O':
                        raise ValueError(f"Error: 製作加法單位元素格式不符 \"{matrix[0]}x\" => x是你要的階數")
                if a < 1:
                    raise ValueError("You can not make a Matrix which dimension is zero.")
                        
                c = [[0 for i in range(a)] for i in range(a)]
                if matrix[0] == 'I':
                    for i in range(a):
                        c[i][i] = 1
                _matrix = c
                _isPhalanx = True
                _column = a
                _row = a
            
        self._matrix = _matrix
        self._isPhalanx = _isPhalanx
        self._column = _column
        self._row = _row


    # ---------------------------------------------------------------  
    
    

    # 管理權限------------------------------------------------------

    @property
    def isPhalanx(self):
        return self._isPhalanx
    @isPhalanx.setter
    def isPhalanx(self, value):
        raise AttributeError("Cannot modify isPhalanx directly")
    @isPhalanx.setter
    def __isPhalanx(self, value = bool):
        self._isPhalanx = value
    
    
    @property
    def column(self):
        return self._column
    @column.setter
    def column(self, value):
        raise AttributeError("Cannot modify isPhalanx directly")
    @column.setter
    def __column(self, value = int):
        self._column = value
    
    
    @property
    def row(self):
        return self._row
    @row.setter
    def row(self, value):
        raise AttributeError("Cannot modify isPhalanx directly")
    @row.setter
    def __row(self, value = int):
        self._row = value
        
    
    @property
    def matrix(self):
        return self._matrix
    @matrix.setter
    def matrix(self, value):
        self._matrix = value
        self.ReNewObjectData()
    
    
    
    # 重新更改元素值
    def ReNewObjectData(self):
        a = len(self._matrix) == len(self._matrix[0])
        self._isPhalanx = a
        self._column = self.length()[0]
        self._row = self.length()[1]
        
    # ---------------------------------------------------------------  
    
    
    
    # 定義物件行為-----------------------------------------------------   
    
    # 定義的迭代行為
    def __iter__(self):
        return iter(self.matrix)


    # 取得矩陣的項目
    def __getitem__(self, index):
        return self.matrix[index]


    # 矩陣加法+
    def __add__(self, other): 
        Self,Other = self.copy(),other.copy()
        Self.Addition(Other)
        return Self


    # 矩陣減法-
    def __sub__(self, other): 
        '''
        執行矩陣的減法運算\nPerform matrix Subtract operation.
        '''
        Self,Other = self.copy(),other.copy()
        Self.Subtract(Other)
        return Self


    # 矩陣乘法*
    def __mul__(self,other):
        '''
        執行矩陣的乘法運算\nPerform matrix multiply operation.
        '''
        Self = self.copy()
        Self.Multiply(other)
        return Self


    # 矩陣的次方**
    def __pow__(self, other):
        '''
        回傳此矩陣的n次方(A^n)，僅限方陣可執行本操作\n
        Return the n-th power of the given square matrix (A^n). 
        This operation is limited to square matrices only.
        '''
        Self = self.copy()
        Self.pow(other)
        return Self    


    # 合併矩陣（製作增廣矩陣）A|B
    def __or__(self, other):
        '''
        合併矩陣（製作增廣矩陣），你可以把兩個矩陣做合併([a|b])，可以簡寫成a = a|b，其中a,b是矩陣且兩個的列數相等\n
        Combine matrices (creating an augmented matrix), you can merge two matrices ([a|b]) by using the shorthand 
        notation a = a|b, where a and b are matrices with equal number of columns.
        '''
        Self,Other = self.copy(), other.copy()
        Self.append(Other)
        return Self


    # 矩陣功能速記
    def __xor__(self, other):
        '''
        次方速記法 Exponentiation shorthand notation.\n
        A^T:回傳轉置矩陣 Return the transpose matrix.\n
        A^n (n⋲int):回傳此矩陣的n次方 Return the n-th power of the matrix.
        '''
        if other == 'T':
            return self.T()
        elif isinstance(other, int):
            return self**other
        else:
            raise TypeError("Unsupported operand type for ^")


    # 輸出矩陣
    def __str__(self):
        '''
        輸出出一個整齊的矩陣字串\n
        Output a formatted matrix string.
        '''
        string = self.toString()
        return string


    # 矩陣相等
    def __eq__(self, other):
        return self.Equal(other)
    
    
    # ---------------------------------------------------------------   
    
    
    
    
    
    # 定義物件好用的功能的簡寫-------------------------------------------
    
    
    # 複製物件
    def copy(self):
        matrix = self.matrix.copy()
        return Matrix(matrix)


    # 輸出矩陣
    def print(self): 
        '''
        輸出出一個整齊的矩陣字串\n
        Output a formatted matrix string.
        '''
        print(self.toString())


    # 回傳轉置矩陣 A^T
    def T(self):
        '''
        回傳此矩陣的轉置矩陣\nReturn the transpose matrix of the given matrix.
        '''
        Self = self.copy()
        Self.Transpose()
        return Self


    # ---------------------------------------------------------------    



    # 轉換矩陣成陣列
    def toList(self,dimension = 2):
        if dimension == 2:
            return self.matrix
        elif dimension == 1:
            List = self.matrix.copy()
            List1 = []
            for i in List :
                List1 = List1 + i
            return List1
        else:
            raise TypeError("Unsupported transfer to other dimension.")   


    # 矩陣轉成整齊字串
    def toString(self):
        '''
        輸出出一個整齊的矩陣字串\n
        Output a formatted matrix string.
        '''
        matrix = self.copy()
        for i in range(matrix.column):
            for j in range(matrix.row):
                if matrix.matrix[i][j] % 1 != 0:
                    matrix.matrix[i][j] = "≑" + str(round(matrix.matrix[i][j], 4))
                    
        b = 0
        for i in matrix:
            for j in i:
                if len(str(j)) >= b:
                    b = len(str(j))
        n=0
        output = ""
        for i in matrix:

            if matrix.column == 1:
                output += "[ "
            elif n == 0:
                output += "⎡ "
            elif n==matrix.column-1:
                output += "⎣ "
            else:
                output += "⎢ "

            for j in i:
                c = str(j)
                if c[0] == "≑" and len(c) < b:
                    c = c[1:]
                    while len(c) != b-1:
                        c = " " + c
                    c = "≑"+c
                elif len(c) < b:
                    while len(c) != b:
                        c = " " + c
                output += (c + ' ')
                

            if matrix.column == 1:
                output += "]\n"
            elif n == 0:
                output += "⎤\n"
            elif n==matrix.column-1:
                output += "⎦\n"
            else:
                output += "⎥\n"
            n+=1

        output = output[:-1]
        return output
    

    # 輸出矩陣的階數
    def length(self):
        '''
        計算矩陣的階數，回傳一個陣列 [m, n]，其中 m 為矩陣的列數（直），n為矩陣的行數（橫）\n
        Calculate the rank of the matrix and return an array [m, n],
        where m represents the number of rows (vertical) in the matrix
        and n represents the number of columns (horizontal).
        '''
        return [len(self.matrix),len(self.matrix[0])]


    #輸出方陣的值 |a|
    def det(self):
        '''
        計算此方陣的行列式值，僅限方陣可以使用\n
        Calculate the determinant of this square matrix. 
        Limited to square matrices only.
        '''
        if self.isPhalanx:
            array = self.toList(1)
            a = int(math.sqrt(len(array)))
            if a==1: 
                if array[0]%1 == 0:
                    return int(array[0])
                else:
                    return float(array[0])
            b = 0
            for i in range(a):
                d = []
                DownMatrix = []
                for j in range(a,len(array)): 
                    if (j % a != i): 
                        d.append(array[j])
                        
                sd = int(math.sqrt(len(d)))
                DownMatrix = TransTo2DArray(d,sd,sd)
                if i%2==0 :
                    b += array[i] * Matrix(DownMatrix).det()
                else:
                    b -= array[i] * Matrix(DownMatrix).det()
            if b%1 == 0:
                return int(b)
            else:
                return float(b)
        else:
            raise IndexError("This matrix is not a square matrix, so it is not possible to calculate its determinant.")


    # 矩陣加法
    def Addition(self, other):
        '''
        執行矩陣的加法運算（直接作用於原本的矩陣）\n
        Perform matrix addition operation.
        (Apply the addition operation directly to the original matrix.)
        '''
        if isinstance(other, Matrix):
            Self,Other = self.copy(),other.copy()
            m,n = Self.length()
            if Self.length() == Other.length():
                c = []
                for i in range(m):
                    d = []
                    for j in range(n):
                        d.append((Self[i][j]+Other[i][j]))
                    c.append(d)
                Return = Matrix(c)
                self.matrix = Return.matrix.copy()
            else:
                raise IndexError("Two Matrix can not do subtraction, two Matrix.length unequal")
        else:
            raise TypeError("Unsupported operand type for +")


    # 矩陣減法
    def Subtract(self, other):
        '''
        執行矩陣的減法運算（直接作用於原本的矩陣）\n
        Perform matrix Subtract operation.
        (Apply the Subtract operation directly to the original matrix.)
        '''
        if isinstance(other, Matrix):
            Self,Other = self.copy(),other.copy()
            m,n = Self.length()
            if Self.length() == Other.length():
                c = []
                for i in range(m):
                    d = []
                    for j in range(n):
                        d.append((Self[i][j]-Other[i][j]))
                    c.append(d)
                Return = Matrix(c)
                self.matrix = Return.matrix.copy()
            else:
                raise IndexError("Two Matrix can not do subtraction, two Matrix.length unequal")
        else:
            raise TypeError("Unsupported operand type for -")


    # 矩陣乘法
    def Multiply(self,other): 
        '''
        執行矩陣的乘法運算（直接作用於原本的矩陣）\n
        Perform matrix Multiply operation.
        (Apply the Multiply operation directly to the original matrix.)
        '''
        if (type(other) == int or type(other) == float):
            Self,Other = self.copy(),other
            m,n = Self.length()
            b = []
            for i in range(m):
                a = []
                for j in range(n):
                    a.append(Self.matrix[i][j]*Other)
                b.append(a)
            Return = Matrix(b)
            self.matrix = Return.matrix.copy()
            
        elif type(other) == Matrix:
            Self,Other = self.copy(),other.copy()
            if Self.length()[1] == Other.length()[0]:
                Other.Transpose()
                b = []
                for i in Self:
                    a = []
                    for j in Other:
                        a.append(Vector(i)**Vector(j))
                    b.append(a)
                Return = Matrix(b)
                self.matrix = Return.matrix.copy()
            else:
                raise IndexError("矩陣乘法（ＡＸＢ）Ａ的行數必須等於Ｂ的列數")
        else :
            raise TypeError("Unsupported operand type for *")


    # 回傳轉置矩陣 A^T
    def Transpose(self): 
        '''
        將此矩陣變成此矩陣的轉置矩陣（直接作用於原本的矩陣）\n
        Transpose the given matrix so that it becomes its transpose matrix. 
        (apply the operation directly to the original matrix) 
        '''
        Self = self.copy()
        m,n = Self.length()
        b = []
        for i in range(n):
            a = []
            for j in range(m):
                a.append(Self.matrix[j][i])
            b.append(a)
        Return = Matrix(b)
        self.matrix = Return.matrix.copy()


    # 矩陣的次方
    def pow(self, other = int):
        '''
        將此矩陣變成此矩陣的n次方(A^n)，僅限方陣可執行本操作（直接對該矩陣操作）\n
        Raise the given square matrix to the power of n (A^n), 
        applying the operation directly to the matrix. 
        This operation is limited to square matrices only.
        '''
        if isinstance(other, int):
            Self,Other = self.copy(),other
            if Self.isPhalanx:
                if Other > 0:
                    for i in range(Other-1):
                        Self = Self * Self
                elif Other < 0:
                    Self = Self.AntiSquare()
                    for i in range(abs(Other)-1):
                        Self = Self * Self
                elif Other == 0:
                    a = self.column
                    del Self
                    Self = Matrix(f"I{a}")
                self.matrix = Self.matrix.copy()
                
            else:
                raise TypeError("Only phalanx can do **")
        else:
            raise TypeError("Unsupported pow between self and other")


    # 高斯消去法
    def GaussianElimination(self):
        '''
        回傳此矩陣進行高斯消去法後的解，目前尚未完備\n
        Return the solution of the matrix after performing Gaussian elimination. 
        Please note that the implementation for this operation is not complete at the moment.
        '''
        
        Self = self.copy()
        b = Self.length()[0]
        
        a = []
        for i in range(b):
            a.append(Self.matrix[i][:b])
        if Matrix(a).det() == 0:
            raise ZeroDivisionError("Unsupported matrix's division. You can't do det = 0")

        for i in range(b):
            c = Self.matrix[i][i]
            d = 0
            if c != 1:
                if c == 0:continue
                d = float(1/c)
                e = Matrix([Self.matrix[i]])
                e = e*d
                Self.matrix[i] = e[0]
            for j in range(b):
                if j == i: continue
                e = Matrix([Self.matrix[j]])
                g = False
                for i in e[0]:
                    if i != 0:
                        g = True
                        break
                    g = False
                if not g:continue
                f = e[0][i]
                e = e - Matrix([Self.matrix[i]])*f
                Self.matrix[j] = e.matrix[0].copy()
        c = []
        if Self.row-Self.column == 1:
            for i in Self.matrix:
                c.append(i[-1])
            return c
        else:
            d = Self.column
            for i in Self.matrix:
                c.append(i[d:])
            return Matrix(c)


    # 反方陣
    def AntiSquare(self):
        '''
        回傳此矩陣的反方陣（目前僅限二階方陣可進行此操作）\n
        Return the inverse matrix of the given matrix. 
        (Currently limited to 2x2 matrices for this operation.)
        '''
        Self = self.copy()
        if Self.length() == [2,2]:
            a = Matrix([[Self[1][1],-Self[0][1]],[-Self[1][0],Self[0][0]]])
            if Self.det() == 0: raise IndexError("Phalanx.det()=0 so this phalanx can't have antiSquare")
            b = float(1/a.det())
            if b%1!=0:
                a = a * b
            elif b%1 == 0:
                a = a*int(b)
            return a
        elif Self.isPhalanx:
            raise IndexError("Creating the inverse matrix is not supported for square matrices of order two or higher.")
            # if Self.det() == 0: raise IndexError("Phalanx.det()=0 so this phalanx can't have antiSquare")
            # a = "I" + str(Self.column)
            # Self.append(Matrix(a))
            # return Self.GaussianElimination()
        else:
            raise IndexError("Only phalanx has AntiSquare")


    # 合併矩陣（製作增廣矩陣）
    def append(self, other): 
        '''
        合併矩陣（製作增廣矩陣），你可以把兩個矩陣做合併([a|b])，可以簡寫成a = a|b，其中a,b是矩陣且兩個的列數相等（這是對物件本身来操作，沒有回傳值）\n
        Combine matrices (creating an augmented matrix), you can merge two matrices ([a|b]) by using the shorthand 
        notation a = a|b, where a and b are matrices with equal number of columns. (This is an operation on the object itself, without returning a value.)
        '''
        if isinstance(other, Matrix):
            Self,Other = self.copy(), other.copy()
            m = Self.length()[0]
            if Self.column == Other.column:
                a = Self.matrix
                b = Other.matrix
                c = [(a[j]+b[j])  for j in range(m)]
                Return = Matrix(c)
                self.matrix = Return.matrix.copy()
            else:
                raise IndexError("Two Matrixes cannot be augmented as their column dimensions are not equal.")
        else:
            raise TypeError("Unsupported not Matrix to append Matrix")


    #矩陣相等
    def Equal(self, other): 
        if isinstance(other, Matrix):
            Self = self.toList()
            Other = other.toList()
            return Self == Other
        else:
            raise TypeError("Unsupported operand type for ==")






























