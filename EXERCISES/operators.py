x = 2
y = 5
print(x * y)  #10
print(x + y)  #7
print(x**y)  #32
print(y//x)  #2
print(y%x)   #1

#Bitwise AND
x&=3
'''The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

2 = 0000000000000010
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================
Decimal numbers and their binary values'''

print(x) #2

#Bitwise OR
y|=3
'''The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

5 = 0000000000000101
3 = 0000000000000011
--------------------
7 = 0000000000000111
===================='''
print(y)  #7

#Bitwise XOR
x^=4
'''
The ^ operator sets each bit to 1 if only one of two bits is 1
2 =000000000010
4 =000000000100
---------------
6 =000000000110'''
print(x)  #6

#Bitwise right shift
y>>=2
'''The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 7 becomes 2:
 7 = 0000000000000111
becomes
 2 = 0000000000000001'''
print(y)  #1


#Bitwise left shift
x<<=3
'''The << operator moves each bit the specified number of times to the left. Empty holes at the right are filled with 0's.
If you move each bit 3 times to the left, 6 becomes 48:
6 = 0000110
48 = 0110000'''
print(x)

#NOT
~x
'''Inverts all the bits.
48 = 0110000000000000
-49= 1001111111111111'''
print(x)

#Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

print (x is y)


#Membership operators
x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list

print("egg" not in x)  # returns True because "egg" is not in the list