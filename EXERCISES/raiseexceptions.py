"""Create the function str_to_bool.Convert value to lower case letters.
If value matches an entry in true_values the function should return True.
If value matches an entry in false_values it should return False.
If it doesn't match any of the values, it should raise a ValueError, with a message of Invalid entry."""
def str_to_bool(value):
    value=value.lower()
    true_values = ['yes', 'y']
    false_values = ['no', 'n']
    if value in true_values:
        return True
    elif value in false_values:
        return False
    else:
        raise ValueError("Invalid Entry")
    
str_to_bool('yes')