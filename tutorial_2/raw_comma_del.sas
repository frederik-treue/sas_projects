Data outdata2;
Infile Datalines delimiter=',';
Input age gender $ dept obs1 obs2 ob3;
datalines;
1,F,3,17,6,24
1,M,1,19,25,7
3,M,4,24,10,20
3,F,2,19,23,8
2,F,1,14,23,12
2,M,5,1,23,9
3,M,1,8,21,7
1,F,1,7,7,14
3,F,2,2,1,22
1,M,5,20,5,2
3,M,4,21,8,18
1,M,4,7,9,25
2,F,5,10,17,20
3,F,4,21,25,7
3,F,3,9,9,5
3,M,3,7,21,25
2,F,1,1,22,13
2,F,5,20,22,5
;
proc print;
run;
