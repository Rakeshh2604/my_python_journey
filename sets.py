# sets are used to store multiple values just like lists and tuples but in sets there is no order for values that ar ethere in the variable and as the values are unordered there is no indexing in sets.
# sets are enclosed by a curly braces. 
a={1,2,3}
print(type(a))
# set is one of the four built in data types in python that are used to store multiple values in a variable. 
# sets does not allow duplicate values. 
b={1,1,2,3,4}
print(b)# so even though there are duplicates it only prints the first occurence of the value and ignores the other ones. 
c={1,2,3,True,'apple'}
print(c)# in sets true and 1 are considered the same values so it considers it as a duplicate and prints the first appearence.
# false and 0 are also same in sets so it only prints the first occurence of either false or 0.

# just like in lists and tuples to get the length of the set we use the len keyword. 

# once a set is created we can add new values to it later on. 
c.add('mango')
print(c)
# to add two sets we then use the update keyword. we can not only update two different sets we can do a set and list, set and tuple or anything literally. 
c.update(b)
print(c)
z={'banana','apple','pineapple'}
for i in z:
    print(i)
#joining of sets 
a={1,2,3,4,7,8}
b={5,6,7,8}
c=a.union(b)
print(c)
d=a.difference(b)
print(d)
e=a.intersection(b)
print(e)
f=a.symmetric_difference(b)
print(f)