class Person:

   def __init__(self, name=None, surname=None, age=0, gender=None):
       self.name = name
       self.surname = surname
       self.__age = age
       self.gender = gender


   def __walk(self):
       print('Person',self.name, 'is walking')

   def info(self):
       print(f"Person {self.name} {self.surname} is {self.__age} years old.")


