import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    all_chars = lower + upper + digits + special
    
    if not all_chars:
        raise ValueError("At least one character set must be enabled.")
    
    return ''.join(random.choice(all_chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print(f"Generated Password: {password}")
