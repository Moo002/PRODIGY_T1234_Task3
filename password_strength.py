import re

def assess_password_strength(password):
    """Evaluates the strength of the provided password based on various criteria."""
    # Initialize score and feedback list
    score = 0
    feedback = []

    # Check password length
    password_length = len(password)
    if password_length >= 12:
        score += 4
    elif password_length >= 8:
        score += 2
    else:
        feedback.append("Password is too short. Consider using at least 8 characters.")
    
    # Check for different types of characters
    def check_character_type(pattern, message):
        nonlocal score
        if re.search(pattern, password):
            score += 3
        else:
            feedback.append(message)
    
    check_character_type(r'[A-Z]', "Include at least one uppercase letter.")
    check_character_type(r'[a-z]', "Include at least one lowercase letter.")
    check_character_type(r'\d', "Include at least one digit.")
    check_character_type(r'[!@#$%^&*(),.?":{}|<>]', "Include at least one special character (e.g., !, @, #, $, etc.).")
    
    # Check for common patterns or sequences
    common_patterns = ['password', '1234', 'qwerty', 'abcd', 'letmein', 'welcome']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 4
        feedback.append("Avoid common patterns like 'password' or '1234'.")

    # Check for sequential characters and repeated characters
    if re.search(r'(012|123|234|345|456|567|678|789)', password):
        score -= 2
        feedback.append("Avoid sequences like '123' or '789'.")
    
    if re.search(r'(.)\1{2,}', password):
        score -= 2
        feedback.append("Avoid repeating the same character more than twice in a row.")

    # Determine strength level
    strength = "Very Weak"
    if score >= 10:
        strength = "Very Strong"
    elif score >= 7:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    elif score >= 2:
        strength = "Weak"

    return strength, feedback

def main():
    """Main function to interact with the user and display password strength assessment."""
    user_password = input("Enter your password: ")
    strength, feedback = assess_password_strength(user_password)

    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions for improvement:")
        for tip in feedback:
            print(f"- {tip}")

if __name__ == "__main__":
    main()

