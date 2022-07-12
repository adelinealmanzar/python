# exercise
username = input('username, please:')
password = input('What\'s your password?')

password_len = len(password)

secret = '*' * password_len

print(f'{username}, your password {secret} is {password_len} letters long')
