planet={'name':'Mars', 'moons':2}
"""Add the code to display the planet information in the following format:

__ has __ moon(s)

If you were working with Earth, the output would be Earth has 1 moon(s)"""
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
"""Add a new value to planet with a key of 'circumference (km)'. This new value should store a dictionary with the planet's two circumferences:

polar: 6752
equatorial: 6792"""
planet['circumfrence (km)']={
    "polar": 6752,
    "equatorial": 6792
}
print(f'{planet["name"]} has polar circumfrence of {planet["circumfrence (km)"]["polar"]}')