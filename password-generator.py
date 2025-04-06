import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
    """
    Generates a secure random password based on user preferences.

    Args:
        length (int): Length of the password (default is 12).
        include_uppercase (bool): Whether to include uppercase letters.
        include_numbers (bool): Whether to include numbers.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    # Define character pools
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special_chars = string.punctuation if include_special_chars else ""

    # Combine all selected character pools
    all_characters = lowercase_letters + uppercase_letters + numbers + special_chars

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input for password preferences
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        include_uppercase = input("Include uppercase letters? (y/n, default is y): ").lower() != 'n'
        include_numbers = input("Include numbers? (y/n, default is y): ").lower() != 'n'
        include_special_chars = input("Include special characters? (y/n, default is y): ").lower() != 'n'

        # Generate and display the password
        password = generate_password(length, include_uppercase, include_numbers, include_special_chars)
        print(f"Your generated password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()