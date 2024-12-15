import secrets

def generate_numeric_otp(length=6): # length specifies the length of the OTP
    return ''.join(str(secrets.randbelow(10)) for _ in range(length))

print("Your OTP is: ", generate_numeric_otp())