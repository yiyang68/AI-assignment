import heapq
import Queue
import math
import ast
import sys
class waterjug:
    def __init__(self,state,parent,child,cost):
        self.state=state
        self.parent=parent
        self.child=child
        self.cost=cost
class pathpl:
    def __init__(self,state,number,parent,child,cost):
        self.state=state
        self.number=number
        self.parent=parent
        self.child=child
        self.cost=cost
class pancake:
    def __init__(self,state,parent,child,cost):
        self.state=state
        self.parent=parent
        self.child=child
        self.cost=cost
N={}
q=Queue.PriorityQueue()
flist=[]
elist=[]
def notexist(node,newj1,newj2,newj3):
    new_node = waterjug((newj1, newj2, newj3), node, [], node.cost + 1)
    node.child.append(new_node)
def notexist2j(node,newj1,newj2):
    new_node = waterjug((newj1, newj2), node, [], node.cost + 1)
    node.child.append(new_node)
def generate3j(node):
    if node.state[0]<maxj[0]:
        newj1,newj2,newj3=maxj[0],node.state[1],node.state[2]
        notexist(node,newj1,newj2,newj3)
    if node.state[1] < maxj[1]:
        newj1,newj2,newj3=node.state[0],maxj[1],node.state[2]
        notexist(node,newj1,newj2,newj3)
    if node.state[2] < maxj[2]:
        newj1, newj2, newj3 = node.state[0], node.state[1], maxj[2]
        notexist(node, newj1, newj2, newj3)
    if node.state[0]>0 and node.state[1] < maxj[1]:
        newj1=node.state[0]+node.state[1]-maxj[1] if node.state[0]+node.state[1]-maxj[1]>0 else 0
        newj2=node.state[0]+node.state[1] if node.state[0]+node.state[1]<maxj[1] else maxj[1]
        notexist(node, newj1, newj2,node.state[2])
    if node.state[0] > 0 and node.state[2] < maxj[2]:
        newj1=node.state[0]+node.state[2]-maxj[2] if node.state[0]+node.state[2]-maxj[2]>0 else 0
        newj3=node.state[0]+node.state[2] if node.state[0]+node.state[2]<maxj[2] else maxj[2]
        notexist(node, newj1, node.state[1], newj3)
    if node.state[1] > 0 and node.state[0] < maxj[0]:
        newj2=node.state[0]+node.state[1]-maxj[0] if node.state[0]+node.state[1]-maxj[0]>0 else 0
        newj1=node.state[0]+node.state[1] if node.state[0]+node.state[1]<maxj[0] else maxj[0]
        notexist(node, newj1, newj2, node.state[2])
    if node.state[1] > 0 and node.state[2] < maxj[2]:
        newj2 = node.state[2] + node.state[1] - maxj[2] if node.state[2] + node.state[1] - maxj[2] > 0 else 0
        newj3 = node.state[2] + node.state[1] if node.state[2] + node.state[1] < maxj[2] else maxj[2]
        notexist(node,node.state[0] , newj2, newj3)
    if node.state[2] > 0 and node.state[0] < maxj[0]:
        newj3=node.state[0]+node.state[2]-maxj[0] if node.state[0]+node.state[2]-maxj[0]>0 else 0
        newj1=node.state[0]+node.state[2] if node.state[0]+node.state[2]<maxj[0] else maxj[0]
        notexist(node, newj1, node.state[1], newj3)
    if node.state[2] > 0 and node.state[1] < maxj[1]:
        newj3=node.state[2] + node.state[1] - maxj[1] if node.state[2] + node.state[1] - maxj[1] > 0 else 0
        newj2=node.state[2] + node.state[1] if node.state[2] + node.state[1] < maxj[1] else maxj[1]
        notexist(node, node.state[0], newj2, newj3)
    if node.state[0]>0:
        notexist(node, 0, node.state[1], node.state[2])
    if node.state[1] > 0:
        notexist(node,node.state[0] ,0 , node.state[2])
    if node.state[2]>0:
        notexist(node, node.state[0], node.state[1], 0)
def generate2j(node):
    if node.state[0]<maxj[0]:
        newj1,newj2=maxj[0],node.state[1]
        notexist2j(node,newj1,newj2)
    if node.state[1]<maxj[1]:
        newj1,newj2=node.state[0],maxj[1]
        notexist2j(node,newj1,newj2)
    if node.state[0] > 0 and node.state[1] < maxj[1]:
        newj1=node.state[0]+node.state[1]-maxj[1] if node.state[0]+node.state[1]-maxj[1]>0 else 0
        newj2=node.state[0]+node.state[1] if node.state[0]+node.state[1]<maxj[1] else maxj[1]
        notexist2j(node, newj1, newj2)
    if node.state[1] > 0 and node.state[0] < maxj[0]:
        newj2=node.state[0]+node.state[1]-maxj[0] if node.state[0]+node.state[1]-maxj[0]>0 else 0
        newj1=node.state[0]+node.state[1] if node.state[0]+node.state[1]<maxj[0] else maxj[0]
        notexist2j(node, newj1, newj2)
    if node.state[0] > 0:
        notexist2j(node, 0, node.state[1])
    if node.state[1] > 0:
        notexist2j(node, node.state[0], 0)
