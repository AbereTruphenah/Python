#Casting
x = str(4)
y = int(4)
z = float(4)

print(x)
print(y)
print(z)


#Get the type
x = 5
y = "John"

print(type(x))
print(type(y))


#Case sensitive
x = 4
X = "Abere"

print(x)
print(X)


#Multiwords variable names
#camel case
myVariableName = "Abere"
print(myVariableName)

#Pascal case
MyVariableName = "Abere"
print(MyVariableName)

#Snake case
my_variable_name = "Abere"
print(my_variable_name)


#Assigning many values to multiple variables
x,y,z = 6,9,3
print(x)
print(y)
print(z)

#One value to multiple variables
x = y = z = "Jane"
print(x)
print(y)
print(z)


#Unpack a collection
students = ["Mary","Jane","Sally"]
x,y,z = students
print(x)
print(y)
print(z)