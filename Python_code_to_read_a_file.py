
# Code to read and add to a file

# First we import the functions within the os library, as the Copy File command isn't native Python
import os
os.system('copy c:\\temp\\a.txt c:\\temp\\myfile.txt')


BO = open ('c:\\temp\\myfile.txt', 'r')
print ("Code line 10 : ", BO.name)

# For ReadLine, outputs the lower of number or until the New Line is reached
# For ReadLines, outpus 'all' unread lines, or reads full lines until the number is exceeded.
ReadLine_Character_Count = 4
ReadLine_Second_Character_Count = 12

line = BO.readline(ReadLine_Character_Count)
line2 = BO.readlines(ReadLine_Second_Character_Count )
print ("Open Line: %s" % (line))
print ("Read 2 Line: %s" % (line2))

BO.close


BO = open ('c:\\temp\\myfile.txt', 'r+')
BO.write('\nOverwrite characters\n')
BO.close

BO = open ('c:\\temp\\myfile.txt', 'a')
BO.write('\nAppended\nto the end\n')
BO.close

BO = open ('c:\\temp\\myfile.txt', 'r+')
# For ReadLines, will output whole lines until the number is exceeded
line = BO.readlines(95)
print ("Fourth open: %s" % (line))
BO.close