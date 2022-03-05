import json 
txt = open("word.txt")

arr = []
for x in txt.readlines():
    arr.append(x.replace("\n",""))

json_file = open("allowed-words.json","w")
json.dump({"words":arr},json_file)