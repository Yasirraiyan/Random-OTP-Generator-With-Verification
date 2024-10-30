
def generateotp(username, password):
    if username == "" or password == "":
        print("Please enter your username and password first!")
    elif username == "Yasir" and password == "Yasyan480":
        print(f"Your OTP is: {otp}")
        user_otp = int(input("Enter the OTP: "))
        checkvalidity(user_otp)
    else:
        print("Invalid username or password")
