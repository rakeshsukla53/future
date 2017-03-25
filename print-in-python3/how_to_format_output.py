# arguments of the print function are the following ones:
import sys

print('rakesh', 'bikash', 'ekansh', sep=' ', end='\n', file=sys.stdout, flush=False)

# example 1

print(192, 168, 178, 224, sep='.')
print("a", 'b', sep=':-')

# example 2

# - print functions are always ended with new line

for index in range(100):
    print(index)

# if you want to change this behaviour then we can use end

for index in range(4):
    print(index, end=' ')

# example 3
# the output of the print function is send to standard output stream(sys.stdout) be default
# we can send the output to stderr or a file

fh = open("data.txt", "w")
print("42 is the answer, but what is the question?", file=fh)
fh.close()


# example 4
# you can redirect the output to standard error channel

print("errro: 42", file=sys.stderr)

# example 5

# so the general syntax for format placeholder is  %[flags][width][.precision]type
# %8.2f
# go over this page http://www.python-course.eu/python3_formatted_output.php

print("%10.3e" % 356.08977)  # e is floating point exponential number
print("%10o" % 25)  # o stands for unsigned octal number

# example 6

# the concept of positional parameters {index:format_placeholder)

print("First argument: {0}, second one: {1}".format(47, 11))
print("Second argument: {1}, first one: {0}".format(47, 11))

# you can also have various precision in the same sentence

print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42, 11))


# example 7

# keyword arguments with the format method

print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))

# example 8 ( left and right justify using the format method

print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))  # < means left justify
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))  # > means right justify

# example 9 This option signals the use of a comma for a thousands separator.

x = 5897653423.89676
print("The value is {0:12,.3f}".format(x))

# example 9 how to use dictionary using the format method

data = dict(school="Delhi", name="Sukla")
# print(**data)
# double star in front of dictionary basically converts this into a form like 'province="Ontario",capital="Toronto"'

print("my school is {school} and name is {name}".format(**data))  # this is a like a keyword argument

# example 10 another cool way to use formatted string for dictionary

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string.format(**capital_country))

# example 10 usage of locals in Python 3

a = 42
b = 47


def f():
    return 42

print(locals())

# locals() "locals" is a function, which returns a dictionary with the current scope's local variables,
# i.e- the local variable names are the keys of this dictionary and the corresponding values are the values
# of these variables:






























