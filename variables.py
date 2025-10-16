# in python variables are supposed to be written in these formats: starting with either a letter or underscore but names should never start with a number, can have a number in between the names, to separate two words we can either use an underscore or start each word with a capital letter. 
myvar=10
my_var=11
My_var=12
My_Var=13
MYVAR=14
MyVar=15
myVar=16
# these are all the kinds of variable names that can be used. But python keywords should never be used as a variable name cause interpretor would consider it as a keyword 

# we can even assign multiple variables to assign to a single value or either a multiple values to multiple variables. 

a,b,c=1,2,3
print(a)
print(b)
print(c)
    #or
x=y=z='orange'
print(x)
print(y)
print(z)
# or instead of writing three print statements we can combine and print all the three variables in a single print statemnt by ,
print(x,y,z)
# if we want to combine two or more variables into a single print statement then we use + symbol
one='hello '
two='world '
print(one+two)

# GLOBAL VARIABLE: a variable that is defined outside the function and can either be used inside or outside the function. 
A='awesome'
def fun():
    print('python is' ,A)
fun()

def func(): # creating a global variable inside a function and can be accesed outside the function too
    global X
    X='Hello'
func()
print(X)
