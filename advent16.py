ex="""AA,0, DD, II, BB
BB,13, CC, AA
CC,2, DD, BB
DD,20, CC, AA, EE
EE,3, FF, DD
FF,0, EE, GG
GG,0, FF, HH
HH,22, GG
II,0, AA, JJ
JJ,21, II"""

q="""OS,0, EE, CL
EN,0, CL, GV
RR,24, FS, YP
VB,20, UU, EY, SG, ZB
UU,0, OT, VB
WH,0, CS, JS
OF,25,to YM
TY,0, AA, GQ
RV,0, BT, YX
GK,0, GD, AA
EL,0, EK, EE
OT,9, YR, BJ, OX, UU, HJ
DG,11, BN, QE
YR,0, OT, YX
GV,0, AA, EN
BN,0, DG, LU
FS,0, TI, RR
DW,0, SS, MS
DJ,0, KY, GD
BJ,0, OT, BT
KY,0, EE, DJ
YP,0, YM, RR
LU,0, BN, CS
OX,0, OT, XD
ZB,0, VB, PP
CL,10, KQ, EN, OS, MQ
XD,0, KR, OX
YM,0, OF, YP
EY,0, MS, VB
KQ,0, CS, CL
SS,0, AA, DW
SG,0, VB, KR
EE,22, XR, OS, KY, EL
OI,0, RE, MS
QE,0, DG, GD
GD,3, GK, DJ, MQ, QE, JS
EK,23,  EL
GQ,0, CS, TY
CS,7, GQ, WH, KQ, LU
MS,4, HJ, EY, DW, OI
XR,0, EE, AA
RE,6, TI, PP, OI
KR,17, XD, SG
BT,15, BJ, RV
PP,0, RE, ZB
TI,0, RE, FS
HJ,0, OT, MS
AA,0, GK, GV, SS, XR, TY
MQ,0, GD, CL
JS,0, GD, WH
YX,5, YR, RV"""


path = []
valvs={}
import copy
class Valve():
	def __init__(self,name,flow):
		self.name=name
		self.flow=flow
		self.others=[]
	def add(self,leads):
		for i in leads:
			self.others.append(i.strip())
			
			
	def explore(self,time,path,maxpath):
		#print(f"== Minute {time} ==")
		newtime = time

		if self.flow>0 and self.name not in path:
			maxpath+= (30-newtime)*self.flow
			newtime+=1
			path.append(self.name)
			print(f"opening {self.name} flow={maxpath}, path = {path}" )
			if len(path)==6:#flowvalves:
				return maxpath
		if len(path)<flowvalves and newtime<30:
			for i in self.others:
				print(f"going to valve {i}")
				path2 = copy.deepcopy(path)
				q = valvs[i].explore(newtime+1,path2,maxpath)
				maxpath = max(maxpath,q)
		return maxpath
		
flowvalves=0
for i in ex.splitlines():
	d = i.split(",")
	name= d.pop(0).strip()
	flow = int(d.pop(0))
	if flow>0:
		flowvalves+=1
	
	if name not in valvs:
		valvs[name]=Valve(name,flow)
		valvs[name].add(d)

print(f"{flowvalves} have flow>0")
print(valvs["AA"].explore(1,[],0))
