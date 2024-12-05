planet_moons={"mercury": 0,"venus": 0,"earth": 1,"mars": 2,"jupiter": 79,"saturn": 82,"uranus": 27,"neptune": 14,"pluto": 5,"haumea": 2,"makemake": 1,"eris": 1}
"""Start by retrieving a list with the number of moons, and store this in a variable named moons. Then obtain the total number of planets and store that value in a variable named total_planets."""
moons=planet_moons.values()
total_planets=len(planet_moons)
"""Start by creating a variable named total_moons; this will be your counter for the total number of moons. Then add a for loop to loop through the list of moons, adding each value to total_moons. Finally, calculate the average by dividing total_moons by total_planets and displaying the value."""
total_moons=0
for value in moons:
    total_moons=total_moons+value
print(total_moons/total_planets)