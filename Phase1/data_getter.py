import json

with open('usernames.json', 'r') as f1, open('usernames2.json', 'r') as f2:
    dict1 = json.load(f1)
    dict2 = json.load(f2)
    
with open('merged.json', 'r') as fp:
    dict3 = json.load(fp)

dict1.update(dict2)
dict1.update(dict3)
with open('mergedFinal.json', 'w') as fp:
    json.dump(dict1, fp)

new = ''
for i in dict1:
    new += i + '\n'
with open('dequed', 'w') as fp:
    fp.write(new)
