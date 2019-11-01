import csv
import sys
sys.setrecursionlimit(10**9)

array_words  = []
with open('sgb-words.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        array_words.append(row[0])

def list_incident(word, array_words):
    array = []
    for w in array_words:
        wcnt = 0
        for i in range(len(word)):
            if w[i] != word[i]:
                wcnt+=1
        if wcnt == 1:
            array.append(w)
    return array

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self,word):
        self.vertices[word] = list_incident(word, array_words)

g = Graph()
for word in array_words:
    g.add_vertex(word)

def BFS(g, vertex_start, discovered):
    level = [vertex_start]
    while len(level) > 0:
        next_level = []
        for u in level:
            for v in g.vertices[u]:
                if v not in discovered:
                    discovered[v] = [v, u]
                    next_level.append(v)
        level = next_level

def construct_path(start, end, graph=g):
    discovered = {start: None}
    BFS(graph, start, discovered)
    path = []
    if end in discovered:
        path.append(end)
        walk =  end
        while walk != start:
            e = discovered[walk]
            if e is not None:
                for x in e:
                    if x!=walk:
                        parent = x
                        path.append(parent)
                        walk = parent
        path.reverse()
    else:
        return "Can't find"
    return path

def BFS_complete(g):
    forest = {}
    count = 0
    for u in g.vertices.keys():
        if u not in forest:
            forest[u] = None
            BFS(g, u, forest)
            count +=1
    return count

print(BFS_complete(g)) #Chỉ ra số thành phần liên thông
print(construct_path("world", "wolds")) #Input lần lượt là từ bắt đầu và từ kết thúc


