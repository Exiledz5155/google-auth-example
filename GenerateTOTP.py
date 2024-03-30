import pyotp
import qrcode
import os

# Generate a TOTP secret
totp_secret = pyotp.random_base32()
print(f"Your TOTP secret is: {totp_secret}")

# Generate a provisioning URI and display QR code URL
totp = pyotp.TOTP(totp_secret)
user_email = "Access 1"
issuer_name = "SSR Data Interface"
provisioning_uri = totp.provisioning_uri(name=user_email, issuer_name=issuer_name)

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(provisioning_uri)
qr.make(fit=True)

# Save QR code as image
img = qr.make_image(fill_color="black", back_color="white")
img.save("totp_qr.png")

# Save TOTP as environment variable
os.environ['TOTP'] = totp_secret

# Append TOTP to .env file
env_path = ".env"
with open(env_path, "a") as env_file:
    env_file.write(f"TOTP={totp_secret}\n")

print("Scan the QR code from Google Authenticator. The QR code image is saved as totp_qr.png.")
print("Alternatively, manually add the secret to Google Authenticator.")
print("Provisioning URI for manual entry (if needed):")
print(provisioning_uri)
print("The TOTP has also been saved in .env")
