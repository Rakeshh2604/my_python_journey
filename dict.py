a={1:'apple',2:'mango',3:'pineapple'}
print(a)
print(type(a))
# to access a specific value from the dictionary we do it using key.
x=a[2]
print(x)
# to get only the keys of the dictionary 
y=a.keys()
print(y)
# to get only the values without keys 
z=a.values()
print(z)
# we can even add new values into a existing dict
a[4]='grapes'
print(a)
# to change the values of already existing values 
a[3]='orange'
print(a)
# nested dictionaries are something where we can add multiple dics in a single dic. 
myfamily = {
    'child1':{
    'name':'rakesh',
    'year':2002
    },
    'child2':{
        'name':'anish',
        'year':2003
    },
    'child3':{
        'name':'ruthvik',
        'year':2004
    }
}
print(myfamily)
print(myfamily['child1']['name'])# this is used to access a specific key from the nested dictionary. 
