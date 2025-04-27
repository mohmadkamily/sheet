#1)
import random

def generate_password(length, chars):
    password = ''.join(random.choice(chars) for _ in range(length))
    return password
print(generate_password(8, "abcde"))


#2)
uppercase_range = range(ord("A"), ord("Z") + 1)
lowercase_range = range(ord("a"), ord("z") + 1)
digits_range = range(ord("0"), ord("9") + 1)
output_string = "".join(
    [chr(x) for x in uppercase_range] +
    [chr(x) for x in lowercase_range] +
    [chr(x) for x in digits_range]
)

print(output_string)


#3)
names = ["mohmad", "kamil", "ahmed"]

letters = {letter for name in names for letter in name}

print(letters)



#4)
def average(*numbers):
    return sum(numbers) / len(numbers)

avg = average(50, 100, 6)
print(avg)


#5)
def substitute(equation, **kwargs):
    for elem in equation:
        if elem in kwargs:
            equation = equation.replace(elem, str(kwargs[elem]))
    return equation

print(substitute("x + y = 5", x=1, y=4))
