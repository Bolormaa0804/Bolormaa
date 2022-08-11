import random
import time

class Grandchild:

    # Each Class will have an init method which is used to create an object known as a constructor in other languages.

    # When a class method is called self will reference the object that called the method.

    countObjectsCreated = 0  # Known as a static Class variable

    def __init__(self, name, age):

        self._name = name

        self.age = age

        Grandchild.countObjectsCreated += 1

    def __str__(self):

        print("\nThis grandchild's name is", self.name)

        return(f"{self.name} is {self.age} years old")

    def isOlder(self, otherGrandchild):

        if self.age > otherGrandchild.age:

            return True

        else:

            return False

    def getCounter():

        print(f"{Grandchild.countObjectsCreated} objects have been created up to this point\n")


def main():

    # Testing/using the Class in main

    # Creating two objects of the Grandchild Class

    James = Grandchild("James", 12)

    Simon = Grandchild("Simon", 10)

    Rafa = Grandchild("Rafa", 35)

    Grandchild.getCounter()

    # Access and Print an Attribute VALUE - No PARENS needed to access the object's data attributes using the dot operator or member access operator.

    print("Accessing an object attribute - Simon's age is", Simon.age)

    print("Accessing an object attribute - James's name is", James.name)

    print("Accessing an object attribute - Rafa's age is", Rafa.age)

    # You can CALL the class methods through the object using the dot operator or member access operator, add PARENS and any paramters.
    '''
    Simon.printDetails()

    James.printDetails()

    Rafa.printDetails()
    '''
    print(f"\nIs Rafa older than James? That is {Rafa.isOlder(James)}")

    print(f"\nIs Simon older than James? That is {Simon.isOlder(James)}")

    # You can create a list of Class objects

    manyGrandChildren = []

    manyGrandChildren.append(James)

    manyGrandChildren.append(Simon)

    # Create 100 GrandChild Objects

    # Place them in a list and find the average age of the Grandchild Objects.

    sumAges = 0

    howMany = 10
    start_time = time.time()
    for i in range(howMany):
        anotheNewGrandchild = Grandchild(howMany, random.randrange(1, 40))

        manyGrandChildren.append(anotheNewGrandchild)
        '''anotheNewGrandchild.printDetails()'''

        sumAges = sumAges + anotheNewGrandchild.age
    end_time = time.time()

    average = sumAges / howMany

    print("Average age of the Grandchildren", round(average, 2))

    print((end_time - start_time), "seconds")
    print(James)


main()

