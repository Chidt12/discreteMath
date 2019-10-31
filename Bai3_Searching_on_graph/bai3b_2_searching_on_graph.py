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
        cnt = 0
        for i in range(len(word)):
            if i != 0 and word[i] in w:
                if word.count(word[i]) == w.count(word[i]):
                    cnt += 1
        if cnt == 4:
            array.append(w)
    return array

class GraphDirected:

    def __init__(self):
        self.graph = defaultdict(list)
    def add_edge(self,word, incident):
        self.graph[word].append(incident)

g = GraphDirected()
for word in array_words:
    array_incident = list_incident(word, array_words)
    for w in array_incident:
        g.add_edge(word, w)