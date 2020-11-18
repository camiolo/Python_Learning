
# To call/use this staff,
#   First, import this module  .... import classdemo
#   Second, explicitly state that we are using it as our object creation  ....   New_obj = classdemo.Staff('Position_name', 'Person_Name', Pay_amount)

class Staff:
    #Contents of the class, known as Staff.

    def __init__ (self, pPosition, pName, pPay):
        self._position = pPosition
        self.name = pName
        self.pay =pPay
        print('Creating Staff Object')

    def __str__(self):
        return "Position = %s, Name = %s, Pay = %d" % (self._position, self.name, self.pay)

    def calculatePay (self):
        prompt = '\nEnter number of hours for %s: ' %(self.name)
        hours = input(prompt)
        prompt =  'Enter the hourly rate for %s: ' %(self.name)
        hourlyRate = input (prompt)
        self.pay = int(hours) * int (hourlyRate)
        return self.pay
    
    @property
    def position(self):
        print("Getter Method")
        return self._position
    
    @position.setter
    def position (self, value):
        if value in ['Manager', 'Basic', 'Man Eater']:
            self._position = value
        else:
            print ('Position is invalid. No changes made.')



class A:
    def __init__(self):
        self.__x = 5   # A double Underscore name isn't an acceptable variable name.  It's auto changed to _A__x 
        self._y = 6
    
    def __str__(self):
        return "X = %d, Y = %d " % (self.__x, self._y)



class Play:
    #Contents of the class, known as Staff.

    def __init__ (self, Alpha, Beta):
        self.one = Alpha
        self.two = Beta
        print('Creating Staff Object')

    def __str__(self):
        return "Position = %s, Name = %s" % (self.one, self.two)


class MethodDemo:
    a = 1 
    def __init__ (self, Alpha, Beta):
        self.one = Alpha
        self.two = Beta
        print('Creating Staff Object')

    @classmethod
    def classM(cls):
        print("Class Method. cls .a = %s"  %( cls.a ))

    @staticmethod
    def staticM():
        print("Static Method")


class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'