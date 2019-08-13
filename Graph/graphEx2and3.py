"""
I am assuming the graph is directed (by looking the example given in file)

It's some what similar to Ex1 (undirected Graph) but have to change
little bits in adjacent list since it directed graph

Also GraphNode object need to have member visited since it will help us to find the DFS and BFS
"""

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.visited = False

    def getData(self):
        return self.data

    def getVisited(self):
        return self.visited

    def setVisitedTrue(self):
        self.visited = True

class DirectedGraphWithAdjList:
    def __init__(self):
        self.adjNodes = dict()

    def nodeInAdjNode(self, key):
        # to check there will be no duplicate node
        for node in self.adjNodes.keys():
            if key == node.getData():
                return node
        return False

    def addNode(self, key):
        nodeInList = self.nodeInAdjNode(key) #this will return node if the node is already exist in the class adjNode
        if nodeInList:
            # if the node is already in class adjNode then it do not add the node
            return
        else:
            # if its new node, then insert the node as key in class adjNode with empty list as value
            # will use that empty list next time for adding edges with different nodes
            self.adjNodes[GraphNode(key)] = []

    def removeNode(self, key):
        nodeInList = self.nodeInAdjNode(key) # if it return nothing, then key is not in the class adjNode
        if not nodeInList:
            return
        else:
            # the key node will be present in all the node in its adjacency list
            # so first take a look at key node's value and then jump to those value and delete the key
            # after all of that, del the key from dictionary
            for i in self.adjNodes[nodeInList]:
                try:
                    self.adjNodes[i].remove(nodeInList)
                except:
                    continue
            del self.adjNodes[nodeInList]

    def addEdge(self, node1, node2):
        source_NodeInList = self.nodeInAdjNode(node1)
        dest_NodeInList = self.nodeInAdjNode(node2)

        if not (source_NodeInList and dest_NodeInList):
            # if one of the node or both node are not in adjList, then do nothing
            return
        else:
            self.adjNodes[source_NodeInList].append(dest_NodeInList)

    def removeEdge(self, node1, node2):
        source_NodeInList = self.nodeInAdjNode(node1)
        dest_NodeInList = self.nodeInAdjNode(node2)

        if not (source_NodeInList and dest_NodeInList):
            return
        else:
            self.adjNodes[source_NodeInList].remove(dest_NodeInList)

    def getAdjNodes(self, key):
        nodeInList = self.nodeInAdjNode(key)
        if not nodeInList:
            return
        else:
            return [node.getData() for node in self.adjNodes[nodeInList]]

    def DFS(self, key):
        nodeInList = self.nodeInAdjNode(key)

        if not nodeInList:
            return
        else:
            nodeInList.setVisitedTrue()
            print(nodeInList.getData(), end= " ")

            for i in self.adjNodes[nodeInList]:
                if i.visited is False:
                    self.DFS(i.getData())

    def BFS(self, key):
        nodeInList = self.nodeInAdjNode(key)

        if not nodeInList:
            return
        else:
            neighborNodes = list()
            nodeInList.setVisitedTrue()
            neighborNodes.append(nodeInList)

            while neighborNodes:
                nodeToPrint = neighborNodes.pop(0)
                print(nodeToPrint.getData(), end=" ")
                for i in self.adjNodes[nodeToPrint]:
                    if i.visited == False:
                        neighborNodes.append(i)
                        i.setVisitedTrue()

def test():
    listNodes = [2,0,1,3]

    myGraph = DirectedGraphWithAdjList()
    for i in listNodes:
        myGraph.addNode(i)
    myGraph.addEdge(2, 0)
    myGraph.addEdge(2, 1)
    myGraph.addEdge(2, 3)
    myGraph.addEdge(0, 2)
    myGraph.addEdge(0, 1)

    print("Adjacent nodes of 2 are: {} ".format(myGraph.getAdjNodes(2)))
    print("Adjacent nodes of 0 are: {} ".format(myGraph.getAdjNodes(0)))
    print("Adjacent nodes of 1 are: {} ".format(myGraph.getAdjNodes(1)))
    print("Adjacent nodes of 3 are: {} ".format(myGraph.getAdjNodes(3)))

    print("the DFS is: " ,end=" ")
    myGraph.DFS(2)

    myGraphForBFS = DirectedGraphWithAdjList()
    BFSNode = [1,2,3,4,5,6,7,8,9]
    for i in BFSNode:
        myGraphForBFS.addNode(i)

    myGraphForBFS.addEdge(1, 2)
    myGraphForBFS.addEdge(1, 9)
    myGraphForBFS.addEdge(9, 7)
    myGraphForBFS.addEdge(9, 3)
    myGraphForBFS.addEdge(7, 6)
    myGraphForBFS.addEdge(3, 4)
    myGraphForBFS.addEdge(3, 6)
    myGraphForBFS.addEdge(3, 5)
    myGraphForBFS.addEdge(8, 5)
    myGraphForBFS.addEdge(7, 8)

    print("\n\n-------------- BFS ------------------")
    print("the BFS is: ", end=" ")
    myGraphForBFS.BFS(1)

if __name__ == "__main__":
    test()

""" ----------- RUN --------------
Adjacent nodes of 2 are: [0, 1, 3] 
Adjacent nodes of 0 are: [2, 1] 
Adjacent nodes of 1 are: [] 
Adjacent nodes of 3 are: [] 
the DFS is:  2 0 1 3 

-------------- BFS ------------------
the BFS is:  1 2 9 7 3 6 8 4 5 

"""
