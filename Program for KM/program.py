import datetime

now = datetime.datetime.now()
dateAndTime = str(now)
x = 0

question1 = input("Are you writing to promise money? (y or n) ")
if question1 == "y":
    name1 = input("What is your name? ")
    amount1 = input("What is the amount of money you are promising in USD? ")
    with open('money.txt', 'a') as f:
        f.write("Promiser Name: " + name1)
        f.write("\n")
        f.write("$" + amount1)
        f.write("\n")
        f.write("Time: " + dateAndTime)
        f.write("\n")
elif question1 == "n":
    name1 = input("What is your name? ")
    amount1 = input("What is the amount of money you are paying in USD? ")
    with open('money.txt', 'a') as f:
        f.write("Payer Name: " + name1)
        f.write("\n")
        f.write("$" + amount1)
        f.write("\n")
        f.write("Time: " + dateAndTime)
        f.write("\n")
else:
    print("ERROR, please enter 'y' for promising money or enter 'n' for paying money. Please restart the program")