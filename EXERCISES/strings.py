#Quotes inside quotes
print("She's a geneous")
print('He is called "Kim"')

#Multiline strings
print("""During the holidays,
I usually go to visit
my grandparents. They are the best people to be with.""")

print('''I joined the WaziLab Iot certification program.
It is the best, 
as it offers many courses for free.''')


#Strings as arrays
x = "Barongo"
print(x[5])

#Looping through a string
for y in "cone":
    print(y)




#String length
a = "Abere Truphenah"
print(len(a))#15


#Check string
x = "This institution's buildings were well designed"
print("institution" in x)#true
        #OR
if "institution" in x:
    print('Yes "institution" is in the string')


#Check if not
txt = "I love my family"
print("sister" not in txt)#True

       #OR
if "sister" not in txt:
    print("I don't have a sister")      



#Slicing Strings
x = "How old are you?"
print(x[5:15])#ld are you

#Slice from thre start
print(x[:15])#How old are you

#Slice to the end
print(x[4:])#old are you?

#Negative indexing
print(x[-8:-1])#are you


#Upper case and lower case
x = "Hello World"
print(x.upper())
print(x.lower())

#Remove whitespace
x = "  I like cooking  "
print(x.strip())

#Rplace string
x = "Hey there"
print(x.replace("Hey","Hello"))

#Split string
x = "hello, there"
print(x.split(' '))
print(x.split(','))


#Concatenate strings
a = "hello"
b = "world"
c = a + " " + b
print(c)

#Formatting strings
#F-strings
price = 100
txt = f"The dress costs {price}"
print(txt)

#Placeholders and Modifiers
price = 2000
txt = f"The device costs {price} shillings."#shillings is a placeholder
print(txt)

txt = f"The device costs {price:.2f} shillings."#add a modifier by adding a colon followed by a legal formatting type.
print(txt)

txt = f"The device costs {3*100} shillings."
print(txt)



#Escape Characters
#Backslash- allows you to use double quotes inside double quotes.
print("The car \"BMW\" passed here in the morning.")
