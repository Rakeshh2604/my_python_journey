# instead of if else statements we can also use match statements and the syntax is as follows:
# match expression: 
#     case x:
#         statement
#     case y:
#         statement
#     case z:
#         statement
day=int(input('enter any number between 1-7'))
match day:
    case 1:
        print('momday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print('saturday')
    case 7:
        print('sunday')
# we can also use _ as a last option this is just like an else statement in if else. when there are no other cases that fulfill then the last case with the _ gets printed. 
days=5
match day:
    case 6:
        print('saturday')
    case 7:
        print('sunday')
    case _:
        print('looking forward for next week')
# we can even combine the cases and print a single statement.
day1=4
match day1:
    case 1|2|3|4|5:
        print('this is a weekday')
    case 6|7:
        print('this is a weekend')