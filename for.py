# for loop is another loop that is used in python. this is used for iterating a variable, list, tuple or anything else.
# unlike while loop for does not need any indexing variable at the beginning. 
fruits=['apple','mango','orange']
for i in fruits:
    print(i)
    if i=='mango':
        break
  
# this is iterating through list in the same way we can also iterate through strings. 
for i in 'banana':
    print(i)

# range function is a method that is sued to iterate the loop a specified number of times. 
for i in range(5): # note that in range if we type 5 it prints only till 4.
    print(i)
# the default increxghxhment in range method is by 1 but we can change it by whatever number we want. 
for x in range(0,10,2): # in this the sequence starts from 0 and increments 2 everytime.
    print(x)
#else statement can also be used with for loop so that once the for loop is done and the loop is exited the statement in the else block would be printed. 
for i in range(6):
    print(i)
else:
    print('loop finished')
# nested for loops where more than one loop is used and for one iteration of the outer loop the inner loop would get executed. 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for i in adj:
    for j in fruits:
        print(i,j)