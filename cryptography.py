from cryptography.fernet import Fernet
import json
import os

# Generate or load encryption key
def load_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
cipher = Fernet(key)

PASSWORD_FILE = "passwords.json"

def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def add_password(site, username, password):
    encrypted_password = cipher.encrypt(password.encode()).decode()
    passwords = load_passwords()
    passwords[site] = {"username": username, "password": encrypted_password}
    save_passwords(passwords)
    print(f"Password for {site} saved successfully!")

def get_password(site):
    passwords = load_passwords()
    if site in passwords:
        decrypted_password = cipher.decrypt(passwords[site]["password"].encode()).decode()
        print(f"Username: {passwords[site]['username']}, Password: {decrypted_password}")
    else:
        print("Site not found!")

def main():
    while True:
        print("\n1. Add Password\n2. Retrieve Password\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            site = input("Enter site name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_password(site, username, password)
        elif choice == "2":
            site = input("Enter site name: ")
            get_password(site)
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
