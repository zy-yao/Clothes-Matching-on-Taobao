import csv
for i in range(0,12):
    with open('/Users/YAO/.spyder-py3/ForPython/new method/rule1_weekresult/result'+str(i+1)+'_1.csv') as origin_f:
        with open('/Users/YAO/.spyder-py3/ForPython/new method/rule1_weekresult2/result'+str(i+1)+'_2.csv','w',newline='') as new_f:
            reader = csv.reader(origin_f)
            writer = csv.writer(new_f)
            writer.writerow(['testItem','matchItem'])
            for row in reader:
                for i in range(0,len(row)):
                    for j in range(0,len(row)):
                        line = []
                        if i != j:
                            line.append(row[i])  
                            line.append(row[j])
                            writer.writerow(line)

