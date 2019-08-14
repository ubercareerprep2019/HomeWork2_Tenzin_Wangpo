"""
            UNDIRECTED GRAPH

Exercise 1

Exercise 4: Minimum Edges between two given Nodes

"""

class GraphNode:
    def __init__(self, data):
        self.data = data

    def getData(self):
        return self.data

class GraphWithAdjacencyList:
    def __init__(self):
        self.adjNodes = dict()

    def nodeInAdjNode(self, key):
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
                self.adjNodes[i].remove(nodeInList)
            del self.adjNodes[nodeInList]

    def addEdge(self, node1, node2):
        source_NodeInList = self.nodeInAdjNode(node1)
        dest_NodeInList = self.nodeInAdjNode(node2)

        if not (source_NodeInList and dest_NodeInList):
            return
        else:
            self.adjNodes[source_NodeInList].append(dest_NodeInList)
            self.adjNodes[dest_NodeInList].append(source_NodeInList)

    def removeEdge(self, node1, node2):
        source_NodeInList = self.nodeInAdjNode(node1)
        dest_NodeInList = self.nodeInAdjNode(node2)
        if not (source_NodeInList and dest_NodeInList):
            return
        else:
            self.adjNodes[source_NodeInList].remove(dest_NodeInList)
            self.adjNodes[dest_NodeInList].remove(source_NodeInList)

    def getAdjNodes(self, key):
        nodeInList = self.nodeInAdjNode(key)
        if not nodeInList:
            return
        else:
            return [node.getData() for node in self.adjNodes[nodeInList]]


    # EXERCISE 4: Minimum number of edges between two nodes of a Graph
    def minNumberOfEdges(self, source, destination):
        #using a BFS to find the minimum edges between two given nodes
        if source == destination:
            return 0
        source_NodeInList = self.nodeInAdjNode(source)
        dest_NodeInList = self.nodeInAdjNode(destination)

        if not (source_NodeInList and dest_NodeInList):
            return
        else:
            neighborList = list()
            parent_list = list()
            parent_list.append(source_NodeInList)
            neighborList += self.adjNodes[source_NodeInList]
            number_of_edges = 1

            while neighborList:
                if dest_NodeInList in neighborList:
                    return number_of_edges
                else:
                    parent_list = list(neighborList)
                    neighborList = list()
                    for i in parent_list:
                        neighborList += self.adjNodes[i]
                    number_of_edges += 1

def test():
    listNodes = [7,2,4,6,0]

    myGraph = GraphWithAdjacencyList()
    for i in listNodes:
        myGraph.addNode(i)
    myGraph.addEdge(7, 2)
    myGraph.addEdge(7, 4)
    myGraph.addEdge(6, 0)
    myGraph.addEdge(4, 6)
    myGraph.addEdge(0, 2)
    myGraph.addEdge(4, 2)

    print("Adjacent nodes of 7 are: {} ".format(myGraph.getAdjNodes(7)))
    print("Adjacent nodes of 4 are: {} ".format(myGraph.getAdjNodes(4)))
    print("Adjacent nodes of 2 are: {} ".format(myGraph.getAdjNodes(2)))
    print("Adjacent nodes of 6 are: {} ".format(myGraph.getAdjNodes(6)))
    print("Adjacent nodes of 0 are: {} ".format(myGraph.getAdjNodes(0)))
    print("\nMinimum Edges between 7 to 6 is {}".format(myGraph.minNumberOfEdges(7, 6)))

    nodeForMinEdges = [0,1,2,3,4,5,6]
    myGraphForMinEdges = GraphWithAdjacencyList()
    for i in nodeForMinEdges:
        myGraphForMinEdges.addNode(i)
    myGraphForMinEdges.addEdge(3, 4)
    myGraphForMinEdges.addEdge(4, 5)
    myGraphForMinEdges.addEdge(4, 0)
    myGraphForMinEdges.addEdge(4, 6)
    myGraphForMinEdges.addEdge(5, 2)
    myGraphForMinEdges.addEdge(2, 1)
    myGraphForMinEdges.addEdge(2, 0)
    myGraphForMinEdges.addEdge(1, 0)

    print("\n-----------New Graph for Minimum edges------------")
    print("\nMinimum Edges between 3 to 1 is {}".format(myGraphForMinEdges.minNumberOfEdges(3, 1)))
    print("\nMinimum Edges between 6 to 5 is {}".format(myGraphForMinEdges.minNumberOfEdges(6, 5)))
    print("\nMinimum Edges between 2 to 3 is {}".format(myGraphForMinEdges.minNumberOfEdges(2, 3)))

if __name__ == "__main__":
    test()

""" --------------- RUN -------------
Graph looks like 
            
            7 ---  2
            |     / \
            |    /   \ 
            |   /     0
            |  /     /
            | /     /
            4 ---- 6 
Adjacent nodes of 7 are: [2, 4] 
Adjacent nodes of 4 are: [7, 6, 2] 
Adjacent nodes of 2 are: [7, 0, 4] 
Adjacent nodes of 6 are: [0, 4] 
Adjacent nodes of 0 are: [6, 2]

Shortest Path from 7 to 6 is 2


-----------New Graph for Minimum edges------------

New Graph for minimum edges between two nodes
        3 ---- 4 ---- 0 ----- 1
              /|       \     /
             / |        \   /
            /  6         \ /
           5 -------------2

Shortest Path from 3 to 1 is 3

Shortest Path from 6 to 5 is 2

Shortest Path from 2 to 3 is 3

"""
