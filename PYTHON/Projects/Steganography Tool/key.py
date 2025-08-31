from cryptography.fernet import Fernet

# Generate key once
key = Fernet.generate_key()

# Save it to a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("Key generated and saved as secret.key")
