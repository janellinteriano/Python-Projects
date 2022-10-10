class Protected: # defining the Protected class
    def __init__(self):
        self._protected = 'David' # setting protected variable to David



class Protected2: # protected2 class
    def __init__(self): # private variable 
        self.__privateVar = 21 

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
    

obj1 = Protected()
obj1.__private = 'Dave' # this is where the name can be changed to dave using Protected()
print(obj1.__private)

obj2 = Protected2()
obj2.getPrivate()
obj2.setPrivate(54) # this is where number can be changed to 54
obj2.getPrivate()
