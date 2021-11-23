# PART I
print("*******CHINESE CALENDAR*******")
print("Enter year:")
year = int(input())

# CONST
startFrom = 1900
AllYears = 12  # quantity of years
AllAnimals = 10  # quantity of animals

# PART II
# CALCULATIONS
number = year - startFrom   # the number of year from begin
currentYear = number % AllYears
animal = number % AllAnimals

# PART III
# CONCLUSION I
if animal == 0 or animal == 1:
    print("iron")
elif animal == 2 or animal == 3:
    print("water")
elif animal == 4 or animal == 5:
    print("wood")
elif animal == 6 or animal == 7:
    print("fire")
elif animal == 8 or animal == 9:
    print("ground")

# PART IV
# CONCLUSION II
if currentYear == 0:
    print("rat")
elif currentYear == 1:
    print("bull")
elif currentYear == 2:
    print("tiger")
elif currentYear == 3:
    print("rabbit")
elif currentYear == 4:
    print("dragon")
elif currentYear == 5:
    print("snake")
elif currentYear == 6:
    print("horse")
elif currentYear == 7:
    print("sheep")
elif currentYear == 8:
    print("monkey")
elif currentYear == 9:
    print("chicken")
elif currentYear == 10:
    print("dog")
elif currentYear == 11:
    print("pig")