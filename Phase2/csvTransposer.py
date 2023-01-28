####import csv
####from itertools import zip_longest
####a = zip_longest(*csv.reader(open("First128.csv", "rb")))
####csv.writer(open("output.csv", "wb")).writerows(a)
##
##from csv import reader, writer 
##with open('First128.csv') as f, open('destination.csv', 'w') as fw: 
##    writer(fw, delimiter=',').writerows(zip(*reader(f, delimiter=',')))

##new = ''
with open('Instagram CSV File.csv', 'r') as fp:
    data = fp.read().split('\n')

for i in range(5):
    print(len(data[i].split(',')))
