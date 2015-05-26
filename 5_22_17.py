sub1 = raw_input("Enter your subject")
sub2 = raw_input("Enter your subject")
sub3 = raw_input("Enter your subject")
sub4 = raw_input("Enter your subject")

print "1. ",sub1
grade1 = raw_input("Enter your grade")
print "2. ", sub2
grade2 = raw_input("Enter your grade?")
print "3. ", sub3
grade3 = raw_input("Enter your grade")
print "4. ", sub4
grade4 = raw_input("Enter your grade")

if grade1 == "A":
    grade1 = 4.00
elif grade1 == "":
    grade1 = 3.00
elif grade1 == "C":
    grade1 = 2.00
elif grade1 == "D":
    grade1 = 1.00
elif grade1 == "F":
    grade1 = 0.00
    
print grade1

if grade2 == "A":
    grade2 = 4.00
elif grade2 == "B":
    grade2 = 3.00
elif grade2 == "C":
    grade2 = 2.00
elif grade2 == "D":
    grade2 = 1.00
elif grade2 == "F":
    grade2 = 0.00
    
print grade2

if grade3 == "A":
    grade3 = 4.00
elif grade3 == "B":
    grade3 = 3.00
elif grade3 == "C":
    grade3 = 2.00
elif grade3 == "D":
    grade3 = 1.00
elif grade3 == "F":
    grade3 = 0.00
    
print grade3

if grade4 == "A":
    grade4 = 4.00
elif grade4 == "B":
    grade4 = 3.00
elif grade4 == "C":
    grade4 = 2.00
elif grade4 == "D":
    grade4 = 1.00
elif grade4 == "F":
    grade4 = 0.00
    
print grade4 
