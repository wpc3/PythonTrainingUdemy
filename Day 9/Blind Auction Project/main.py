import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)
print("Welcome to the secret auction program.")

bidding_dictionary = {}

auction_game = True

while auction_game:
    name_input = input("What is your name? \n")
    bid_input = int(input("What is your bid? \n"))
    bidding_dictionary[name_input] = bid_input
    adding_bidder_input = input("Would any one else like to bid? y/n \n").lower()

    if adding_bidder_input == 'y':
        print("\n" * 100)
    elif adding_bidder_input != 'y' or adding_bidder_input != 'n':
        print("Please enter y or n to continue")

    # print(bidding_dictionary)

    key_with_max_value = max(bidding_dictionary, key=bidding_dictionary.get)
    max_value = bidding_dictionary[key_with_max_value]

    if adding_bidder_input == 'n':
        auction_game = False
        print(f"The winner is {key_with_max_value} with a bid of ${max_value}.")

# def user_name_input():
#     global bid_input
#     name_input = input("What is your name? \n")
#     try:
#         bid_input = int(input("What is your bid? \n"))
#     except:
#         print("Please type a number")
#         user_name_input()
#     bidding_dictionary[name_input] = bid_input
#
# def continue_bid():
#     adding_bidder_input = input("Would any one else like to bid? y/n \n").lower()
#     print("\n" * 100)
#     key_with_max_value = max(bidding_dictionary, key=bidding_dictionary.get)
#     max_value = bidding_dictionary[key_with_max_value]
#     if adding_bidder_input != 'y' or adding_bidder_input != 'n':
#         continue_bid()
#     if adding_bidder_input == 'n':
#
#
#         auction_game = False
#         print(f"The winner is {key_with_max_value} with a bid of ${max_value}.")
#
#
# def game_logic():
#     # auction_game = True
#     while auction_game:
#         user_name_input()
#         continue_bid()
#         print(bidding_dictionary)
#
#
#
# game_logic()