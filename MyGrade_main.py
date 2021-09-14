def calculateGrade(labs, midterm, final):
    labScore = labs * .34
    midtermScore = midterm * .33
    finalScore = final * .33
    return labScore + midtermScore + finalScore



def main():
    print("Calculate your Grade\n")
    labs = str(input("Enter labs score: "))
    while labs.isdigit() == False:
        labs = str(input("Score must be a number. Enter labs score: "))
    midterm = str(input("Enter midterm score: "))
    while midterm.isdigit() == False:
        midterm = str(input("Score must be a number. Please enter Midterm score: "))
    final = str(input("Enter final score: "))
    while final.isdigit() == False:
        final = str(input("Score must be a number. Please enter final score: "))
    formattedScore = "{:.2f}".format(calculateGrade(float(labs), float(midterm), float(final)))
    print("Final Grade: ", formattedScore)


main()

