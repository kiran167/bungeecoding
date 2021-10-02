import csv
from operator import add
file=open(r"C:\Users\chait\Downloads\internship-test2-master\internship-test2-master\input\question-2\main.csv")
csvreader = csv.reader(file)
f=open(r'C:\Users\chait\Downloads\internship-test2-master\internship-test2-master\output\answer-1\output2.csv','w')
writer=csv.writer(f)
c=0
header=[]
rows=[]
header=next(csvreader)
header=["occupation","min","max"]
for row in csvreader:
    rows.append(row)
writer.writerow(header)
res={}
for i in range(len(rows)):
    r=rows[i]
    y=r[3]
    if y not in res:
        res[y]=[]
    else:
        res[y].append(r[1])
for i in res:
    l=[]
    l.append(min(res[i]))
    l.append(max(res[i]))
    res[i]=l
for i in sorted(res.keys()):
    d=[]
    d.append(i)
    d.append(res[i][0])
    d.append(res[i][1])
    writer.writerow(d)