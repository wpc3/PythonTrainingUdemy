# TODO-1: Import and print the logo from art.py when the program starts.
import art
logo = art.logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):

    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter in alphabet:


                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                output_text += alphabet[shifted_position]
        else:
                output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")
    # run_it_back = input("Would you like to play again? y/n \n").lower()
    # if run_it_back != "y":
    #     play_again = False


    # play_again = input("Would you like to encode or decode again? Y/N \n").lower()
    #
    # if play_again == "y":
    #     caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    # elif play_again != "y" or play_again != "n":
    #     print("please type y or n")
    #     play_again



# TODO-3: Can you figure out a way to restart the cipher program?
play_again = True
while play_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    runBack = input("Would you like to try again? y/n \n").lower()

    if runBack != "y":
        play_again = False



