# a school has following rules for grading system
# below 25-f
#25 to 45-e
#45 to 50-o
#50 to 60-c
#60 to 80-b
#80 to above 80-a
# ask user to entr marks and print the corresponding grade.
grade="grade"
marks=int (input("entr your marks:"))
if marks>80:
       print(grade="a")
elif marks>60 - 80:
     print(grade="b")
elif marks>50 - 60: 
     print(grade="c")  
elif marks>45 - 50: 
     print(grade="d")  
elif marks>25 - 45: 
     print(grade="e")  
elif marks <25: 
     print(grade="f")                 
