import numpy
#create a dictionary to define the values of grades numerically
GradeValues = {
    'A+': 100,
    'A': 95,
    'A-': 90,
    'B+': 89,
    'B': 85,
    'B-': 80,
    'C+': 79,
    'C': 75,
    'C-': 70,
    'D+': 69,
    'D': 65,
    'D-': 60,
    'F': 50
}

#define function that turns the letter grades into numerical grades
def GradeToNumber(grade):
    return GradeValues.get(grade, None)

#define function to find the average grade of the given grades
def AverageGrade(grades):
    #call the GradeToNumber function to interpret the letters as grades and then find their sum and get the average
    NewGrades = [GradeToNumber(grade) for grade in grades]
    total = sum(NewGrades)
    print(total)
    average = total / 3
    print(average)
    #create a massive elif chain that organizes codes into their respective categories.
    if 97 <= average <= 100:
        return 'A+'
    elif 93 <= average <= 96:
        return 'A'
    elif 90 <= average <= 92:
        return 'A-'
    elif 87 <= average <= 89:
        return 'B+'
    elif 83 <= average <= 86:
        return 'B'
    elif 80 <= average <= 82:
        return 'B-'
    elif 77 <= average <= 79:
        return 'C+'
    elif 73 <= average <= 76:
        return 'C'
    elif 70 <= average <= 72:
        return 'C-'
    elif 67 <= average <= 69:
        return 'D+'
    elif 63 <= average <= 66:
        return 'D'
    elif 60 <= average <= 62:
        return 'D-'
    else:
        return 'F'

