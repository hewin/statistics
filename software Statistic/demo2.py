
from types import MethodType
import types



class Student(object):
   def __init__(self,name,score):
      self.__name = name
      self.__score = score
   def equal(self,student):
      return student.__n==self.__n
   def getGrade(self):
      return 'A' if self.__s>90 else 'B'
   def __str__(self):
      return 'Student object(name:%s score:%s)' % (self.__name,self.__score)
   @property
   def score(self):
      return self.score

   @score.setter
   def score(self,value):
      if not isinstance(value,int):
         raise ValueError('score must be an integer')
      if value<0 or value>100:
         raise ValueError('score must between 0~100')
      self.score = value


s = Student('a',90)

class Fib:
   count = 0
   def __init__(self,n):
      self.a = 0
      self.b = 1
      self.n = n


   def __iter__(self):
      return self

   def next(self):
      if self.count < self.n:
         self.a,self.b = self.b,self.a + self.b
         self.count = self.count + 1
      return self.a

for n in Fib(10):
    print n