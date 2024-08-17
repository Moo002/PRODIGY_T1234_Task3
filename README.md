# PRODIGY_T1234_Task3
Password Strength Assessment tool
# Password Strength Checker

## Overview

This Python script evaluates the strength of a given password based on various criteria and provides feedback to improve password security. It checks for password length, character variety, common patterns, and sequences, offering suggestions for stronger passwords.

## Features

- **Length Check**: Scores based on password length.
- **Character Variety**: Ensures inclusion of uppercase letters, lowercase letters, digits, and special characters.
- **Common Patterns**: Flags common and easily guessable patterns.
- **Sequential and Repeated Characters**: Identifies and warns against predictable sequences and repeated characters.

## Usage

1. **Run the Script**: Execute the script using Python.
    ```bash
    python password_strength_checker.py
    ```

2. **Enter Password**: When prompted, enter the password you wish to evaluate.

3. **View Results**: The script will display the strength of the password and provide feedback for improvement.

## Example

```bash
Enter your password: P@ssw0rd123
Password Strength: Moderate
Suggestions for improvement:
- Include at least one special character (e.g., !, @, #, $, etc.).
- Avoid common patterns like 'password' or '1234'.
