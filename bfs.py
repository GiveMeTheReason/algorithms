from collections import deque

def pers_is(pers):
    if pers[-1] == "e":
        return True
    else:
        return False

def bfs(name):
    '''
    Example from "Grokking Algorithms"
    Breadth First Search
    '''
    queue = deque()
    for item in graph.get(name):
        queue.append(item)
    passed_set = set()
    while queue:
        pers = queue.popleft()
        if not pers in passed_set:
            if pers_is(pers):
                print(pers, "is a mango seller!")
                return True
            else:
                passed_set.add(pers)
                for item in graph.get(name):
                    queue.append(item)
    print("No mango sellers!")
    return False
    
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["tom"] = []

bfs("you")  # alice is a mango seller!
