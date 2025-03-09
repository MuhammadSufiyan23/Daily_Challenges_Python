# DAY-9 CHALLENGE

import re

def check_password_strength(password):
    if len(password) < 6 or password.isalpha():
        return "Weak ❌"

    elif len(password) >= 8 and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Moderate ⚠"

    elif (
        len(password) >= 8
        and re.search(r"[A-Z]", password)  
        and re.search(r"[a-z]", password)  
        and re.search(r"\d", password)  
        and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)  
    ):
        return "Strong ✅"

    else:
        return "Moderate ⚠"

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
