from collections import deque
def hasPath(graph,src,dst):
    arr=[src]
    while(len(arr)>0):
        current = arr.pop()
        for neighbour in graph[current]:
            arr.append(neighbour)
            if neighbour == dst:
                return True
    return False


def hasPathBre(graph,src,dst):
    arr=deque([src])
    while len(arr)>0:
        curr =arr.popleft()
        if curr==dst:
            return True
        for neighbour in graph[curr]:
            arr.append(neighbour)
    return False
dd={
    "a":["c","b"],
    "b":["d"],
    "c":["e"],
    "d":["f"],
    "e":[],
    "f":[]
}
newPath = {
    "f":["g","i"],
    "g":["h"],
    "h":[],
    "i":["g","k"],
    "j":["i"],
    "k":[]
}
print(hasPathBre(newPath,"j","f"))
#alvin the programmer