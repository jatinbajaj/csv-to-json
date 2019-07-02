import csv
import json

mydict = {}
outfile = open('out.json','w')
rep = 'O'
with open('test.csv','r') as csvfile: #Opening test.csv
    csvreader = csv.reader(csvfile) #Reading the csv file into csvreader object

#    fields=csvreader.
    for col in csvreader: #Go through all columns and dump it into json file
        out=json.dumps(col)

outfile.write(out)




