# true and false are the boolean types in python.
# true and false are also the keywords in python

# operations that give boolean type

a = 5
b = 10
c = 15

# relational operations
print(b>a) # true
print (b!= a) # true
print (b>a) #false
print (a=c) # false


# logical operations
print(b > a and a == c) # false
print(b > a or a == c) # true
print(not true) # false
print(not false) # true
print(not a) # false

# membership operation
print(2 in [1,2,3]) # true
print(3 not in [1,2,3]) # false

# identity operation
a = 1
b = 1
print(a == b) # true
print(a is be) # true
a = 12343254423 # it is created in one memory location
b = 12343254423 # but it is created in another memory location
print(a == b) # true
print(a is b) # false






# concept of truthy and falsy
# truthy
# all non-empty datatypes and non-zero number are truthy values
# all these datatypes are truthy datatypes

# Truthy
# All non-empty datatypes and non-zero numbers are truthy values
a = 12 #integer
b = 5.7 #float
c = [1, 2] #list
d = (4, 5) #tuple
e = {1, 2} #set
f = {"name": "Jon"} #dictionary
g = True #boolean
# All these datatypes are truthy datatypes
# We can check the truthiness of the data using bool function

print(bool(b))  # True
# we can check the truthiness of the data using bool function

# falsy
# all empty datatypes and zero are falsy values
a = 0
b = 0
c = []
d = ()
e = {}
f = set{}
g = False
h = None
print(bool(g)) # false

# python booleans are subclass of the integer class. That means True is 1 and False is 0
a = True
b = 3
print (a+b) # 4
print(70* false) # 0
print (true + true) # 2