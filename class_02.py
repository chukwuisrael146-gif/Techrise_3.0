# var1 = "Obi"

# print (var1)
# print (type(var1))

var1 = 25.5
# print (var1)
# print (type(var1))

# var1 = "A"
# var2 = "a"
# print (ord(var1))
# print (ord(var2))

x = str(var1)
print (x)
print (type(x))

x, y, z, = "Orange", "Apple", "Banana"
print (x)
print (y)
print (z)

# Data type 
# Strings

name = "Chukwu Israel"
for C in name:
    print (C)
    
print (len(name))

txt = " Obi is a boy "
print (len(txt))

# slicing

print ("boy" in txt) 
print (txt[0:3])
print (txt[2:5])
print (txt[1:6])
print (txt[2:])

text = "InformationTechnology"
print (text[1:8:2])
print (text[::3])

# list

mylist = ["Orange", "Apple", "Mango", "Banana" , "Grapes", "Pineapple", "Watermelon", "Strawberry", "Cherry", "Peach"]
print (mylist[4])
print (mylist[4][0])


print (txt.upper())
print (txt.strip())

txt2 = "ada is a girl"

print (txt + " " + txt2)
