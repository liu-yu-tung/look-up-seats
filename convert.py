import json
import csv

from collections import defaultdict

keys = ["oldAudi", "oldSeat", "newAudi", "newSeat", "oldPos", "newPos"]

def createSeatDic(myList):
    dd = {}
    for i in range(6):
        dd[keys[i]] = myList[i]
    return dd

input_file_name = "./seats.csv"
output_file_name = "./seats.json"

seats_arr = list(csv.reader(open(input_file_name)))
seats_json = {}

d = defaultdict(dict)

for i in range(len(seats_arr)):
    d[str(seats_arr[i][0])][str(i)] = createSeatDic(seats_arr[i])

print(dict(d))

s = str(dict(d))
ss = ""
for i in range(len(s)):
    if s[i] == "'":
        ss = ss + '"'
    else:
        ss = ss + s[i]

print(ss)
with open(output_file_name, "w") as f:
    f.write(ss)
