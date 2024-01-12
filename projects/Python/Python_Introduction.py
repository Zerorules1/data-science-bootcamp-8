# Review Python Language

my_name = "Petch" # 'Petch'
my_age = 29

print(my_name)
print(my_age)

print(1+1)
print(2*2)
print(3-5)
print(4/2)

# string & fstring in Python
my_name = "Petch"
my_university = 'KMUTT'

my_long_string= """This is a very long
    This is a second line
    This is a third line
"""

print(my_name, my_university, my_long_string)

# fstring template
my_name = "Petch"
my_age = 33

text = f"my name is {my_name}, and I am {my_age} years old."
print(text)

# function designed for string (string method)
text = "a duck walks into a bar"

text.upper() # upper case the text
text.count("a") # count a in text
text2 = text.replace('duck', 'lion') # replace duck with lion
print(text)
print(text2)

# list
shopping_list = ['egg', 'milk', 'bread']
print(shopping_list)

print(shopping_list[0:3]) # 0 to 2

# list method = append
shopping_list.append('orange juice')
print(shopping_list)

# list method .pop()
shopping_list.pop()
print(shopping_list)

len(shopping_list) # length

# dictionary key-value pair
student = {
    "id": 1,
    "name": "Mary",
    "age": 22,
    "movies" : ['Spider Man', 'Thor','Iron Man 3']
}
type(student)

student['movies'][1]

# add into city 
student['city'] = 'Manchester'

# remove key-value
del student['city']

# user-defined function
def hello(username):
    print("Hello !" + username)

hello("Petch")

def my_sum(val1, val2):
    return(val1 + val2)

result = my_sum(5,15)
print(result)

class Dog:
    name = "Inu"
    age = 3
    color = "Brown"
    breed = "French Bulldog"

    # function (dog method)
    def sitting(self):
        print("I am sitting now!")
    def hungry(self, food_name):
        print(f"I am hungry, I need {food_name}!")

my_dog = Dog()
type(my_dog)

my_dog.hungry("Hot dog")

