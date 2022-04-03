#BY @LUISLEALDEV 
#https://luislealdev.web.app

# height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = weight/(height**2)
BMI = str(BMI)
print("Your BMI is: " + BMI)


#If you want to round the number, change the code to this one
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = round(weight/(height**2)) #This line is the only one that changes
BMI = str(BMI)
print("Your BMI is: " + BMI)

#It can also be rounded by the number of digits that you want to
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

BMI = round(weight/(height**2),2) #This line is the only one that changes (Again)
BMI = str(BMI)
print("Your BMI is: " + BMI)