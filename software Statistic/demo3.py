
class Fib(object):
	def __init__(self):
		self.a = 0
		self.b = 1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a > 100000:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		a,b=0,1
		if isinstance(n,int):
			for x in range(n):
				a,b = a,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			end = n.stop
			L = []
			for x in range(end)[start:]:
				# if x>=start:
				L.append(a)
				a,b = b,a+b
			return L

f = Fib()
print f[0:5]

class A(object):
	count = 0
	def __init__(self):
		pass
	def do(self):
		self.count +=1
	def __call__(self):
		print "a"

a = A()
b = A()
a.do()
a.do()
b.do()
b.do()
print a.count 
print b.count
print callable(a)