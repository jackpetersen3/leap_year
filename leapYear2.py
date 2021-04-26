quit1 = 0
while quit1 == 0:
    year = input("Enter a year: ")
    try:
        year = int(year)
    except:
        print("input must be an integer")
        break
    if  year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year\n")
            else:
                print(year, "is not a leap year\n")
        else:
            print(year, "is a leap year\n")
        
    else:
        print(year, "is not a leap year\n")
    quit1 = input("To enter another year press 0, to quit press 1: ")
    quit1 = int(quit1)