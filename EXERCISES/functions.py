def generate_report(main_tank,external_tank,hydrogen_tank):
    output=f"""Fuel report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)
generate_report(80,70,75)


from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
    arrival_time()
    
    
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')
fuel_report(main=50,external=100,emergency=60)


def numbers(num1,num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2
result = numbers(30,40)
print("The result is", result)
