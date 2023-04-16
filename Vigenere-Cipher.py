# VIGENÈRE CIPHER

import pyfiglet

# Introduction
print("\33[36m*\33[0m" *120)
result = pyfiglet.figlet_format("The Vigenère Cipher".center(100), font = "digital" )
print(result)
print("\33[33mThe Vigenère Cipher\33[0m".center(130))
print("\33[36m*\33[0m" *120)
print()
print("\33[36mWelcome!\33[0m \33[33mI suppose that you have something to \33[36mencypt, \33[33mam I right? \n\33[35mWell, in that case, I must help you with that.\n\33[0m")
print("\33[31m             (\ __ /)".center(20," "))
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
print("          |    /     \     |\33[0m".center(20," "))
print()
user_decision = (input("\33[36mIf so, please \33[44mpress any key \33[0m\33[36mto continue: \n \33[31m୧ʕ•̀ᴥ•́ʔ୨\33[0m\n"))
print()
print()
print()
print("\33[35m𓆙 " * 40)
print("\33[31m(૭ ｡•̀ ᵕ •́｡ )૭\33[0m\n")

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
    print("\33[34m\nThe ciphered message: \33[0m" , ''.join(cipher_message))

# Ask the user for message and keyword.
def main():
    print("\33[31mJust a simple reminder, I could only accept words without spaces and I also prefer it to be in uppercase.\nHowever, if you type in lowercase, I think I could do something about it.\nJust make sure to type in ONLY LETTERS.\n")
    user_message = input("\33[32mPlease input your message here: \33[0m").upper()
    user_keyword = input("\33[32mPlease input your keyword here: \33[0m").upper()
    print()
    print()
    print()
    print("\33[33mJust a while...")
    print("(｡ĭ﹏ĭ) ( ĭ﹏ĭ ) (ĭ﹏ĭ｡) \33[0m")
    print()
    print()
    print()



# Print the ciphered message.
    output_message(user_message, user_keyword)
    print("\33[35mThe inputted message: \33[0m" , user_message)
    print("\33[33mThe inputted keyword: \33[0m" , user_keyword)

main ()

print()
print()
print()
print("\33[35mPhew! \33[31m( ˘▾˘)~ \33[35mThat was fun encypting your message \33[31m(๑˃́ꇴ˂̀๑). \n\33[35mI hope that we can meet again to encrypt more messages in the future \33[31m✩°｡⋆⸜(˙꒳​˙ ). \33[35mUntil then, take care!\33[0m")


