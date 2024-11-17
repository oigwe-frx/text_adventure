# Step 1: Welcome message
print("Welcome to your adventure simulator.")
print("I am going to ask you a bunch of questions, and then create an epic story with you as the star!")

# Step 2: Ask for the user's name and save it in a variable
name = input("What's your name? ")

# Step 3: Greet the user by name
print(f"Hello, {name}!")

# Step 4: Ask five additional questions and save the answers
favorite_food = input("What's your favorite food? ")
disliked_animal = input("What's an animal you don't like? ")
best_friend = input("What's your best friend's name? ")
favorite_place = input("Where's your favorite place to go? ")
superpower = input("If you could have any superpower, what would it be? ")

# Step 5: Create and print the adventure story
story = f"""
Once upon a time, there was a brave adventurer named {name}. One day, {name} was enjoying a delicious meal of {favorite_food}
at {favorite_place} when suddenly, a wild {disliked_animal} appeared! 

With no one else around, {name} knew it was time to use a secret superpower — the power of {superpower}! 
Just as things were getting intense, {name}'s best friend, {best_friend}, arrived to join in the adventure.

Together, they faced the {disliked_animal} and became heroes of {favorite_place}. The story of {name} and {best_friend}'s 
legendary adventure spread far and wide. And from that day on, {name} was known as the greatest adventurer in the land!
"""

print(story)
