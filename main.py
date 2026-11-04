import re
import getpass

def analyze_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Consider using 12 or more characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    common_passwords = [
        "password", "12345678", "qwerty",
        "password123", "admin123"
    ]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Avoid common passwords.")

    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, suggestions


def main():
    print("=" * 40)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 40)

    password = getpass.getpass("Enter your password: ")

    strength, score, suggestions = analyze_password(password)

    print("\nPassword Analysis Result")
    print("-" * 40)
    print("Strength:", strength)
    print("Score:", str(score) + "/6")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nYour password meets all the checks!")

    print("\nNote: This is a basic educational checker.")
    print("It does not guarantee password security.")


if __name__ == "__main__":
    main()