from uuid import getnode


class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node: Node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []
    
    def addEdge(self, edge: Edge):
        src = edge.getSource()
        dest = edge.getDestination()

        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node: Node):
        return self.edges[node]
    
    def hasNode(self, node: Node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
    
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    
    return g

#print(buildCityGraph(Graph))


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint=False):
    path = path + [start]
    if toPrint:
        print("Current DFS path: ", printPath(path))

    if start == end:
        return path
    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print("Already visited", node)
    return shortest

def shortestPath(graph, start, end, toPrint=False):
    return DFS(graph, start, end, [], None, toPrint)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination), toPrint=True)
    if sp != None:
        print(f"Shortest path from {source} to {destination} is {printPath(sp)}")
    else:
        print(f"There is no path from {source} to {destination}")

print("DFS algorithm:")
testSP('Chicago', 'Boston')
testSP('Boston', 'Phoenix')
print("DFS end #########")


def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrint:
        print('Current BFS path: ', printPath(pathQueue))
    while len(pathQueue) != 0:
        tmpPath = pathQueue.pop(0)
        print('Current BFS path: ', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None

def shortestPath(graph, start, end, toPrint=False):
    return BFS(graph, start, end, toPrint)

print("BFS algorithm:")
testSP('Chicago', 'Boston')
testSP('Boston', 'Phoenix')
print("BFS end #########")



    
