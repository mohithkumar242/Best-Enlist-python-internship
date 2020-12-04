#1
import re

string=input("enter a string")
chari = re.compile(r'[^a-zA-Z0-9.]')
string = chari.search(string)
if(not bool(string)):
    print("string format is corrrect")
else:
    print("String format is not correct")

print()
print()


#2
text=input("enter a string")
pattern = '\w*ab\w*'
if re.search(pattern,  text):
	print('Found a match!')
else:
	print('Not matched!')



print()
print()


#3
string1=input("enter a string")
fo=re.findall("[0-9]+",string1)
print(fo)

print()
print()

#4
string2=input("enter a string :")
print(re.findall(r"\d{1,3}",string2))


print()
print()

#5
string3=input("enter a string")
print(re.findall(r"[A-Z]+",string3))
