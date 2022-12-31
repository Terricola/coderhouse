# Instructions:
# The components of the password are represented in the form of arrays.
# Use the random method to select at least one character from each array of characters.
# Since the 12-character password is required, so fill the rest of the length of the password left with randomly selected
# characters from an array formed from the combination of all the characters needed in the final password. Anytime the password is generated,
# shuffle the password using random.shuffle() to ensure that the final password does not follow a particular patter

import random

letters = ["a", "b", "c", "d", "e",
            "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t",
            "u", "w", "v", "z"
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

special_chars = [".", "-", "_", "*"]

password = []

if len(password) < 1:
    first_letter = random.choice(letters)
    first_letter = first_letter.capitalize() # Makes the first character upper case
    password.append(first_letter)
    print(password) # Debug purposes
    while len(password) < 11:
        password.append(random.choice(letters))
        password.append(random.choice(numbers))
        random.shuffle(password[1:]) # This mix the password order except the first character that should always be upper case
        print(password) # Debug purposes
    password.append(random.choice(special_chars)) # Final last character should be a special character

# Final result
print(f" La contraseña final es: {password} con un total de {len(password)} caracteres")


    

