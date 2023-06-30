# # print
# print("Moch Satria Dhapa Hamdani")
# print("-" * 10) # expression

# # variable
# name = "Moch Satria Dhapa Hamdani" # string data type
# name = "dhapa"
# price = 10000 # integer data type
# rating = 4.9 # float data type
# is_publiced = True # boolean
# print("nama saya ", name)

# full_name = 'satria dhapa'
# age = 20
# is_new = True

# # receiving input

# name = input("what is your name? ") 
# print("hallo" + name)

# # liitle example
# full_name = input("what's your name? ")
# color = input("What's your favourite color? ")
# print(full_name + " likes " + color)

# # type conversion
# birth = input("birth year: ")
# age = 2023 - int(birth)
# print(age)

# # little example
# berat_lbs = int(input("Berat (lbs): "))
# berat_kg = berat_lbs * 0.45
# print(berat_kg, "Kg")

# # strings handling

# course = "python for 'beginer'"
# print(course)
# # course = '''
# #     Moch Satria Dhapa Hamdani
# #     Teknik Informatika
# # '''
# print(course)
# print(course[-5])
# print(course[0:8])

# # litte example

# name = "satria"
# print(name[1:-1])

# # formatted strings
# first = "satria"
# last = "hamdani"
# fmt1 = first + ' [' + last + '] is a junior data scientist'
# fmt2 = f'{first} [{last}] is a junior data scientist'
# print(fmt2)

# #string methods
# course = "python is the best programming languages"
# print(course.upper())
# print(course.lower())
# print(len(course))
# print(course.find('l'))
# print(course.title())
# print(course.replace())

# # calculate BMI
# height = 1.79
# weight = 68.7
# BMI = weight / (height**2)
# print(round(BMI))

# # aritmetic operations
# x = 11
# x += 3
# x -= 2
# x *= 2
# x /= 90
# print(x)

# #operator precedence
# x = 10 + (2 *2)
# print("hasilnya " + x)

# import math
# x = (2 + 3) * 10 - 3
# print(x)
# x = 2.4
# print(round(x))
# print(x)

import time
tmp = int(input("how much temperature today? "))
if tmp <= 16:
    print("it's cold day")
    time.sleep(2)
    print("wear warm clothes")
elif tmp >= 16 and tmp <= 25:
    print("it's a lovely day")
    time.sleep(2)
    print("Enjoy!!!")
elif tmp >= 26:
    print("it's hot day")
    time.sleep(2)
    print("drink some of cold water")
else:
    print("invalid input")