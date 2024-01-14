import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

password_length = int(input("Enter the desired password length: "))
num_passwords = int(input("Enter the number of passwords to generate: "))
file_name = input("Enter the file name to save the passwords: ")

passwords = [generate_password(password_length) for _ in range(num_passwords)]
save_passwords_to_file(passwords, file_name)
print(f"{num_passwords} passwords saved to", file_name)
