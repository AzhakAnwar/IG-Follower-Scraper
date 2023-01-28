import json
##def dataManager():
with open('mergedFinal.json', 'r') as fp:
    dataDict = json.load(fp)

allKeys = set()
for i in dataDict:
    allKeys.update(dataDict[i])
column = ''
row = ''
for i in allKeys:
    column += i + '\n'
    row += ',' + i

with open('output.csv', 'w') as fp:
    fp.write(row)
    fp.write(column)

##dataManager()
