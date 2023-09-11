# Author: Giovanni Marassi
# Date: 2023/09/11
# Version: 1.0

import argparse
import secrets
import string


def generate_password(password_lenght, alphabet):
    """
        This function is actually the function that generates
        the random password, based on lenght secret.choice()
        will take a random char from the list "alphabet" and add it
        to password variable.
        
        INPUT: (int) password_lenght, (str) alphabet; 
        OUTPUT: (str) password;
    """
    password = ""
    
    for i in range(password_lenght):
        password += ''.join(secrets.choice(alphabet))
        
    return password


def main():
    """
        When script is launched based on number entered as argument,
        random password is generated.
    """
    parser = argparse.ArgumentParser(description="Password generator")
    parser.add_argument("-password_lenght", type=int)
    args = parser.parse_args()
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    alphabet = letters + digits + special_chars
    
    password = generate_password(args.password_lenght, alphabet)

    print(f"Password generated is: {password}\n")

if __name__ == "__main__":
    main()