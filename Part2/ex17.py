import random
name = input("Greetings Agent. What is your name?")
adjectives = ["Sneaky","Silent", "Fearless","Fierce", "Shadowy"]
animals = ["Panther", "Falcon", "Otter", "Wolf", "Cobra", "Fox"]
codename = random.choice(adjectives) + " " + random.choice(animals)
lucky_number = random.randint(1, 99)
print(f"\nWelcome Agent {name}!")
print(f"Your codename is: **{codename}**")
print(f"Your lucky number is: **{lucky_number}**")
print("Use it wisely in your next mission. Good luck! 🕶️")