# lists in python can store multiple values and is enclosed in a square bracket. 
a=[1,2,3]
print(a)
# lists are ordered, can be changed and also can store duplicate values. Indexing in lists start from 0.
b=['apple','banana','apple']
print(b)
print(len(b))# to identify the length of the list. 
# a list can be of any datatype and can also store multiple datatypes in a single list.
c=[1,2,'banana','4,','0.5']
print(c)
# just like in strings we can also access specific items from the list using indexing. 
print(c[2])
# positive indexing starts from the left and negative starts from the right. to access more than one element we can use : 
print(c[0:3])
# we can also use in keyword to check if the specific value is present in the list or not. 
d=[1,2,3,'banan','apple','mango']
if 'mango' in d:
    print('it is present')
else:
    print('it is not present')
# we can even change the value of anything in the list 
d[0]='green apple'
print(d)
# we can also change a range of values using indexing
d[1:2]=['watermelon','peach']
print(d)
# to insert new items in a list we use the insert keyword.
d.insert(3,'guava')
d[4]='kiwi'
print(d)
# to add a new item at the end of the list we use append keyword. 
d.append('orange')
print(d)
d.extend(c)
print(d)
# to remove an item from the list we use remove keyword
d.remove('orange')
print(d)
# to remove a specific item based on its index then we use the pop keyword 
a=[1,2,3]
a.pop(0)
print(a)
# if we do not mention the specific index then it removes the last item of the list.

# del keyword also does the same thing as pop but if we dont specifiy any index then it removes the entire list. 
x=[5,6,7]
del x[0]
print(x)

y=['apple','banana']
for x in y:
    print(x) # we can even loo through a list to print all the values one by one in a different line. 
# we can even loop through a list using comprehension
[print(y) for i in y]

# comprehension in lists is used to reduce the syntax of using the standard loops cause if we want to print a new list form the older on we can use comprehension. 
a= ["apple", "banana", "cherry", "kiwi", "mango"]
# now from this if i only want the items that start with a then its going to be a long code.
b=[]
for i in a:
    if 'a' in i:
        b.append(i)
print(b) # this the code to get the items that has a in it instead of this we can use comprehension which takes only one line. 
c=[i for i in a if 'a' in i] # this is the code for comprehension first we start with initialising the for loop variable in this example it is i and then we start the for loop followed by if else only when needed. 
print(c) 
# the above example is using the if statement without the if statement it is much easier
a=[1,2,3,4]
b=[i for i in a]
print(b)

# sort is a keyword in python that is used to sort the list either from ascending or descending order.
a=[1,2,3,4,8,7,6]
a.sort()
print(a)
# to get the result in descending order then we write reverse=true
a.sort(reverse=True)
print(a)
# can also be used with strings 
b=['watermelon','mango','apple']
b.reverse()
print(b)

# we can join two lists by three different methods: 
# 1. 
x=[1,2,3]
y=[4,5,6]
z=x+y
print(z)
# 2. we can use a forloop and append function also to join two lists.
for i in x:
    y.append(i)
y.sort()
print(y)
# 3. last method is by using the extend function 
x.extend(y)
x.sort()
print(x)