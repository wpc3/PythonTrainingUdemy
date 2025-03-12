import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

randomGenerator = random.randint(0,4)

if randomGenerator == 0:
    print(friends[0])

elif randomGenerator == 1:
    print(friends[1])

elif randomGenerator == 2:
    print(friends[2])

elif randomGenerator == 3:
    print(friends[3])

else:
    print(friends[4])



