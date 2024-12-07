"""Starting with the variables you've just created, create a while loop. The while loop will run while new_planet is not set to done.
Inside the loop, check to see whether the new_planet variable contains a value, which should be the name of a planet. This is a quick way to see whether the user has entered a value. If they have, your code will append that value to the planets variable.
Complete the while loop by using input to prompt the user to enter a new planet name or done if they're done entering planet names. You'll store the value from input in the new_planet variable.
Finally, outside of the while loop, print the list of planets by using print."""
new_planet=''
planets=[]
while new_planet.lower() != "done":
    if new_planet:
        planets.append(new_planet)
    new_planet=input("Enter name of a planet if not done else 'done' to exit.")
print(planets)