#!/usr/bin/env python3

'''
this generates some random data for use with SAS, with names for the different columns
'''

import csv
import random
import math
import xlwt

def main():
    names = ['ID', 'obs1', 'obs2'];
    data = [names];
    for i in range(30):
        data.append([int(random.random()*100)+1, random.random(), math.exp(random.random()*10)])
    book = xlwt.Workbook(encoding='utf-8');
    sheet1 = book.add_sheet("sheet1");
    
    for linenr in range(31):
        for colnr in range(3):
            sheet1.write(linenr,colnr,data[linenr][colnr]);
    book.save("../testdata/data.xls");
    
    with open('../testdata/data.tsv','w') as myfile:
        writer = csv.writer(myfile, dialect='excel', delimiter='\t')
        for line in data:
            writer.writerow(line)

    with open('../testdata/data.txt','w') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        for line in data:
            writer.writerow(line)

    with open('../testdata/data.csv','w') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        for line in data:
            writer.writerow(line)

    with open('../testdata/data.ssv','w') as myfile:
        writer = csv.writer(myfile, dialect='excel', delimiter=' ')
        for line in data:
            writer.writerow(line)

    with open('../testdata/data.osv','w') as myfile:
        for line in data:
            out = str(line[0]);
            if random.random() < 0.5:
                out=out+":"+str(line[1])
            else:
                out=out+"\t"+str(line[1])
            if random.random() < 0.5:
                out=out+":"+str(line[2])
            else:
                out=out+"\t"+str(line[2])
            myfile.write(out+"\n");

    names2 = ['ID','Age','Gender','Dept']
    data2 = [names2]
    for i in range(30):
        if random.random() < .5:
            gen = 'M'
        else:
            gen = 'F'
        if random.random() < .5:
            dept = 'Corporate'
        else:
            dept = 'Sales'

        data2.append([int(random.random()*100)+1,int(random.random()*50)+20,gen,dept])
    with open('../testdata/data2.csv', 'w') as myfile:
        writer = csv.writer(myfile, dialect='excel')
        for line in data2:
            writer.writerow(line)
        
if __name__=="__main__":
    main()
