# ==========================
# Title: cuauro_hobbies.py
# Author: Richard Krasso
# Modified by: Patrick Cuauro
# Date: 21 Jun 2023
# Description: Exercise 5.2
# Python conditional and loops
# exercises
# ==========================
# declare a list of hobbies
hobbies = [
    "play video games",
    "practice martial arts",
    "learning languages",
    "watch anime",
    "read manga",
    "listen to music"
]
# display list of hobbies using for loop function
print("----------Hobbies---------")
for item in hobbies:
    print(item)
# declare a list of weekdays
days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]
print("--------------------------")
print("----------Weekdays--------")
# display list of weekdays and condition days off (Sunday & Saturday)
for item in days:
    if item == "Sunday":
        print("It's Sunday, no work today, hobby time!")
    elif item == "Monday":
        print("It's Monday, workday.")
    elif item == "Tuesday":
        print("It's Tuesday, workday.")
    elif item == "Wednesday":
        print("It's Wednesday, workday.")
    elif item == "Thursday":
        print("It's Thursday, workday.")
    elif item == "Friday":
        print("It's Friday, workday.")
    elif item == "Saturday":
        print("It's Sunday, no work today, hobby time!")
print("--------------------------")
