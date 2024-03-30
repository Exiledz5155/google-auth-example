from dotenv import load_dotenv
import os
import pyotp

# Load .env file
load_dotenv()

totp_secret = os.environ.get('TOTP')
print(totp_secret)

totp = pyotp.TOTP(totp_secret)

user_code = input("Enter the code from Google Authenticator: ")

# Verify the code
if totp.verify(user_code):
    print("The TOTP code is correct. Authentication successful.")
else:
    print("Invalid TOTP code. Authentication failed.")
