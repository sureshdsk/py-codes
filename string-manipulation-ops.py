# String Manipulation in Python
# @IdiotInside_
str1 = "idiot inside"
str2 = "hello idiot inside"
str3 = "ab c\n\nde fg\rkl\r\n"
str4 = "   idiot inside   "
str5 = "idiot idiot inside inside"

print ("String: ",str1)
print ("count('i') ",str1.count('i') )
print ("find(i) ",str1.find("i"))
print ("find(s) ",str1.find("s"))
print ("rfind(i) ",str1.rfind("i"))
print ("replace() ",str1.replace("idiot","geek"))


print ("split() ",str2.split(' '))
print ("split('1') ",str2.split(' ', 1 ))

print ("splitlines()",str3.splitlines())
print ("splitlines(True) ",str3.splitlines(True))


print ("lstrip()",str4.lstrip())
print ("lstrip('idiot')",str5.lstrip("idiot"))

print ("rstrip()",str4.rstrip())
print ("rstrip('inside')",str5.rstrip("inside"))

print ("index('idiot')",str5.index("idiot"))
print ("index('idiot',5)",str5.index("idiot",5))
#print ("index()",str5.index("idiot",15)) returns error

print ("rindex(i'')",str1.rindex("i"))
print ("rindex('i',5,7)",str1.rindex("i",5,7))
#print ("rindex('o',5)",str1.rindex("o",5)) returns error