def path_generate(node):
    for j in range(0,len(citylist)):
        if matrix[node.number][j]:
            new_node=pathpl(citylist[j],j,node,[],node.cost+matrix[node.number][j])
            node.child.append(new_node)
def pancake_gen(node):
    n=len(node.state)
    i=0
    while i<n:
        x = []
        j=n-i-1
        m=n-i-1
        p=n-i
        while m>=0:
            x.append(0-node.state[m])
            m=m-1
        while p<n:
            x.append(node.state[p])
            p=p+1
        new_node = pancake(tuple(x),node,[],node.cost+1)
        node.child.append(new_node)
        i=i+1

def printtree(node):
    print 'cost:',node.cost
    while(node!=head):
        print node.state
        node=node.parent
str="false"
def dfs():
    while 1:
        if not flist:
            print "false"
            break
        node=flist.pop()
        if node.state==goalstate:
            printtree(node)
            break
        if len(node.state)==3:
            generate3j(node)
        elif len(node.state)==2:
            generate2j(node)
        elif type(node.state)==type('a'):
            path_generate(node)
        else:
            pancake_gen(node)
        for children in node.child:
            temp = node
            flag = True
            while (temp != head):
                 if children.state==temp.state:
                    flag=False
                    break
                 temp=temp.parent
            if children.state == temp.state:
                flag = False
            if flag:
                flist.append(children)
#dfs()
def bfs():
    while 1:
        if not flist:
            print "false"
            break
        node=flist.pop(0)
        if node.state==goalstate:
            printtree(node)
            break
        elist.append(node.state)
        if len(goalstate)==3:
            generate3j(node)
        elif len(goalstate)==2:
            generate2j(node)
        elif type(goalstate)==type('a'):
            path_generate(node)
        else:
            pancake_gen(node)
        for children in node.child:
            if children.state not in elist:
                flist.append(children)
#bfs()
M = {'a':{'b':2, 'c':1, 'd':3, 'e':9, 'f':4},
     'e': {'f': 5},
     'c':{'d':8},
     'b':{'c':4, 'e':3},
     'd':{'e':7},
     'h':{'f':9, 'g':8},
     'f':{'c':2, 'g':2, 'h':2},
     'g':{'f':1, 'h':6}
     }
def unicost():
    while 1:
        if not q:
            print "false"
            break
        node= q.get()
        if node[1].state==goalstate:
            printtree(node[1])
            break
        if len(node[1].state)==3:
            generate3j(node[1])
        elif len(node[1].state)==2:
            generate2j(node[1])
        elif type(node[1].state)==type('a'):
            path_generate(node[1])
        else:
            pancake_gen(node)
        for children in node[1].child:
            q.put((children.cost,children))
#unicost()
def DLS(list):
    while 1:
        if not list:
            #print "false"
            return False
        x=list.pop()
        node=x[0]
        limit=x[1]
        if node.state==goalstate:
            printtree(node)
            return True
        if len(node.state)==3:
            generate3j(node)
        elif len(node.state)==2:
            generate2j(node)
        elif type(node.state)==type('a'):
            path_generate(node)
        else :
            pancake_gen(node)
        limit=limit-1
        for children in node.child:
            temp = node
            flag = True
            while (temp != head):
                 if children.state==temp.state:
                    flag=False
                    break
                 temp=temp.parent
            if children.state == temp.state:
                flag = False
            if limit<0:
                flag=False
            if flag:
                list.append((children,limit))
def iddfs():
    limit =1
    while 1:
        list=[]
        list.append((head,limit))
        if DLS(list):
            break
        else:
            limit=limit+1
def h_water(node):
    if len(node.state)==3:
        a= math.sqrt((node.state[0]-goalstate[0])**2+(node.state[1]-goalstate[1])**2+(node.state[2]-goalstate[2])**2)
    if len(node.state)==2:
        a=math.sqrt((node.state[0]-goalstate[0])**2+(node.state[1]-goalstate[1])**2)
    return a
def h_path(node):
    a=math.sqrt((N[node.state][0]-N[goalstate][0])**2+(N[node.state][1]-N[goalstate][1])**2)
    return a
def h_pancake(node):
    n=len(node.state)-1
    a=0
    while n>=0:
        if node.state[n]!=goalstate[n]:
            a=n
            break
        n=n-1
    return a
