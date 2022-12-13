asm="""addx 1
addx 4
noop
noop
addx 30
addx -24
addx -1
noop
addx 4
addx 1
addx 5
addx -4
addx 5
addx 4
addx 1
noop
addx 5
addx -1
addx 5
addx 3
noop
addx -38
addx 9
addx -4
noop
addx 3
noop
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx -17
addx 22
addx -2
addx 5
addx 2
addx 3
addx -2
addx -36
noop
addx 5
noop
addx 3
noop
addx 2
addx -5
noop
addx 10
addx 3
addx -2
addx 3
addx 2
addx 4
noop
noop
noop
noop
addx 3
noop
noop
addx 7
addx 1
noop
noop
addx -38
addx 39
addx -32
noop
noop
noop
addx 5
addx 2
addx -1
addx 4
noop
addx 5
addx -2
addx 5
addx 2
addx -26
addx 31
addx -2
addx 4
addx 3
addx -18
addx 19
addx -38
addx 7
noop
noop
addx 34
addx -39
addx 8
addx 5
addx 2
addx 10
addx -5
addx -2
addx 5
addx 2
addx 11
addx -6
noop
addx 3
noop
addx 2
addx 3
addx -2
addx -38
noop
noop
noop
addx 5
addx 11
noop
addx -3
noop
noop
noop
addx 2
noop
addx -11
addx 16
noop
addx 3
addx 2
addx 8
noop
noop
noop
noop
noop
addx 4
addx 3
noop
addx -20
noop"""

cycle = 1
sample = [20,60,100,140,180,220]

res=[]
X = 1
screen = ["" for i in range(7)]

rows = ""
def draw(cycle,X):
	if cycle in sample:
		res.append(X)
	col = (cycle-1) % 40
	row = (cycle-1) // 40
	c=" "
	if (col >= X-1 and col <= X+1):
		c = '@'
	screen[row]+=c

for i in asm.splitlines():
	draw(cycle,X)
	if i=="noop":
		cycle+=1
	else:
		cycle+=1
		draw(cycle,X)
		cycle+=1
		add,x=i.split(" ")
		X+=int(x)


q = [a*b for a,b in zip(sample,res)]
print(sum(q))

for i in screen:
	print(i)
