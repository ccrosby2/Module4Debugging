#Cierra Crosby
#2/7/2024
#Instructor Antonio Tovar
#This program ask a person what is the current time in hours between 0-23
#This program ask what is the number of hours the person will wait to wake up for a event
#This program print the time it will be to wake up for a event

str_time = input("What time is it now(in hours 0-23)?")
str_wait_time = input("What is the number of hours to wait?")
time = int(str_time)
wait_time = int(str_wait_time)

time_when_alarm_go_off = time + wait_time
print(time_when_alarm_go_off)
