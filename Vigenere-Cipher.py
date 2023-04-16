# VIGENÈRE CIPHER

# Introduction
print("*" *120)
print("The Vigenère Cipher".center(130))
print("*" *120)
print()
print("Welcome! I suppose that you have something to encypt, am I right? \nWell, in that case, I must help you with that.\n")
print("             (\ __ /)".center(20," "))
print("              (UwU)".center(20," "))
print("       ＿ノ ヽ ノ＼＿ ".center(20," "))
print("     /　`/ ⌒Ｙ⌒ Ｙ　 ".center(20," "))
print("  ( 　(三ヽ人　 /　 　|".center(20," "))
print(" |　ﾉ⌒＼ ￣￣ヽ　 ノ".center(20," "))
print("ヽ＿＿＿＞､＿＿／".center(20," "))
print("          ｜( 王 ﾉ〈 ".center(20," "))
print("           /ﾐ`ー―彡\ ".center(20," "))
print("          |╰         ╯|  \ ".center(20," "))
print("          |       /\       |".center(20," "))
print("          |      /  \      |".center(20," "))
print("          |    /     \     |".center(20," "))
print()
print()
user_decision = (input("If so, please press any key to continue: \n ୧ʕ•̀ᴥ•́ʔ୨\n"))
print()
print()
print()
print("𓆙 " * 40)
print("(૭ ｡•̀ ᵕ •́｡ )૭\n")

# Import string function to generate list.
import string

# Make a list for upper case ASCII letters.
letter_list = list(string.ascii_uppercase)

# Make a dictionary for letter to index range.
letter_to_index = dict(zip(letter_list, range(len(letter_list))))

# Make a dictionary for index range to letter.
index_to_letter = dict(zip(range(len(letter_list)), letter_list))

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

    # Join the letters to form the ciphered message and print.
    print("\nThe ciphered message: " , ''.join(cipher_message))

# Ask the user for message and keyword.
def main():
    print("Just a simple reminder, I could only accept words without spaces and I also prefer it to be in uppercase.\nHowever, if you type in lowercase, I think I could do something about it.\nJust make sure to type in ONLY LETTERS.\n")
    user_message = input("Please input your message here: ").upper()
    user_keyword = input("Please input your keyword here: ").upper()
    print()
    print()
    print()
    print("Just a while...")
    print("(｡ĭ﹏ĭ) ( ĭ﹏ĭ ) (ĭ﹏ĭ｡)")
    print()
    print()
    print()
   


# Print the ciphered message.
    output_message(user_message, user_keyword)
    print("The inputted message: " , user_message)
    print("The inputted keyword: " , user_keyword)

main ()

print()
print()
print()
print("Phew! ( ˘▾˘)~ That was fun encypting your message (๑˃́ꇴ˂̀๑). \nI hope that we can meet again to encrypt more messages in the future ✩°｡⋆⸜(˙꒳​˙ ). Until then, take care!")


