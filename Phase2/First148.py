import json

with open('mergedFinal.json', 'r') as fp:
    dataDict = json.load(fp)

column = ''
row = ''
allNames = []

firstFollowers = list(dataDict.keys())

allNames.extend(firstFollowers)
dictValues = set()

for i in dataDict.values():
    dictValues.update(i)

allNames.extend(dictValues.difference(allNames))
       
print(len(allNames))
print(len(firstFollowers))

while '' in allNames:
    allNames.remove('')
    
for i in firstFollowers:
    followers = dataDict[i]
    column += i
    for j in allNames:
        if j in followers:
            column += ',1'
        else:
            column += ',0'
    column += '\n'

for i in allNames:
    row += ',' + i
with open('First128.csv', 'w') as fp:
    fp.write(row + '\n')
    fp.write(column)
