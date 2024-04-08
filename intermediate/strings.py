my_string = 'Hello'
my_string = "Hello"
my_string = "I' m  a 'Geek'"

my_string = 'I\' m  a "Geek"'
my_string = 'I\' m a \'Geek\''
print(my_string)

# triple quotes for multiline strings
my_string = """Hello
World"""
print(my_string)

my_string = "Hello \
World"
print(my_string)

# get character by referring to index
b = my_string[0]
print(b)


b = my_string[1:3] # the last index is not included
print(b)
b = my_string[:5] 
print(b)
b = my_string[6:] 
print(b)
b = my_string[::2] 
print(b)
b = my_string[::-1] 
print(b)

# concat strings with +
greeting = "Hello"
name = "Tom"
sentence = greeting + ' ' + name
print(sentence)


my_string = 'Hello'
for i in my_string:
    print(i)

if "e" in "Hello":
    print("yes")
if "llo" in "Hello":
    print("yes")

my_string = "     Hello World "


my_string = my_string.strip()
print(my_string)


print(len(my_string))


print(my_string.upper())
print(my_string.lower())

print("hello".startswith("he"))
print("hello".endswith("llo"))

print("Hello".find("o"))

print("Hello".count("e"))

message = "Hello World"
new_message = message.replace("World", "Universe")
print(new_message)

# split the string into a list
my_string = "how are you doing"
a = my_string.split() # default argument is " "
print(a)
my_string = "one,two,three"
a = my_string.split(",")
print(a)

# join elements of a list into a string
my_list = ['How', 'are', 'you', 'doing']
a = ' '.join(my_list) # the given string is the separator, e.g. ' ' between each argument
print(a)


# use braces as placeholders
a = "Hello {0} and {1}".format("Bob", "Tom")
print(a)

# the positions are optional for the default order
a = "Hello {} and {}".format("Bob", "Tom")
print(a)

a = "The integer value is {}".format(2)
print(a)

# some special format rules for numbers
a = "The float value is {0:.3f}".format(2.1234)
print(a)
a = "The float value is {0:e}".format(2.1234)
print(a)
a = "The binary value is {0:b}".format(2)
print(a)

# old style formatting by using % operator
print("Hello %s and %s" % ("Bob", "Tom")) # must be a tuple for multiple arguments
val =  3.14159265359
print("The decimal value is %d" % val)
print("The float value is %f" % val)
print("The float value is %.2f" % val)


name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)


# --> join method is much faster
from timeit import default_timer as timer
my_list = ["a"] * 1000000

# bad
start = timer()
a = ""
for i in my_list:
    a += i
end = timer()
print("concatenate string with + : %.5f" % (end - start))

# good
start = timer()
a = "".join(my_list)
end = timer()
print("concatenate string with join(): %.5f" % (end - start))