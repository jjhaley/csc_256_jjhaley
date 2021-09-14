import datetime

def calculateRetirementAge(year, month):
    birthYear = int(year)
    birthMonth = int(month)
    if birthYear >= 1960:
        print("Your full retirement age is 67 years and 0 months")
        convertMonth = datetime.datetime.strptime(str(birthMonth), "%m")
        retirementMonth = convertMonth.strftime("%B")
        retirementYear = birthYear + 67
        print("This will be in " + retirementMonth + " of " + str(retirementYear))
    elif birthYear < 1960 and birthYear > 1954:
        convertMonth = 12 - ((1960 - birthYear) * 2)
        if (birthMonth + convertMonth) > 12:
            retirementMonth = (birthMonth + convertMonth) - 12
            retirementYear = birthYear + 67
        else:
            retirementMonth = birthMonth + convertMonth
            retirementYear = birthYear + 66
        print("Your full retirement age is 66 years and " + str(convertMonth) + " months")
        retirementMonth = datetime.datetime.strptime(str(retirementMonth), "%m")
        retirementMonth = retirementMonth.strftime("%B")
        print("This will be in " + retirementMonth + " of " + str(retirementYear))
    elif birthYear <= 1954 and birthYear >= 1943:
        print("Your full retirement age is 66 years")
        retirementMonth = datetime.datetime.strptime(str(birthMonth), "%m")
        retirementMonth = retirementMonth.strftime("%B")
        retirementYear = birthYear + 66
        print("This will be in " + retirementMonth + " of " + str(retirementYear))
    else:
        if (1943 - birthYear) >= 6:
            convertMonth = 12 - (((1943 - birthYear) * 2) % 12)
            if convertMonth == 12:
                convertMonth = 0
        else:
            convertMonth = 12 - ((1943 - birthYear) * 2)
        retirementYears = int(66 - ((1943 - birthYear) / 6))
        if (birthMonth + convertMonth) > 12:
            retirementMonth = (birthMonth + convertMonth) - 12
            retirementYear = (retirementYears + 1) + birthYear
        else:
            retirementMonth = birthMonth + convertMonth
            retirementYear = birthYear + retirementYears
        print("Your full retirement age is " + str(retirementYears) + " years and " + str(convertMonth) + " months")
        retirementMonth = datetime.datetime.strptime(str(retirementMonth), "%m")
        retirementMonth = retirementMonth.strftime("%B")
        print("This will be in " + retirementMonth + " of " + str(retirementYear))

def main():
    print('Social Security Full Retirement Age Calculator\n')
    year = 0
    month = 0
    userIn = " "
    while userIn != "":
        userIn = str(input("Enter Year of Birth or press enter to exit: "))
        if userIn == "":
            continue
        while int(userIn.isdigit()) == False:
            userIn = str(input("Error. Please enter a number for year: "))
            year = userIn
        year = userIn
        userIn = str(input("Enter Month of Birth: "))
        while int(userIn.isdigit()) == False:
            userIn = str(input("Error. Please enter a number for month: "))
            month = userIn
        month = userIn
        calculateRetirementAge(year, month)








main()