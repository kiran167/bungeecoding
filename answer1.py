import csv
from operator import add
file=open(r"C:\Users\chait\Downloads\internship-test2-master\internship-test2-master\input\question-1\main.csv")
csvreader = csv.reader(file)
f=open(r'C:\Users\chait\Downloads\internship-test2-master\internship-test2-master\output\answer-1\output1.csv','w')
writer=csv.writer(f)
c=0
header=[]
rows=[]
header=next(csvreader)
for row in csvreader:
    rows.append(row)
del header[2]
writer.writerow(header)
res=rows[0]
y=res[0]
for i in range(1,len(rows)):
    if i%10==0:
        del res[2]
        writer.writerow(res)
        res=rows[i]
        y=res[0]
    else:
        l=rows[i]
        p=l[1]
        res=[int(res[j]) + int(l[j]) for j in range(len(l))]
        res[0]=y
        res[1]=p
del res[2]
writer.writerow(res)