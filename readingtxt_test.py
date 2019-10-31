import csv

setvertices = set()
setedges = []

with open('example.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=" ")
    line_count = 0
    for row in csv_reader:
        setedges.append(row)
        for i in row:
            setvertices.add(i)

