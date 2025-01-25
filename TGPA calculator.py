# CODED BY DEXTER

# Initialize subject marks ACCORDING TO COLLEGE
subjects = {
    "Mathematics": int(input("Enter marks for Mathematics: ")),
    "Physics": int(input("Enter marks for Physics: ")),
    "Chemistry": int(input("Enter marks for Chemistry: ")),
    "Structural mechanics": int(input("Enter marks for structural mechanics: ")),
    "English": int(input("Enter marks for English: ")),
    "ED": int(input("Enter marks for ed: ")),
    "structural lab": int(input("Enter marks for structural lab: ")),
    "physics lab": int(input("Enter marks for physics lab: ")),
    "chemistry lab": int(input("Enter marks for chemistry lab: ")),
    "yoga": int(input("Enter marks for yoga: "))
}

# Function to calculate TGPA
def calculate_tgpa(marks):
    if 90 <= marks <= 100:
        return 10
    elif 80 <= marks < 90:
        return 9
    elif 70 <= marks < 80:
        return 8
    elif 60 <= marks < 70:
        return 7
    elif 50 <= marks < 60:
        return 6
    elif 40 <= marks < 50:
        return 4
    else:
        return 0  # Fail or below passing marks

# Calculate total score
total_score = 0

for subject, marks in subjects.items():
    tgpa = calculate_tgpa(marks)
    if subject == "Mathematics":
        total_score += tgpa * 4  # Mathematics weighted by 4 ACCORDING TO COLLEGE
    else:
        total_score += tgpa * 2  # Other subjects weighted by 2

        value = total_score/22   #change "22" according to your TOTAL GRADE POINT OF THAT SEMISTER

# Display total score
print(f"Your total weighted TGPA score is: {value}")


if (value == 10) : print( "EXTRA ORDINARRY -> A++ ")
if(value ==9): print( "VERY GOOD -> A+ ")
if(value ==8): print( "GOOD -> A ")
if(value ==7): print( "NICE -> B+ ")
if(value ==6): print( "SATISFACTORY -> B ")
if(value ==5): print( "TRY HARD -> C ")
if(value ==4): print( "PASSED -> P ")
if (value <4): 
    print("YOU ARE FAIL ")

