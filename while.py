# python has two types of loops while and for 
# in while loop we can execute statements as long as the condition is true. 
i=1
while i<6:
    print(i)
    i+=1# always remember to increment or else the loop goes into infinity loop.
j=1
while j<=10:
    print(j)
    if j==5:
        break
    j+=1
# we use the break statment to break the loop once the condition is fulfiled in this case when the loop reaches 5 it breaks the loop and the code is terminated. 
h=1
while h<=10:
    h+=1
    if h==5:
        print('this is 5')
    continue
# in continue statement the condition that is given if it gets fulfilled then the loop prints the customized statement and continues the loop till the end and terminates.

# we can also use an else statement in while loop so that once the loop ends the statment that is given in the else block will get executed. 
x=1
while x<5:
    print(x)
    x+=1
else:
    print('loop is no longer active')
