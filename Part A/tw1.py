from collections import defaultdict
class Graph:
    count = 0
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfid(self, v, target,  max_depth):
        self.count += 1
        print(v, target)
        if v == target: return True
        if max_depth <= 0: return False
        for neighbour in self.graph[v]:
            if self.dfid(neighbour, target, max_depth-1): return True
        return False


    def dfs(self, v, target, max_depth):
        for i in range(max_depth):
            if self.dfid(v, target, i): return True
        return False



def main():
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    source = 0
    target = 6
    max_depth = 3
    print("Source", source, "Target", target, "MaxDepth", max_depth)
    if g.dfs(source, target, max_depth): print("The target is reachable in ", g.count, "steps")
    else: print("Target is not reachable in given depth")

if __name__ == "__main__":
    main()
