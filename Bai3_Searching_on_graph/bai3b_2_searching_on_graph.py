import csv
import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

array_words  = []
with open('sgb-words.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        array_words.append(row[0])

def list_incident(word, array_words):
    array = []
    for w in array_words:
        if w != word:
            cnt = 0
            for i in range(len(word)):
                if i != 0 and word[i] in w:
                    if word[1:].count(word[i]) <= w.count(word[i]):
                        cnt += 1
            if cnt == 4:
                array.append(w)
    return array

class GraphDirected:

    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self,word, incident):
        self.graph[word].append(incident)

    def BFS(self, start, discovered):
        level = [start]
        while len(level) > 0:
            nextlevel = []
            for vertex in level:
                for v in self.graph[vertex]:
                    if v not in discovered:
                        discovered[v] = [vertex, v]
                        nextlevel.append(v)
            level = nextlevel

    def construct_path(self, start, end):
        discovered = {start: None}
        self.BFS(start, discovered)
        path = []
        if end in discovered:
            path.append(end)
            walk =  end
            while walk != start:
                e = discovered[walk]
                if e is not None:
                    parent = e[0]
                    path.append(parent)
                    walk = parent
            path.reverse()
        else:
            return "Can't find"
        return path


g = GraphDirected()
for word in array_words:
    array_incident = list_incident(word, array_words)
    for w in array_incident:
        g.add_edge(word, w)

print(g.construct_path("words","graph"))
# thêm input lần lượt là từ đầu và từ cuối
