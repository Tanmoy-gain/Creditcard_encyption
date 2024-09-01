from cryptography.fernet import Fernet
import os

# Step 1: Generate a key and save it securely
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

# Step 2: Load the key from the file
def load_key():
    return open("secret.key", "rb").read()

# Step 3: Encrypt the credit card number
def encrypt_credit_card(card_number):
    key = load_key()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(card_number.encode())
    return encrypted

# Step 4: Decrypt the credit card number
def decrypt_credit_card(encrypted_card_number):
    key = load_key()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_card_number).decode()
    return decrypted

# Access control management function
def access_control(user_role):
    # In a real application, this would check user roles from a database or an IAM system.
    allowed_roles = ["admin", "finance_manager"]
    if user_role not in allowed_roles:
        raise PermissionError("Access Denied: You don't have permission to access this data.")

# Example usage
if __name__ == "__main__":
    # Generate the key once (only run this once and store the key securely)
    if not os.path.exists("secret.key"):
        generate_key()

    card_number = "1234-5678-9012-3456"
    user_role = "admin"  # or "user", "finance_manager", etc.

    try:
        # Access control check
        access_control(user_role)

        # Encrypt the credit card number
        encrypted_card = encrypt_credit_card(card_number)
        print(f"Encrypted Credit Card: {encrypted_card}")

        # Decrypt the credit card number
        decrypted_card = decrypt_credit_card(encrypted_card)
        print(f"Decrypted Credit Card: {decrypted_card}")

    except PermissionError as e:
        print(e)
