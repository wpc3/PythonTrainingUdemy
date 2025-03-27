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
    # print(bidding_dictionary)

    key_with_max_value = max(bidding_dictionary, key=bidding_dictionary.get)
    max_value = bidding_dictionary[key_with_max_value]




    # for bid in bidding_dictionary:
    #     if bidding_dictionary[bid] > highest_bid.values():
    #         bidding_dictionary = highest_bid
