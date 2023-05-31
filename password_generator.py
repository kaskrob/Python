import random
import string

def generate_weak_password():
    """Generates a weak password by choosing a word from a list"""
    word_list = ['password', 'secret', '123456', 'qwerty', 'letmein']
    return random.choice(word_list)

def generate_strong_password():
    """Generates a strong password with a mix of lowercase letters,
    uppercase letters, numbers, and symbols"""
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(16))
    return password

def main():
    """Main function to run the password generator"""
    strength = input("How strong do you want your password to be? (weak/strong): ")
    if strength == 'weak':
        password = generate_weak_password()
    elif strength == 'strong':
        password = generate_strong_password()
    else:
        print("Invalid choice. Please choose 'weak' or 'strong'.")
        return
    print("Your password is:", password)

if __name__ == '__main__':
    main()
