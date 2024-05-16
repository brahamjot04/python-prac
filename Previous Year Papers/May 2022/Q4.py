# WAP to accept a number from 1 to 12 and display the name of the month and days in a month

def month(mon_num):
    match mon_num:
        case 1:
            print("Month: January")
            print(no_31)

        case 2:
            print("Month: Feburary")
            print("Days: 28/29")

        case 3:
            print("Month: March")
            print(no_31)

        case 4:
            print("Month: April")
            print(no_30)

        case 5:
            print("Month: May")
            print(no_31)

        case 6:
            print("Month: June")
            print(no_30)

        case 7:
            print("Month: July")
            print(no_31)

        case 8:
            print("Month: August")
            print(no_31)

        case 9:
            print("Month: September")
            print(no_30)

        case 10:
            print("Month: October")
            print(no_31)

        case 11:
            print("Month: November")
            print(no_30)

        case 12:
            print("Month: December")
            print(no_31)

        case _:
            print("Invalid month number")
            ip_month()

def ip_month():
    mon_num = int(input("Enter the month number(from 1 to 12:) "))
    month(mon_num)

no_30 = "Days: 30"
no_31 = "Days: 31"
ip_month()
