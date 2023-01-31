

















totalgrades = []

try:
        inpx = int(input("how many As do you have?"))
        inpx2 = int(input("how many Bs do you have?"))
        inpx3 = int(input("how many Cs do you have?"))
        inpx4 = int(input("how many Ds do you have?"))
        inpx5 = int(input("how many Fs do you have?"))
except ValueError:
        print("Error, not a number inputted, please rerun script!")

for i in range(inpx):       # automated code segment that adds the number of A's, B's, C's, D's, and F's to a list
    totalgrades.append('A') # AUTOMATED BY GITHUB-COPILOT (https://copilot.github.com/)
for i in range(inpx2):
    totalgrades.append('B')
for i in range(inpx3):
    totalgrades.append('C')
for i in range(inpx4):
    totalgrades.append('D')
for i in range(inpx5):
    totalgrades.append('F')





# function pulled from CS 1351 project transcript reader


def CalculateMAJORGPA(c:list[str])->int: # differnet but similiar function except it checks if class it is major related before calculating/adding it
    GPAtotal = 0
    gradedClass = 0

    for element in c:

        if element == 'A' or element =='A+':
                GPAtotal += 4.0 
                gradedClass += 1
        elif element == 'A-':
                GPAtotal += 3.7
                gradedClass += 1
        elif element == 'B+':
                GPAtotal += 3.3
                gradedClass += 1
        elif element == 'B':
                GPAtotal += 3.0
                gradedClass += 1
        elif element == 'B-':
                GPAtotal += 2.7
                gradedClass += 1
        elif element == 'C+':
                GPAtotal += 2.3
                gradedClass += 1
        elif element == 'C':
                GPAtotal += 2.0
                gradedClass += 1
        elif element == 'C-':
                GPAtotal += 1.7
                gradedClass += 1
        elif element == 'D+':
                GPAtotal += 1.3
                gradedClass += 1
        elif element == 'D':
                GPAtotal += 1.0
                gradedClass += 1
        elif element == 'F':
                GPAtotal += 0.0
                gradedClass += 1
        else:
                GPAtotal += 0

    # for element in b:
    #     if b[element] == 'P' or b[element] == 'F' or b[element] = ''
    if gradedClass == 0: # checks/prevents divided by zero error if no classes eligible for gpa count
        gradedClass = 1 

    GPAtotal = GPAtotal/gradedClass

    return GPAtotal

gpa = CalculateMAJORGPA(totalgrades)
print(f"\n your total gpa is {gpa}")


HSFscholar = 3
dsfscholar = 3.5
academicstand = 2.2 #academic standing for University of Denver
print("checking current scholarship eligibality; ")

if gpa >= HSFscholar:
        print("\n You are eligible for the Hispanic scholarship Fund")
else: 
        print("\n You are NOT eligible for the Hispanic scholarship Fund")
if gpa >= dsfscholar:
        print("\n You are eligible for the DSF Scholarship")
else:
        print("\n You are NOT eligible for the Hispanic scholarship Fund")
if gpa >= academicstand:
        print("\n You are in good academic standing")
else:
        print("\n You are not in good academic standing")


# this script is an improved version of a gpa calculator we had made in CS 1351 at University of Denver
# Meant to quickly calculate possible gpa based on current grades/transcript
# TODO: Integrate a UI (tkinter or web/html) & more accurate grade grading
# TODO eventually: Integrate an API/Canvas  and create small application that pulls your current Canvas grades and displays a report/summarize of future
# impact, future gpa, eligiblity etc. 