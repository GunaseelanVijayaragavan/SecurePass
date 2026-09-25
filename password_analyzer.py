# SecurePass - Password Strength Analyzer

COMMON_PASSWORDS = {
    "123456",
    "password",
    "12345678",
    "qwerty",
    "123456789",
    "admin",
    "welcome",
    "letmein",
    "password123",
    "1234567890"
}


def analyze_password(password):
    score = 0
    suggestions = []
    checks = []

    # Length check
    if len(password) >= 8:
        score += 20
        checks.append(("Length", True))
    else:
        suggestions.append("Use at least 8 characters.")
        checks.append(("Length", False))

    # Extra points for longer passwords
    if len(password) >= 12:
        score += 10

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 15
        checks.append(("Uppercase", True))
    else:
        suggestions.append("Add at least one uppercase letter.")
        checks.append(("Uppercase", False))

    # Lowercase check
    if any(char.islower() for char in password):
        score += 15
        checks.append(("Lowercase", True))
    else:
        suggestions.append("Add at least one lowercase letter.")
        checks.append(("Lowercase", False))

    # Number check
    if any(char.isdigit() for char in password):
        score += 15
        checks.append(("Number", True))
    else:
        suggestions.append("Add at least one number.")
        checks.append(("Number", False))

    # Special character check
    if any(not char.isalnum() for char in password):
        score += 15
        checks.append(("Special Character", True))
    else:
        suggestions.append("Add at least one special character.")
        checks.append(("Special Character", False))

    # Common password check
    common = password.lower() in COMMON_PASSWORDS

    if common:
        score = min(score, 30)
        suggestions.insert(
            0,
            "Avoid commonly used passwords."
        )

    # Strength calculation
    if common or score < 40:
        strength = "WEAK"
    elif score < 75:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return {
        "score": score,
        "strength": strength,
        "suggestions": suggestions,
        "checks": checks,
        "common": common,
        "length": len(password)
    }


# Standalone testing
if __name__ == "__main__":

    print("=" * 40)
    print("        SECUREPASS")
    print(" Password Strength Analyzer")
    print("=" * 40)

    password = input("\nEnter a test password: ")

    result = analyze_password(password)

    print("\n========== RESULT ==========")

    print(f"Score    : {result['score']}/100")
    print(f"Strength : {result['strength']}")

    if result["common"]:
        print("⚠ WARNING: Commonly used password")

    if result["suggestions"]:
        print("\nSuggestions:")

        for suggestion in result["suggestions"]:
            print(f"- {suggestion}")

    else:
        print("\n✓ Password meets all basic requirements!")

    print("\nNote: Password is analyzed locally.")
    print("It is not stored by this program.")