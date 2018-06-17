proc import datafile="/folders/myfolders/testdata/data.txt"
out = fromfile1
dbms = dlm
replace;
delimiter=',';
getnames = yes;
run;