#tuples are also used to store multiple values in a single variable. but unlike list these are stored in a paranthesis 
a=(1,2,3)
print(type(a))
# tuples once created are not unchangable that is we cannot add new elements or delete or modify existing variables but tuples too like lsits allow duplicate values.
# to print a tuple with a single element then after the element we should end it with a comma or eles it does not get counted as a tuple it would be a normal datatype. 
a=(1)
print(type(a))
# just like lists we can access a single element form a tuple using indexing. 
b=(1,2,3,4,5)
c=list(b)
c.remove(5)
d=tuple(c)
print(d)

# unpacking of tuples 
x=('apple','banana','mango')
(green,yello,red)=x
print(green)# apple
print(yello)#banana
print(red)# mango

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green,*red,blue)=fruits
print(green)
print(red)
print(blue)

# we can even use loops to iterate through the values in the tuples
y=(1,2,3,4,'apple','amgno','orange')# this is using loops to loop through the values of the tuple.
for i in y:
    print(i)
g=(1,2,3,4,'mango','orange')# this is using loops to loop through the index values of the tuple
for i in range(len(g)):
    print(g[i])
# join tuples 
# just like in lists evne in tuples we can join two or more tuples together. 
a=(1,2,3)
b=(4,5,6)
c=a+b
print(c)
# if we want to multiply the tuples that we want then we just use the multiply symbol. 
c=c*2
print(c)

# as we know that tuples are not mutable and canot be modified unless it is first converted into a list and then back into the tuple again so in tuple there are only two methods that are available which are count() and index()
# so index method in tuple is used to get the index number of a specific value unlike indexing which gives us the value once we enter a specific index. 
