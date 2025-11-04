# # an if statement is written by using the keywords if and else. so we give it a statement and if the statement is true then the command inside the if keyword would get executed or else the statement in the else keyword would get executed. 
# a=int(input('enter any number'))
# if a<10:
#     print('yes a is smaller than 10')
# else:
#     print('no a is not less than 10')
# # while using if else statements indentation is a must and if there is no indentation then the terminal raises an error. the standard indentation that is used is four spaces. 
# # we can have multiple statements in a if block. 
# # elif statement is also used in python if statements it works as follows first the terminal checks the if statement if it is false then it goes to elif and if its true it prints the statement and the code is terminated but even if that is false then it prints the else statement.
# a=70
# if a>100:
#     print('mango')
# elif a==65:
#     print('apple')
# elif a==75:
#     print('orange')
# elif a>65:
#     print('bye fucker')
# else:
#     print('sorry the number is not available')

# # else statements 
# a=10
# b=20
# if a==b:
#     print('both are equal')
# elif a>b:
#     print('a is greater than b')
# else:
#     print('b is greater than a')
# # else statement is a default method in if else. that is if the prompt is not true for either if or any other elif statement then it directly goes into else and prints the statement else statements does not require any kind of prompt of command to check anything if everything else fails the else statement gets printed. 
# a=input('please enter your email')
# if len(a)>0:
#     print(f'welcome {a}')
# else:
#     print('please enter a valid email')
# # if else statements can also be used with logical operators such as and, or, not

# a=100
# b=200
# if a==b or a<b or a>b:
#     print('b is greater')
# # in the same way we can also use the and, not statements and statement is used when both the statements are true then it prints the statement and not statment is used if both the statements are false then it prints true or the statement that is given.
# username='rakesh'
# password='rak2604'
# login=True
# if username:
#     if password:
#         if login:
#             print('welcome user')
#         else:
#             print('account is inactive')
#     else:
#         print('please enter password')
# else:
#     print('please enter username')



# a=int(input('enter the first number'))
# b=int(input('enter the second number'))
# c=int(input('enter the third number'))
# if a>b or a>c: 
#     print(f'{a} is larger than the other two')
# elif b>c or b>a:
#     print(f'{b} is larger than the other two')
# else:
#     print(f'{c} is larger than the other two')

# sentence=input('enter any sentence to find out the vowels in it ' )
# vowels='aeiou'
# char=0
# for i in sentence.lower():
#     if i in vowels:
#         char+=1
# print(f'the number of vowels in the sentence are {char}')

# grade=int(input('enter the percentage to check for grade'))
# if grade>90 and grade<=100:
#     print('Grade A')
# elif grade>=80:
#     print(' Grade B ')
# elif grade >=70:
#     print('Grade C')
# elif grade >=60:
#     print('Grade D')
# else:
#     print('Fail ')

# units=int(input('enter the number of units to find out the price '))
# if units<=100:
#     print(f'the final bill is {(units*1.5)+50} rs ')
# elif units>101 and units <=200:
#     print(f'the final bill is {(units*2.5)+50} rs')
# elif units>200:
#     print(f'the final bill is {(units*4)+50} rs ')

username=input('please enter your username')
password=input('please enter your password')
user='admin'
passw='1234'
if username==user and password==passw:
    print('login successful')
elif username==user:
    print('wrong password')
else:
    print('both are wrong')