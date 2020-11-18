
# This is a list, built via a comparison; then with items added.
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
combs.append("'\n'")
print (combs )

# This is also a list, built using For Loops.    For loops are 'weird' because the #next_item statement doesn't exist.  
#    rather, ending indentation ends the For Loop.
bath = []
for x in [3,2,1]: 
    for y in [3,1,4]:
        y =y
        print(y)
        if x != y:
            bath.append((x,y))

# Listss (and other variables) can be combined together via 
print (combs + bath  )

message1 = '{:10.2f} and   {:d}'.format(1.234234234, 12)

print (message1)

txt = "For only {price:,.2f} dollars!"
print(txt.format(price = 9999949))

# List Example - use [ ]  or 
#    can also use .append() to add items from the list.
#    ListName[-1]  will return the last item in a list.
UserAge = [21,22,23,24,25]
UserAge.append(26)
print(UserAge)
del UserAge[-2]
print ("Updated list with second last item removed is %s ."%(UserAge))

# This is a Tuple - a Tuple can never be modified - 
Tupple_example_Months_of_Year = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov","Dec")
print (Tupple_example_Months_of_Year )

# This is a Dictonary - It has two columns, the first must have all unique values.  It can only have two columns
Dict_Test = {"One":"Singular","Two":"Double", "Three":"Triple", "Four":"", "Five":"Still don't know", "Six":6}
Dict_test_2 = dict(One="Singular",Two="Double", Three="Triple", Four=0, Five="Still don't know", Six= 6)
print(Dict_Test["Four"])
print(Dict_test_2["Four"])

variable = "I'm a variable!"; var1 = "so am I"; var2 = "Me too!"
#Insert a variable into a print statement via either
print("test %s" %(variable))   # where %  symbol means variable, s means a string
#or
print( '''test {}, {}'''.format(var1, var2))
print( f'Our varialbes are var1 with value {var1} and var2 with value {var2}')


# Unprintable Characters List:
#  \t  tab  line
#  \n  new line
#  \"   \\   \'   prints the character after the \


# Triple quotes (within print only?) include chariage returns within the output
# The input() function lets user enter data
variable = input(''' What variable
would
you 
like
......
to ENTER!  ''')

print("You entered variable %s" %(variable)) 


#  Else if sytax is a bit weird - elif on a new line, not indented.
if variable == "Awesome":
    var1 = "Awesome"
elif variable == "cool":
    var1 = "Enh - decent"
elif variable == "Wooo":
    var1 = "boo"
else:
    var1 = "match failed"

print (var1, "  ", variable)


for index, temp_var in enumerate(Tupple_example_Months_of_Year):
    print ("\t", index, "is the index value, and the month is", temp_var)


#  A For loop works off a list similar object (including tuple and Dic).  
#      The function Range() easily generates a list object.
#      It can also work off a String object, where every character within the string is a list member
#      The key word    break    ends the for loop
#      The key word    continue    pops the loop onto the next item


#  A While loop does all the indented statements and then jumps back to the top and re-evaluates the While


# Try     Except     runs code within the Try - than if it encounters an error, jumps to the Except statement.
#     The   Except   statement also has options - include the possible error category, and it will use that specific Except type.


#  Built in code includes pre-written classes, variables and functions, designed
#     to perform common tasks, and saved in files known as modules.


#   Replace function is 'fun'
newString = "Hello  World".replace("World", "universe")

#  Python defines your own Functions the syntax
#       def  functionName (list of parameters):
#             code detailing what the function should do
#              return  [expression]
#


def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck):
        if (numberToCheck%x == 0):
            return False
    return True

To_Check = int(input("enter a possible prime number: "))
print(checkIfPrime(To_Check))

# Within the same folder, I've created a file titled "Check_If_Prime".  This file has a Function, that I use below.
import Check_If_Prime
print(Check_If_Prime.Module_checkIfPrime(To_Check))





# Python allows default parameter values
def someFunction (a, b, c=1, d=2, e=3):
    print(a, b, c, d, e)

#  Python accepts a Variable Length Argument List
#    This is called by adding a  *  before the parameter variable

# This function adds all the numbers passed to it.
#  If you want your function to receive a Dictionary instead of a list; use ** before the variable name, rather than *  
def addNumbers(*num):
        sum = 0
        for i in num:
            sum = sum + i
        print(sum)


f = open ('c:\\temp\\myfile.txt', 'r+')
firstline = f.readline()
secondline = f.readline()
print(firstline)
print(secondline)
f.close()


