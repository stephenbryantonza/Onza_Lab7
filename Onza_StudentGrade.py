
name = (input("Enter your Name:"))
section = (input("Enter your section:"))

print ("Grade input must be between the range of 40 - 100.")
prelim = float(input("Enter your prelim grade:"))

if prelim <= 39:
  print("ERROR, PLEASE TRY AGAIN!")
  exit()
 
elif prelim >= 101:
  print("ERROR, PLEASE TRY AGAIN!")
  exit()


midterm = float(input("Enter your midterm grade:"))

if midterm <= 39:
  print("ERROR, PLEASE TRY AGAIN!")
  exit()
 
elif midterm >= 101:
  print("ERROR, PLEASE TRY AGAIN!")
  exit()


final = float(input("Enter your finals grade:"))

if final <= 39:
  print("ERROR, PLEASE TRY AGAIN!")
  exit()
 
elif final >= 101:
  print("ERROR, PLEASE TRY AGAIN!")
  exit()

combinedgrades = prelim + midterm + final
Fprelim = prelim*.3333
Fmidterm = midterm*.3333
Ffinal = final*.3333

Fgrades = Fprelim + Fmidterm + Ffinal
print("-----------------")
print (f"This is your final grade: {Fgrades:.0f}")
 
if Fgrades < 75:
    print("GPA: 5.0")
    print("General Description: Failed") 
elif Fgrades <= 75:
    print("GPA: 3.00")
    print("General Description: Passed")
elif Fgrades <= 78:
    print("GPA: 2.75")
    print("General Description: Fair")
elif Fgrades <= 81:
    print("GPA: 2.50")
    print("General Description: Fairly Satisfactory")
elif Fgrades <= 84:
    print("GPA: 2.25")
    print("General Description: Satisfactory")
elif Fgrades <= 87:
    print("GPA: 2.00")
    print("General Description: Good")
elif Fgrades <= 90:
    print("GPA: 1.75")
    print("General Description: Verygood")
elif Fgrades <= 93:
    print("GPA: 1.50")
    print("General Description: Superior")
elif Fgrades <= 96:
    print("GPA: 1.25")
    print("General Description: Outstanding")
elif Fgrades <= 99:
    print("GPA: 1.00")
    print("General Description: Excellent")
elif Fgrades<=100:
    print("GPA: 1.00")
    print("General Description: Excellent")