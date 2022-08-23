# exercise

# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
passwords = input('Passwords:').split(",")

def is_in_char_limit(word):
    if len(word) > 6 and len(word) < 12:
        return True
    return False

def is_lowercase(word):
    for l in word:
        if l.islower() == True:
            return True
    return False

def is_uppercase(word):
    for l in word:
        if l.isupper() == True:
            return True
    return False

def is_number(word):
    for l in word:
        if l.isnumeric() == True:
            return True
    return False

def is_special(word):
    for l in word:
        if l == '@' or l == '#' or l == '$':
            return True
    return False

def check_passwords(passwords):
    result = []
    for password in passwords:
        if is_in_char_limit(password) and is_lowercase(password) and is_uppercase(password) and is_number(password) and is_special(password):
            result.append(password)
    return result

print(check_passwords(passwords))
