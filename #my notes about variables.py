#my notes about variables

#(1. WHAT IS A VARIABLE?) a variable is a name that stores a value in your program. you can think of it like a container or a label that holds data
name = "Zeynep" 
age = 19
height = 1.67
#name stores a STRING ("Zeynep")
#age stores an INTEGER (19)
#height stores a FLOAT (1.67)

#(2. NAMING RULES FOR VARIABLES)
#must start with a letter or underscore
#cannot start with a number
#cannot contain spaces
#are case-sensetive (Age and age are different)
#should not use speacial characters like ?,!,-, etc.
user_name = "Luna"    # valid
_user2 = "Leo"        # valid
2user = "Nope"        # invalid
user-name = "No"      # invalid

#(3.COMMON DATA TYPES FOR VARIABLES)
# int     integer                   age = 21 
# float   decimal number            price = 19.99
# str     string                    message = "hello"
# bool    boolean(True or False)    is_student = True
# list    list of values            colors = ["red", "blue"]
#you can use the type() function to check a variable's type
print(type(age))       # <class 'int'>

#(4. ASSIGNING AND UPDATING VARIABLES)
#you assign a variable with = , and you can change it any time. python is dynamically typed, meaning you do not have to declare the type
points = 50
points = 70            # new value

x = 5                  # int
x = "hello"            # now it is a string

#(5. INPUT FROM USER) you can ask the user for input and store it in variables
name = input("what is your name? ")
print("nice to meet you,", name)
#want a number from the user?
age =int(input("enter your age: "))

#(6. STRING FORMATTING WITH VARIABLES) you can combine variables and text using: f-strings, + operator, format() method
name = "zeynep"
age = 19
print(f"my name is {name} and i am {age} years old.")  # f-string 
print("my name is " + name + " and i am " + str(age) + " years old ")  # +
print("my name is {}  and i am {} years old ".format(name,age))  # format()