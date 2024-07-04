import re

def assess_password_strength(password):
    strength = 0

    # Check length
    if len(password) < 8:
        return "Weak", "Password should be at least 8 characters long."

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1

    if strength == 4:
        return "Strong", "Password is strong."
    elif strength >= 2:
        return "Medium", "Password is medium strength. Consider adding more character types."
    else:
        return "Weak", "Password is weak. Consider adding more character types and increasing length."

def main():
    password = input("Enter a password: ")
    strength, feedback = assess_password_strength(password)
    print(f"Password strength: {strength}")
    print(feedback)

if __name__ == "__main__":
    main()
    