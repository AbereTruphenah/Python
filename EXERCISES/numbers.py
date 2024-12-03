x = 4
y = 4.55
z = 1j

print(type(x))
print(type(y))
print(type(z))

#Type conversion
x = 35E2 #E = 10 , E2=E^2
print(type(x))
print(int(x))

y = 2
print(complex(y))

z = "0.5"
print(complex(z))



#Random number
import random
print(random.randrange(0,10))