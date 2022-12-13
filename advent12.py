t = """abaaaaacaaaacccccccccaaaaaaccccccccccccccccccccccccccccccccccaaaaaa
abaaaaacaaaaccccaaaaaaaaaacccccccccccccccccccccccccccccccccccaaaaaa
abaaacccaaaaccccaaaaaaaaaaacccaacccccccccccaacccccccccccccccccaaaaa
abaaaacccaacccccaaaaaaaaaaaaaaaaacccccccccccacccccccccccccccccccaaa
abacaacccccccccccaaaaaaaaaaaaaaaaccccccccccaacccccccccccccccccccaaa
abcccacccccccccccaaaaaaaccaaaaaaaccccccccccclllcccccacccccccccccaac
abccccccccccccccccaaaaaccccccccccccccccccclllllllcccccccccccccccccc
abaaacccccccccccccaaaaaccccccccccccccccaakklllllllcccccccccaacccccc
abaaacccccccccccacccaaaccccccccccccccccakkklpppllllccddaaacaacccccc
abaaacccaaacccccaacaaaccccccccccccccccckkkkpppppllllcddddaaaacccccc
abaacccaaaacccccaaaaaccccccccccccccccckkkkpppppppllmmddddddaaaacccc
abaaaccaaaaccccccaaaaaacaaacccccccccckkkkpppuuuppplmmmmdddddaaacccc
abaaacccaaaccccaaaaaaaacaaaaccccccckkkkkoppuuuuuppqmmmmmmdddddacccc
abcccccccccccccaaaaaaaacaaaacccccjkkkkkooppuuuuuuqqqmmmmmmmddddcccc
abccccccccccccccccaaccccaaaccccjjjjkoooooouuuxuuuqqqqqqmmmmmddecccc
abacaaccccccccccccaacccccccccccjjjjoooooouuuxxxuvvqqqqqqqmmmeeecccc
abaaaacccccccacccaccccccccccccjjjjoootuuuuuuxxxyvvvvvqqqqmmmeeecccc
abaaaaacccccaaacaaacccccccccccjjjoooottuuuuuxxyyvvvvvvvqqmnneeecccc
abaaaaaccaaaaaaaaaaccccccccaccjjjooottttxxxxxxyyyyyyvvvqqnnneeecccc
abaaaccccaaaaaaaaaacccccccaaccjjjoootttxxxxxxxyyyyyyvvqqqnnneeecccc
SbcaaccccaaaaaaaaaaccccaaaaacajjjnnntttxxxxEzzzyyyyvvvrrqnnneeccccc
abcccccccaaaaaaaaaaacccaaaaaaaajjjnnntttxxxxyyyyyvvvvrrrnnneeeccccc
abcccccccaaaaaaaaaaacccccaaaaccjjjnnnnttttxxyyyyywvvrrrnnneeecccccc
abcccccccccaaaaaaccaccccaaaaaccciiinnnnttxxyyyyyyywwrrnnnneeecccccc
abccccccccccccaaacccccccaacaaaccciiinnnttxxyywwyyywwrrnnnffeccccccc
abccccccccccccaaacccccccaccaaaccciiinnnttwwwwwwwwwwwrrrnnfffccccccc
abccccccccccccccccccccccccccccccciiinnnttwwwwsswwwwwrrrnnfffccccccc
abaaaccaaccccccccccccccccccccccccciinnnttswwwssswwwwrrroofffacccccc
abaaccaaaaaacccccccccccccccccaaacciinnntssssssssssrrrrooofffacccccc
abaccccaaaaacccccccaaacccccccaaaaciinnnssssssmmssssrrrooofffacccccc
abaacaaaaaaacccccccaaaaccccccaaaaciiinmmmssmmmmmoosroooooffaaaacccc
abaaaaaaaaaaaccccccaaaaccccccaaacciiimmmmmmmmmmmoooooooofffaaaacccc
abcaaaaaaaaaaccccccaaaaccccccccccccihhmmmmmmmhggoooooooffffaaaccccc
abcccccaaacaccccccccaaccccccccccccchhhhhhhhhhhggggggggggffaaacccccc
abaccccaacccccccccccaaaccccccccccccchhhhhhhhhhgggggggggggcaaacccccc
abaaaccccaccccccccccaaaacccaacccccccchhhhhhhaaaaaggggggcccccccccccc
abaaaccccaaacaaaccccaaaacaaaacccccccccccccccaaaacccccccccccccccaaac
abaacccccaaaaaaaccccaaaaaaaaacccccccccccccccaaacccccccccccccccccaaa
abaaaccccaaaaaaccccaaaaaaaaccccccccccccccccccaacccccccccccccccccaaa
abccccccaaaaaaaaaaaaaaaaaaacccccccccccccccccaaccccccccccccccccaaaaa
abcccccaaaaaaaaaaaaaaaaaaaaacccccccccccccccccccccccccccccccccaaaaaa"""

emap=[]
y=0
for line in t.splitlines():
    lmap = []
    x = 0
    for c in line:
        if c == "S":
            c =  "a"
            start = (x,y)
        elif c == "E":
            c = "z"
            end = (x,y)
        c = ord(c)-ord("a")+1
        x+=1
        lmap.append(c)
    emap.append(lmap)
    y+=1


empty = [[0 for i in range(x)] for i in range(y)]

print(start,end)

                
def calc(node,path):
    x,y = node
    if y<0 or x<0 or x>=len(grid[0]) or y>=len(grid):
        return
    if grid[y][x] == 0 or path<grid[y][x]:  
        grid[y][x]=path
    else:
        if path >= grid[y][x]:
            return
    val = maze[y][x]
    #print(x,y,val)
    for i in [(x-1, y),(x,y - 1),(x,y + 1),(x+1,y)]:
        x2,y2 = i
        if y2>=0 and x2>=0 and x2<len(grid[0]) and y2<len(grid):
            if maze[y2][x2] <= val+1: 
                if path<998:
                    calc(i,path+1)
        
#empty[start[1]][start[0]] = 1   
for uu in range(len(empty)):
    start=(1,uu)
    grid = empty
    maze = emap
    calc(start,1)

    s=""
    for line in grid:
        for c in line:
            s+=f" {c:02}"
        s+="\n"
    #print(s)
    print(grid[end[1]][end[0]]-1)