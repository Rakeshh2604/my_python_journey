# in programming we sometimes need to know if an expression is true of false and for this we use boolean
print(5<3)
print(6==6)
a=10
b=20
if a>b:
    print('a is greater than b')
else:
    print('b is greater than a')

# almost any value is evaluated as true unless it has a value in it for suppose in a string variable if it is left empty then it prints false and in an int variable if the value is 0 then it prints false. 
a=0
b=''
print(bool(a))
print(bool(b))

# boolean can also be used in functions to print true or false.
def fun():
    return True
if fun():
    print('yes')
else:
    print('No')
# this code prints yes because we returned true in the function if we return false then it prints No
