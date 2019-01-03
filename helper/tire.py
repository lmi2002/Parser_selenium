import csv
from properties.prop_csv import Csv
lst = []
lst_end = []
with open(r'C:\Users\anokhin\Desktop\tare.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        ar = row[0].split(';')
        lst.append(ar)

for it in lst:
    lst_1 = []
    art = it[0]
    mx = it[2]
    mi = it[3]
    lst_1 = [art]

    for r in lst:
        art1 = r[0]
        h = r[1]
        if h <= mx and h >= mi:
            lst_1.append(art1)

    lst_end.append(lst_1)

with open(r'C:\Users\anokhin\Desktop\parser\tare_result.csv', 'w', newline='', errors='ignore') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for line in lst_end:
        writer.writerow(line)
