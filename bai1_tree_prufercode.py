array_data = [[0,2],[0,3],[2,4],[2,6],[2,9],[6,1],[6,5],[9,7],[9,8]]

class Node:
    def __init__(self,value):
        self.value = value
        self.neighbors = []

    def isLeaf(self):
        if len(self.neighbors) <= 1:
            return True
        else:
            return False

    def addneighbor(self,neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
        if self not in neighbor.neighbors:
            neighbor.neighbors.append(self)

    def deleteneighbor(self,neighbor):
        if neighbor in self.neighbors:
            self.neighbors.remove(neighbor)

array_nodes = []
for i in range(len(array_data)+1):
    array_nodes.append(Node(i))

for x,y in array_data:
    array_nodes[x].addneighbor(array_nodes[y])

prufercode = []

def genPruferCode(array):
    if len(array) == 2:
        return
    else:
        allleaf = []
        min = Node(1000000)
        for node in array:
            if node.isLeaf():
                if node.value <= min.value:
                    min = node
        array.remove(min)
        for neighbor in min.neighbors:
            neighbor.neighbors.remove(min)
        prufercode.append(min.neighbors[0].value)
        genPruferCode(array)

genPruferCode(array_nodes)

print(prufercode)
