#this program is used to find whether the inputted year is leap year or not

def checkyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
opt = int(input("Enter year: "))                        

if (checkyear(opt)):
    print("It is a Leap Year")
else:
    print("Not a Leap Year")    