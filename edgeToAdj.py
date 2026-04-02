# def edgeToAdj(edge):
#     obj={}
#     for path in edge:
#         if path[0] in obj:
#             obj[path[0]].append(path[1])
#             if path[1] in obj:
#                 obj[path[1]].append(path[0])
#             else:
#                 obj[path[1]]=[path[0]]
#         else:
#             obj[path[0]]=[path[1]]
#             obj[path[1]]=[path[0]]
#     print(obj)

def anotherM(edge):
    obj={}
    
    for path in edge:
        [a,b]=path
        if a not in obj:
            obj[a]=[]
        if b not in obj:
            obj[b]=[]
        obj[a].append(b)
        obj[b].append(a)
    return obj
    
def hasPath(edges,src,dst):
    setter = set()
    graph = anotherM(edges)
    stack = [src]
    while len(stack)>0:
        curr = stack.pop()
        if curr in  setter:
            continue
        setter.add(curr)
        if curr == dst:
            return True
        for neighbour in graph[curr]:
            stack.append(neighbour)
    return False
edge = [
    ["i","j"],
    ["k","i"],
    ["m","k"],
    ["k","l"],
    ["o","n"]
]
print(hasPath(edge,"i","n"))