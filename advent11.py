
class Monkey():
	def __init__(self,worries,test):
		self.worries = worries
		self.test = test
		self.inspects = 0
	def link(self,pos,neg):
		self.pos = pos
		self.neg = neg


	def inspect(self):
		for i in self.worries:
			self.inspects+=1
			q = self.test2(i)
			q = q%9699690
			if (q % self.test == 0):
				self.pos.throw(q)
			else:
				self.neg.throw(q)
		self.worries=[]
		
	def throw(self,num):
		self.worries.append(num)
						
	def __str__ (self):
		return str(self.inspects)#+str(self.worries)
		

		
class AddMonkey(Monkey):
	def __init__(self,worries,test,add):
		self.worries = worries
		self.test = test
		self.add = add
		self.inspects = 0
	def test2(self,num):
		return num + self.add
		
class MulMonkey(Monkey):
	def __init__(self,worries,test,mul):
		self.worries = worries
		self.test = test
		self.mul = mul
		self.inspects = 0
	def test2(self,num):
		return num * self.mul
		
class SqMonkey(Monkey):
	def test2(self,num):
		return num * num
	"""	
M0=MulMonkey([79, 98],23,19)
M1=AddMonkey([54, 65, 75, 74],19,6)
M2=SqMonkey([79, 60, 97],13)
M3=AddMonkey([74],17,3)

M0.link(M2,M3)
M1.link(M2,M0)
M2.link(M1,M3)
M3.link(M0,M1)

ml = [M0,M1,M2,M3]
"""
M0=MulMonkey([99, 63, 76, 93, 54, 73],2,11)
M1=AddMonkey([91, 60, 97, 54],17,1)
M2=AddMonkey([65],7,7)
M3=AddMonkey([84, 55],11,3)
M4=SqMonkey([86, 63, 79, 54, 83],19)
M5=AddMonkey([96, 67, 56, 95, 64, 69, 96],5,4)
M6=MulMonkey([66, 94, 70, 93, 72, 67, 88, 51],13,5)
M7=AddMonkey([59, 59, 74],3,8)

M0.link(M7,M1)
M1.link(M3,M2)
M2.link(M6,M5)
M3.link(M2,M6)
M4.link(M7,M0)
M5.link(M4,M0)
M6.link(M4,M5)
M7.link(M1,M3)
ml = [M0,M1,M2,M3,M4,M5,M6,M7]





for j in range(10000):
	for i in ml:
		i.inspect()

for i in ml:
	print(i)
