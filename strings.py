# in python strings are enclosed in a double or single quotes. 
a='hello' # is same as 
a="hello"
print(a)
# we can even use quotes inside quotes but it needs to be differentiated properly 
b="My name is 'Rakesh'"
print(b)
# we can write multiple lines of string by using either triple double or single quotes
c = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(c)
d= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(d)
# in python strings are arrays and can be printed using slicing operator where each letter is 1
a='hello world'
print(a[3])
# we can even loop over a string using forloop 
for x in 'banana':
    print(x)
# to check for a specific word we use the keyword in 
y='hello, my name is rakesh'
print('hello' in y)
# we can even use if else to check if the specific word is present 
z='hello guy, my name is rakesh'
if 'guy' in z:
    print('yes it is present')
else:
    print('nope it is not there')
# we can even find out the length of the string by using the keyword len
g='rakesh'
print(len(g))
# to check if a word is presnt in a stirng we use in if it is not present then we use not keyword 
f='hello word, python is fun'
print('word' not in f)
######### string slicing ###########
# is used to prit certain characters of a string.
e='hello world'
print(e[2:5]) # in this example 2 is the character number it starts from and 5 is till where it counts and 5 does not count so it goes like 2,3,4 so its l l o. and the first index starts from 0 not 1 
# to print from a specific index to an end then we write the first index and second one we leave it empty
print(e[2:])
# negative indexing starts from the last. so in the above example of hello world -1 is d and -2 is l and so on. so to print world we write 
print(e[-6])
# there are few methods in python that are used to modify strings
f=' HELLO WORLD '
print(f.lower()) # lower keyword is used to convert all the letters of the string into lower case letters
print(f.strip())# strip keyword removes all the white spaces that are present on any side of the string
print(f.replace('H','J'))# replace keyword is used to replace any keyword with another one 
print(f.split())# splilt keyword is used to split the string into two words if there are two or more words present.
########### String concatination ############
# this is another method in python that is used to join or cancatinate two strings 
a='hello ' # in this if we dont add a space after the word then we would get the result as helloworld
b='world'
c=a+b
print(c)
# the above example is possible because both the variables are in string format. But to concatinate two different variable data types then we use something called as f string. 
a=23
b=f'my name is rakesh and my age is {a}' # here we used curly braces to format the value so that it prints 23 instead of a if we dont put a inside curly braces then it prints my name is rakesh and my age is a. these curly braces are also called as paceholder and it can also return mathematical operators too.
print(b)

