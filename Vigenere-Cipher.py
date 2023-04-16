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
def output_message(user_message, user_keyword):
    cipher_message = []

    # Loop the process so that the number of letter in the message will all be encrypted
    for i in range(len(user_message)):

        # Identify the position of the letter of the message and keyword.
        message_index = letter_to_index[user_message[i]]
        keyword_index = letter_to_index[user_keyword[i % len(user_keyword)]]

        # Add the numbers of position of message and keyword
        combined_sum = (message_index + keyword_index)% 26

        # From the sum of the message and keyword, get the equivalent letter of the number.
        cipher_message.append(index_to_letter[combined_sum])
        print("The ciphered message: " , ''.join(cipher_message))

# Print the ciphered message.
    
main ()