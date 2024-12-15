import secrets
import string

def generate_alphanumeric_otp(length=6): # length specifies the length of the OTP
    # create a character set including letters and didgits
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
    
print("Your OTP is: ", generate_alphanumeric_otp())