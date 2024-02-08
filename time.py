#Cierra Crosby
#2/7/2024
#Instructor Antonio Tovar
#This program writes a statement to calculate the number of hours a person is currently in from their specific time zone.
#This program asks the number of hours a person will wait to be in a different time zone.
#This program prints out the number of hours it is currently and adds to the number of hours a person waits to their time zone. 


currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)
