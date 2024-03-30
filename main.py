import random

def select_person(names):
    if len(names) == 0:
        print("Please enter at least one name.")
        return None
    else:
        random_person = random.choice(names)
        return random_person.strip() 

names_string = input("Input everyone's name, separated by a comma: ")

names = [name.strip() for name in names_string.split(",")]

selected_person = select_person(names)

if selected_person:
    print(f"{selected_person} is going to buy the meal today!")
