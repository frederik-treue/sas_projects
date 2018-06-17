proc import datafile="/folders/myfolders/testdata/data.csv"
out = fromfile1
dbms = csv
replace;
getnames = yes;
run;