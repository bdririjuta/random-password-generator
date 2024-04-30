import random
import string

generate_len=8
characters=string.ascii_letters + string.digits + string.punctuation
# Generate the password
password = ""
for i in range(generate_len):
    password += random.choice(characters)


print(" Your Random Password:", password)