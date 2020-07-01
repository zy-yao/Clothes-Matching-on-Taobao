import csv
with open('II.csv') as origin_f:
    with open('ruel1_final.csv','w',newline='') as new_f:
        reader = csv.reader(origin_f)
        writer = csv.writer(new_f)
        for row in reader:
            row[0] = row[0] + ' ' +row[1]
            del row[1]
            writer.writerow(row)
