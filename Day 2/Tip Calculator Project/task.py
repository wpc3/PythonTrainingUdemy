print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_payment_per_person = round(((bill * (1 + tip/100)) / people),2)


print(f"You should pay ${total_payment_per_person}")
