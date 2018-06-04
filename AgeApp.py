import datetime

Name = input("Enter your name \n")
Age = input("Enter your Age \n")
CurrentYear = datetime.datetime.now().year
BirthYear = CurrentYear - int(Age)
AgeFifty = BirthYear + int(50)

print("Hello, {}, You are {} years old, your birth year is {} and you will be 50years old by {}".format(Name, Age, BirthYear, AgeFifty))
