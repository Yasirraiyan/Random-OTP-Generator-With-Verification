def checkvalidity(user_otp):
    # Check if the user-provided OTP matches the generated OTP
    if user_otp == otp:
        print("Verification Successful!")
    else:
        print("Invalid OTP!!")
