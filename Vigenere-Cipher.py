# VIGENÈRE CIPHER

# Import string function to generate list.
import string

# Make a list for upper case ASCII letters.
letter_list = list(string.ascii_uppercase)

# Make a dictionary for letter to index range.
letter_to_index = dict(zip(letter_list, range(len(letter_list))))

# Make a dictionary for index range to letter.
index_to_letter = dict(zip(range(len(letter_list)), letter_list))


# Ask the user for message and keyword.
def main():
    user_message = input("Please input your message here: ").upper()
    user_keyword = input("Please input your keyword here: ").upper()


# Decryption/encryption of the message with keyword.


# Print the ciphered message.
    
main ()