def greedy():
    while 1:
        if not q:
            print "false"
            break
        node= q.get()
        if node[1].state==goalstate:
            printtree(node[1])
            break
        if len(node[1].state)==3:
            generate3j(node[1])
        elif len(node[1].state)==2:
            generate2j(node[1])
        elif type(node[1].state)==type('a'):
            path_generate(node[1])
        else:
            pancake_gen(node[1])
        for children in node[1].child:
            if len(node[1].state)==3 or len(node[1].state)==2:
                q.put((h_water(children),children))
            elif type(node[1].state) == type('a'):
                q.put((h_path(children), children))
            else:
                q.put((h_pancake(children),children))
def astar():
    while 1:
        if not q:
            print "false"
            break
        node= q.get()
        if node[1].state==goalstate:
            printtree(node[1])
            break
        if len(node[1].state)==3:
            generate3j(node[1])
        elif len(node[1].state)==2:
            generate2j(node[1])
        elif type(node[1].state)==type('a'):
            path_generate(node[1])
        else:
            pancake_gen(node[1])
        for children in node[1].child:
            if len(node[1].state)==3 or len(node[1].state)==2:
                q.put((h_water(children)+children.cost,children))
            elif type(node[1].state) == type('a'):
                q.put((h_path(children)+children.cost, children))
            else:
                q.put((h_pancake(children)+children.cost,children))
def cost_limitDFS(list,cutoff):
    next_min=float("inf")
    while 1:
        if not list:
            return (next_min,0)
        node=list.pop()
        if h_pancake(node)+node.cost<=cutoff:
            if node.state==goalstate:
                printtree(node)
                return (next_min,1)
            if len(node.state) == 3:
                generate3j(node)
            elif len(node.state) == 2:
                generate2j(node)
            elif type(node.state) == type('a'):
                path_generate(node)
            else:
                pancake_gen(node)
            for children in node.child:
                temp = node
                flag = True
                while (temp != head):
                    if children.state == temp.state:
                        flag = False
                        break
                    temp = temp.parent
                if children.state == temp.state:
                    flag = False
                if flag:
                    list.append(children)
        else:
            if h_pancake(node)+node.cost<next_min:
                next_min=h_pancake(node)+node.cost
#bfs()
#greedy()
#iddfs()
#astar()
def idastar():
    cutoff=h_pancake(head)
    while 1:
        list = []
        list.append(head)
        x=cost_limitDFS(list,cutoff)
        if x[1]!=0:
            print 'true'
            break
        if math.isinf(x[0]):
            print 'false'
            break
        cutoff=x[0]
#idastar()
filename=sys.argv[1]
funcname=sys.argv[2]
file=open(filename,'r')
maxj = ()
initstate = ()
goalstate = ()
firstline= file.readlines()
x=firstline[0].split('\r')
if x[0]=='jugs':
    print x[1]
    maxj=tuple(map(int,x[1].strip(' ').strip('(').strip(')').split(',',1)))
    initstate=tuple(map(int,x[2].strip(' ').strip('(').strip(')').split(',',1)))
    goalstate=tuple(map(int,x[3].strip(' ').strip('(').strip(')').split(',',1)))
    head=waterjug(initstate,0,[],0)
if x[0]=='pancakes':
    initstate = tuple(map(int, x[1].strip(' ').strip('[').strip(']').split(',')))
    goalstate = tuple(map(int, x[2].strip(' ').strip('[').strip(']').split(',')))
    head=pancake(initstate,0,[],0)
else:
    y=firstline[1].strip().strip('\n').split(')')
    for i in range(0,len(y)):
        z=y[i].strip(',').strip(' ').strip('[').strip(']').strip('(').split(',')
        N[z[0]]=tuple(map(int,z[1:]))
    citylist = N.keys()
    matrix = [[0 for i in range(len(citylist))] for i in range(len(citylist))]
    initstate=''.join(firstline[2].rstrip().strip('\n'))
    goalstate=''.join(firstline[3].strip('\n'))
    for i in range(4,len(firstline)):
        w=firstline[i].strip().strip('(').strip(')').split(',')
        k=[]
        for i in w:
            j=i.replace(' ','')
            k.append(j)
        matrix[citylist.index(k[0])][citylist.index(k[1])]=int(k[2])
        matrix[citylist.index(k[1])][citylist.index(k[0])] = int(k[2])
    head=pathpl(initstate,citylist.index(initstate),0,[],0)
file.close()
q.put((0,head))
flist.append(head)
if funcname=='dfs':
    dfs()
if funcname=='bfs':
    bfs()
if funcname=='iddfs':
    iddfs()
if funcname=='unicost':
    unicost()
if funcname=='greedy':
    greedy()
if funcname=='astar':
    astar()
if funcname=='idastar':
    idastar()