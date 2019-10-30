import csv

array_words  = []
with open('sgb-words.txt') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        array_words.append(row[0])


print(len(array_words))
