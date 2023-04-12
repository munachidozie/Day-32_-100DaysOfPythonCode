import random

name = input("What is your name?  ")
print()

greetings = ["Hello", "Nnọọ", "Konnichiwa", "Guten tag", "Bore da", "Pẹlẹ o", "Sannu"]
text = random.randint(0, 6)

print(f"{greetings[text]} {name}")