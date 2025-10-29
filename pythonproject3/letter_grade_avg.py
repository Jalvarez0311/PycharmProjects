#import functions from letter_grade.py
from L04_HW.grade_compute import AverageGrade

#define first function to process the user input
def processLine():

    #Give parameters and ask for user input
    print('Enter letter grades (Ex: A, B-, C+, F)')
    First = input('Enter the first grade or Q to quit: ')

    #check first input for Q and get other inputs. Turn every input into uppercase so that lowercase is accepted as well
    First = First.upper()
    if First == 'Q':
        return None
    Second = input('Enter the second grade: ')
    Second = Second.upper()
    Third = input('Enter the third grade: ')
    Third = Third.upper()
    Fourth = input('Enter the fourth grade: ')
    Fourth = Fourth.upper()
    #put the grades in a list and then return the list of grades to the main function
    grades = [First, Second, Third, Fourth]
    return grades

def main():
    #initialize the grades list by calling the processLine function
    grades = processLine()
    #continuation of checking for Q in the main program to end the program and display that the program was successfully terminated
    if grades == None:
        print('Program Terminated')
        return 0

    #unpack grades inputted
    print('Grades entered: ', *grades)
    #minL stores the lowest grade (which is the highest on the ASCII table) to be displayed later
    minL = max(grades)
    #variable Minimum used to store the index of the minimum value for future use
    Minimum = grades.index(max(grades))
    #pop the minimum value so that it is not used in the calculation of the average
    grades.pop(Minimum)
    #call the AverageGrade function to calculate the average of the grades
    Average = AverageGrade(grades)

    #print the minimum grade that was removed and then the average score of the three remaining grades
    print('The lowest grade of', minL, 'will be removed')
    print('The resulting average grade is', Average)

if __name__ == "__main__":
    main()

## processes one line of input
## @return True if the sentinel was encountered or False otherwise



