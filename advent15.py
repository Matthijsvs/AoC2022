ex = """2, 18, -2, 15
9, 16, 10, 16
13, 2, 15, 3
12, 14, 10, 16
10, 20, 10, 16
14, 17, 10, 16
8, 7, 2, 10
2, 0, 2, 10
0, 11, 2, 10
20, 14, 25, 17
17, 20, 21, 22
16, 7, 15, 3
14, 3, 15, 3
20, 1, 15, 3"""

q = """3844106, 3888618,3225436, 4052707
1380352, 1857923,10411, 2000000
272, 1998931,10411, 2000000
2119959, 184595,2039500, -250317
1675775, 2817868,2307516, 3313037
2628344, 2174105,3166783, 2549046
2919046, 3736158,3145593, 4120490
16, 2009884,10411, 2000000
2504789, 3988246,3145593, 4120490
2861842, 2428768,3166783, 2549046
3361207, 130612,2039500, -250317
831856, 591484,-175938, 1260620
3125600, 1745424,3166783, 2549046
21581, 3243480,10411, 2000000
2757890, 3187285,2307516, 3313037
3849488, 2414083,3166783, 2549046
3862221, 757146,4552923, 1057347
3558604, 2961030,3166783, 2549046
3995832, 1706663,4552923, 1057347
1082213, 3708082,2307516, 3313037
135817, 1427041,-175938, 1260620
2467372, 697908,2039500, -250317
3448383, 3674287,3225436, 4052707"""


class sens():
	def __init__(self,pos):
		q = self.decode(pos)
		self.x = q[0]
		self.y = q[1]
		self.bx = q[2]
		self.by = q[3]		
		self.manh = abs(self.x-self.bx)+abs(self.y-self.by)
		#print(f"dist = {self.manh}")
	def decode(self,s):
		p = s.split(",")
		numbers = [ int(x) for x in p ]
		return numbers


	def getimp(self,row):	#impossible locations
		if abs(self.y-row)>self.manh:
			return None
		else:
			l = []
			for i in range(self.manh-abs(self.y-row)+1):
				l.append(self.x-i)
				l.append(self.x+i)

		return l
l=[]
for i in q.splitlines():
	l.append(sens(i))

search = 2000000
pos=[]
for i in l:
	q=i.getimp(search)
	if q is not None:
		pos.extend(q)		
	g = set(pos)	
	
for i in l:
	if i.by==search and i.bx in g:
		g.remove(i.bx)
print ("Part 1:",len(g))

