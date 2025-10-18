# operators are used to perform operations on variables.such as addition, multiplication, division, subtraction etc.
print(5+10)
# it can also be used to add a variable and a value or two variables too
a=10+5
b=a+20
c=a+b
print(c)
# on python operators are further divided into different groups: Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

######## arithmetic operators #########
a=10
b=20
print(a+b) # addition
print(b-a) # subtraction
print(a*b) # multiplication
print(b/a) # division gives quotient in float
print(a%b) # modulus: returns remainder
print(a**b) # exponential
print(b//a) # floor division gives the quotient in int

######## assignment operators #########
# these operators are used to assign values to a variable 
c=4
c+=3 # c=c+3
c-=3 # c=c-3
c*=3 # c=c*3
c/=3 # c=c/3
c**=3 # c=c**3
######## comparision operators ########
# these are used to compare two values
x=3
y=5
print(x<y)
print(x>y)
print(x==y)
print(x<=y)
print(x>=y)
print(x!=y)
# in python chaining comparision operators can also be used
z=10
print(1<z<20)
print(1<z and z>5)

####### logical operators ########
# these statements are used to combine conditional statements. 
# 1. and operator returns true if both the statements ar etrue.
# 2. returns true if either one of the statement is true.
# 3. not returns false if the result is true.

a=5
print(1<a and a<20)
b=10
print(a<10 or b==1)

###### identity operators ######
# identity operators are used to compare the values but not if they are equal but to check if they are the same object with the same memory location. Two keywords are used in identity operators which are 'is' and 'is not'. is returns true if both the variables store the same value and is not returns true if both the variables store different values. 
a='banana'
b='banana'
print(a is b)
 # this returns true because both a and b have a stored value 'banana'
c='banana'
d='apple'
print(c is d)# this returns false because both the variables does not store the same value inside. 
print(c is not d) # this again prints true because both the variables stores different values. 

x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)
print(id(x),id(y))
####### membership operators #########
# there are two keywords in this 'in' and 'not 'in'. in keyword returns true if the specific value is present in the variable and not in returns true if the specific value is not presnet in the variable. 
