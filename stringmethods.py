

 #Strings are immutable

a="!!!! Frank !!!!!!!!!!!!!! Frank!!"
print(len(a))

print(a.upper())

print(a.lower())

print(a.rstrip("!"))
  #only strips the trailing characters

print(a.replace("Frank","John"))  
  #replace all occurances of string

print(a.split(" "))
  #split the string into a list of words


b="introduction tO pYthon"
print(b.capitalize())
#capatalize converts only the first character and rest to lowercase

c="Welcome to console!!!"
print(len(c))
print(len(c.center(50)))
 #center method aligns the string to the center as per the parameters

print(a.count("Frank"))
 #counts the number of time a value occured in the string

print(a.startswith("!!"))
 #checks if the string starts with the given value

print(a.endswith("!!!"))
 #gives the output in True or False

 # We can also check for a value in between the string by providing the start and end index positions
print(c.endswith("to",4,10))

str1="He's name is Dan.He is an honest man"

print(str1.find("is"))
print(str1.find("kjha"))  #if it does not finds the value in the string it return -1


print(str1.index("is"))  #similar to find but if it does not find the value in the string it gives error

print(str1.isalnum()) #returns True only if the enire string only consists of A-Z,a-z,0-9(alphanumeric) or returns false
print(str1.isalpha()) #returns True only if the enire string only consists of A-Z

str2="Welcome00"
print(str2.isalnum())
print(str2.isalpha())

print(str2.islower())
 #returns True if the string contains only lowercase characters

print(str1.isprintable())
 #returns True if the string contains only printable characters
str3="Frank is good\n"
print(str3.isprintable())

s1="    "
s2="    "
print(s1.isspace())
print(s2.isspace())
#returns True if the string contains only spaces

str1="World Health Organization"
print(str1.istitle())
#returns True if the string contains only title case characters

print(str1.isupper())
#returns True if the string contains only uppercase characters

print(str1.swapcase())
#returns the string with all uppercase characters changed to lowercase characters and vice versa

str1="his name is dan.dan is an honest man."
print(str1.title())
#returns the string with the first character of each word capitalized