"""Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum."""
number1 = 30
number2 = 40
product = number1 * number2
if product >= 1000:
    print("The product is",product)
else:
    print(number1 + number2,"is the sum")