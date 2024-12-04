name = input("Enter your name ")
print("Your name is",name)


x = "Python"
y = "is"
z = "awesome"
print(x,y,z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Global Variables
x = "Abere"
def myfunc():
    print("My name is " + x)
myfunc()    


#Creating a variable inside a function with the same name as the global variable
x = "dancing"
def myfunc():
    x = "singing"
    print("I love " + x)#singing
myfunc()
print("I love " + x)#dancing


#Global keyword
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("That is " + x)    



x = "awesome"
def myfunc():
    global x
    x = "nice"
myfunc()
print("That is " + x)    