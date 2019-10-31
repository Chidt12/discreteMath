import csv


list_edges = []
start_robot1 = 0
start_robot2 = 0
end_robot1 = 0
end_robot2 = 0
num_vertices = 0
num_edges = 0
distance_allowed = 0
with open('testcase1.txt') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=" "))
    for i in range(len(csv_reader)):
        if i == 0:
            num_vertices = int(csv_reader[i][0])
            num_edges = int(csv_reader[i][0])
        elif i <= num_edges:
            list_edges.append(csv_reader[i])
        elif i == num_edges + 1:
            start_robot1 = csv_reader[i][0]
            start_robot2 = csv_reader[i][1]
        elif i == num_edges + 2:
            end_robot1 = csv_reader[i][0]
            end_robot2 = csv_reader[i][1]
        else:
            distance_allowed = csv_reader[i][0]


