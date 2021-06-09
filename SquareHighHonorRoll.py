# PROGRAM: SquareHighHonorRoll.py
# COURSE: ITSE 1302 Final Project
# AUTHOR: Stacey Nash
# DATE: April 30, 2021
# DESCRIPTION: The program will process a file containing
# student information, determine A and B Honor Roll
# students, display summary statistics, and create two separate .dat
# files (one for each honor roll).


# Each student record contains name, id, grade
# open 'grades.dat'
file = open("grades.dat")
total = []
A = []  # A Honor Roll
B = []  # B Honor Roll
N = []  # No Honor Roll

# Loop (read) each record from the file, removing the \n character (.strip());
# .strip() removes the \n from str data type
for student in file:
  # split the record into fields based the delimiter (comma)
    studentList = student.split(",")    # .split() will create a list out of a string
    name = studentList[0]               # 'name' located at index 0; string data type - no casting needed
    idNum = int(studentList[1])         # 'ID' located at index 1; numerical data type requires casting as an int
    grade = int(studentList[2])         # 'grade' located at index 2; 
    if (grade >= 90):
        A.append(name)                  # names separated and added to student list A, B, or C, based on grade
    elif (80 <= grade < 90):
        B.append(name)
    else:
        N.append(name)

##print(A) - test if looping for A students worked
##print(B) - see if 'elif' (look Mr. Coffman - elif! :-) for B students worked
##print(N) - see if 'else' statement worked
 
# close the file right after the loop is done
file.close()


# sort A and B honor roll
A.sort()
B.sort()

# len() determines how many items are in the list  
total = len(A) + len(B) + len(N)    

print("\nProcessing student grades...")
print("Processing complete.\n")
print("SUMMARY STATISTICS")
print("------------------")
print("Total students : " + str(total)) # len() must be cast as string to avoid TypeError  

pA = (len(A) / total) * 100  # calculate percentage of A Honor Roll students
pB = (len(B) / total) * 100  # calculate percentage of B Honor Roll students

# format() inserts the values into the {} sequentially
#  (f{1:.2}%) resulted in ValueType error
print("\nA Honor Roll Students : {} ({}%)" .format(len(A), pA))         
print("B Honor Roll Students : {} ({}%)" .format(len(B), pB))   

# write A student names to 'AHonorRoll.dat'
outputFile = open("AHonorRoll.dat", "w") # defaults to 'text' file
for record in A:
    outputFile.write(record + "\n")
outputFile.close()
print("\nAHonorRoll.dat file created...")

# write B student names to 'BHonorRoll.dat'
outputFile = open("BHonorRoll.dat", "w") 
for record in B:
    outputFile.write(record + "\n")
outputFile.close()
print("BHonorRoll.dat file created...")

# Unable to display the sorted .dat files as vertical lists (?)

# Thank you for your generosity and humility, Mr. Coffman.
# You are instrumental in my pending success.
# God bless you and your family exponentially. 

print("\nEnd of program.")

