class Protected: # defining the Protected class
    def __init__(self):
        self.__private = 'David' # setting __private to David

person1 = Protected()
person1.__private = 'Dave' # this is where the name can be changed to dave using Protected()
print(person1.__private)
