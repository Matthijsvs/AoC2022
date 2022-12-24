import re
import time
from dataclasses import dataclass
from heapq import heappush,heappop

@dataclass
class State:
    """Class for keeping track of an item in inventory."""
    step:int
    res:list
    bot:list
    def __lt__(self,other):
        return False
ex="""Blueprint 1:Each ore robot costs 4 ore.  Each clay robot costs 2 ore.  Each obsidian robot costs 3 ore and 14 clay.  Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2:  Each ore robot costs 2 ore.  Each clay robot costs 3 ore.  Each obsidian robot costs 3 ore and 8 clay.  Each geode robot costs 3 ore and 12 obsidian."""
q="""Blueprint 1: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 3: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 4: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 4 ore and 14 obsidian.
Blueprint 5: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 6: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 13 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 15 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 9: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 19 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 11: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 6 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 12: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 2 ore and 10 obsidian.
Blueprint 13: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 14: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 9 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 15: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 13 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 16: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 17: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 6 clay. Each geode robot costs 3 ore and 16 obsidian.
Blueprint 18: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 19: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 20: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 18 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 21: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 17 clay. Each geode robot costs 3 ore and 11 obsidian.
Blueprint 23: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 3 ore and 7 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 11 clay. Each geode robot costs 4 ore and 12 obsidian.
Blueprint 25: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 5 clay. Each geode robot costs 3 ore and 18 obsidian.
Blueprint 27: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 2 ore and 13 obsidian.
Blueprint 28: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 3 ore and 19 obsidian.
Blueprint 29: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 3 ore and 14 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 4 ore and 16 obsidian."""



def canBuy(resources,pricelist):
    for i in range(len(resources)):
        if resources[i]<pricelist[i]:
            return False
    return True

def Buy(resources,bots,num):
    for i in range(len(resources)):
        resources[i]-=price[num][i]
    bots[num]+=1

def buyNext(nextitm,resources,step,bots):
        lmax=-1
        if step>=24:
            return max(lmax,resources[3])
        
        newbots=bots.copy()
        done=False
        while not done:
            if canBuy(resources,price[nextitm]):
                Buy(resources,price,newbots,nextitm);
                done=True
            resources = [ resources[x] + bots[x] for x in range (len (resources))]
            step+=1
            if step>=24:
                return resources[3]
                done=True
        bots=newbots
        #print(bots,"\t",resources)
        for i in range(4):
            lmax = max(lmax,buyNext(i,resources.copy(),step,bots))
        return lmax


def processState(state,l):
    for i in range(4):
        if canBuy(state.res,price[i]):
                newbots=state.bot.copy()
                res = state.res.copy()
                Buy(res,newbots,i);
                resources = [ res[x] + state.bot[x] for x in range (4)]
                s = State(state.step+1,resources,newbots)
                score = resources[3]*1000 + resources[2]*23 + resources[1]*7 + resources[0]+newbots[2]*300+newbots[3]*500
                heappush(l,(-1*score,s))
                #print(s)
    resources = [ state.res[x] + state.bot[x] for x in range (len (state.res))]
    s=State(state.step+1,resources,state.bot)
    score = resources[3]*1000 + resources[2]*23 + resources[1]*7 + resources[0]+state.bot[2]*300+state.bot[3]*500
    
    heappush(l,(-1*score,s))

    
x = re.findall(r"Blueprint\s*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)\D*(\d+)", q)
idx=1
tot=1
start = time.time()

for recipe in x[:3]:
    stats = [int(_) for _ in recipe]

    price = [[stats[1],0,0,0],          #ore bot costs ore
             [stats[2],0,0,0],          #clay bot costs ore
             [stats[3],stats[4],0,0],   #Obsidian bot costs ore+clay
             [stats[5],0,stats[6],0]]   #Geode bot costs ore+obs

    #print(price) 
    ore=0
    clay=0
    obsidian=0
    geode=0
    resources=[ore,clay,obsidian,geode]
    bots = [1,0,0,0] #1 ore bot is gifted

    
    stat = State(0,resources,bots)  #zero state
    sl=[]                           #statelist
    processState(stat,sl)           #create first iteration states
    
    for i in range(1,32):
        #print(f"step {i} {len(sl)}")
        osl=sl[:]                   #old state list
        sl=[]
        for i in range(5000):
            if len(osl)>0:
                score,itm = heappop(osl)
                processState(itm,sl)
            else:
                break

    s,bestState=heappop(sl)
    lmax=bestState.res[3]
    print(bestState)
    tot*=lmax
    print(f"{time.time()-start:05.1f}\t{lmax}\t{tot}")
    idx+=1


