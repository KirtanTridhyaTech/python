import sys
print(sys.version)
print(sys)

if(5 < 2):
 print("5 is greater than 2")
if 5 > 2:
 print("okay")

x = 2
y = "Hello"
print(x)
print(y)
#This is a comment line
print("Comment define using #") #comment
"""
multiline comment
working
"""
print("comment")
a,b,c = 2,5,6
print(b,end="\n")

a = b = c = 4
print(b)
b=3
print(a,b)
x = [3,5,32,6]
a,b,c,d = x
print(b)