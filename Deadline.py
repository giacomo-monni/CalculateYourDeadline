# 1. Ask a user to enter the deadline for their project
# 2. Tell how many days they have to complete the project
# 3. Tell how many time they have using a combination of weeks and days


#Import of datetime library
import datetime

#First part
#Asking the project deadline
deadline=input("Hi user!\nPlease insert your project's deadline\n")
#Deadline conversion from string to datetime type
deadline=datetime.datetime.strptime(deadline,'%d/%m/%Y').date()
#Acquisition of today's date
currentDate=datetime.date.today()
#Remaining days calculation
remainingDays=deadline-currentDate

#Second part
#Result's communication
print('You must complete your project in %d '%remainingDays.days+'days')

#Third part
#Calculus of weeks and days format
remainingDaysWeek=(remainingDays.days%7)
remainingWeeks=remainingDays.days/7
remainingWeeks=int(remainingWeeks)
print('You must complete your project in %d '%remainingWeeks+'weeks and %d'%remainingDaysWeek+' days')
