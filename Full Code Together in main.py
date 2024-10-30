import random

# Get user input for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Generate an OTP between 1000 and 99999999
otp = random.randrange(1000, 99999999)

def generateotp(username, password):
    if username == "" or password == "":
        print("Please enter your username and password first!")
    elif username == "Yasir" and password == "Yasyan480":
        print(f"Your OTP is: {otp}")
        user_otp = int(input("Enter the OTP: "))
        checkvalidity(user_otp)
    else:
        print("Invalid username or password")

def checkvalidity(user_otp):
    # Check if the user-provided OTP matches the generated OTP
    if user_otp == otp:
        print("Verification Successful!")
    else:
        print("Invalid OTP!!")

# Call the function with provided username and password
generateotp(username, password)
