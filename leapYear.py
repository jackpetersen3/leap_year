quit1 = 0
while quit1 == 0:
    year = input("Enter a year: ")
    year = int(year)
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
    print("Hello World")
    print("What is happening")
