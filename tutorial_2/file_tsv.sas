proc import datafile="/folders/myfolders/testdata/data.tsv"
out = fromfile1
dbms = dlm
replace;
delimiter='09'x;
getnames = yes;
run;