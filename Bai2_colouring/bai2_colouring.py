import csv
import graphviz as gv

setvertices = set()
setedges = []
startVertexDraw = 0
colors = ['orange','red','yellow','green','pink','blue','grey','black','cyan','brown','violet','lime','magenta','maroon','indigo','cornsilk','gold','olive','peru','firebrick']

with open('bai2_coloring_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    line_count = 0
    for row in csv_reader:
        if len(row) != 1:
            setedges.append(row)
            for i in row:
                setvertices.add(i)
        else:
            startVertexDraw = row[0]


def choosecolour(array_color_incident=[0,1,4]):
    true_color = 1
    while true_color in array_color_incident:
        true_color +=1
    return true_color

class GraphUndirected:

    def __init__(self):
        self.edges = {}
        self.vertices_colour = {}

    def add_vertex(self, value):
        self.edges[value] = {}
        self.vertices_colour[value]= 0

    def add_edge(self, vertex, opposite):
        self.edges[vertex][opposite] = [vertex,opposite]

    def incident_edge(self, vertex):
        for edge in self.edges[vertex].values():
            yield edge

    def find_opposite(self,edge, vertex):
        for v in edge:
            if v != vertex:
                return v

    def DFS_colouring(self, vertex_start, dicovered_list):
        array_color_incident = set()
        for edge in self.incident_edge(str(vertex_start)):
            v = self.find_opposite(edge, str(vertex_start))
            array_color_incident.add(self.vertices_colour[v])
        self.vertices_colour[str(vertex_start)] = choosecolour(array_color_incident)

        for edge in self.incident_edge(str(vertex_start)):
            v = self.find_opposite(edge,str(vertex_start))
            if v not in dicovered_list:
                dicovered_list[v] = edge
                self.DFS_colouring(v, dicovered_list)

    # def construct_path(self, start, end, dicovered_list):
    #     path=[]
    #     v= str(end)
    #     u = str(start)
    #     if v in discovered_list:
    #         path.append(v)
    #         walk = v
    #         while walk != u:
    #             e = discovered_list[walk]
    #             parent = self.find_opposite(e, walk)
    #             path.append(parent)
    #             walk = parent
    #         path.reverse()
    #     return path

g = GraphUndirected()
for i in setvertices:
    g.add_vertex(i)

for i,j in setedges:
    g.add_edge(i,j)
    g.add_edge(j,i)

result = {str(startVertexDraw):None}
g.DFS_colouring(startVertexDraw,result)


# DRAW GRAPHIZ FILE
graph_draw = gv.Graph(format='png')
for node in g.vertices_colour:
    graph_draw.node(node, _attributes={'color':colors[g.vertices_colour[node]], 'style': 'filled'})

for edge in setedges:
    graph_draw.edge(str(edge[0]),str(edge[1]))
graph_draw.view()
print(graph_draw.source) 

filename = graph_draw.render(filename='bai2_coloring.dot')