from collections import deque #we we an adjacency list to represent graphs 
def depthFirst(adj,str):
    arr=[str] #depthfirst uses a stack
    while len(arr) > 0:
        curr = arr.pop()
        print(curr)
        for node in adj[curr]:
            arr.append(node)
def depthFirstRec(adj,src):
    print(src)
    for  neigherbor in adj[src]:
        depthFirstRec(adj,neigherbor)
def breadthFirst(adj,src):
    arr=deque([src]) #breadthfirst uses a stack
    #print(len(arr))
    while len(arr)>0:
        curr =arr.popleft()
        print(curr)
        for neighbour in adj[curr]:
            arr.append(neighbour)    
dd={
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}
#depthFirst(dd,"a")
breadthFirst(dd,"a")

