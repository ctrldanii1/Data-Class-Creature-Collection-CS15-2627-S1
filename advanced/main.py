from dataclasses import dataclass

@dataclass
class Variant:
    name: str
    alias: str
    earth: int
    health: float

miles = Variant("Miles Morales", "Spider-Man", 1610, 180.5)
gwen = Variant("Gwen Stacy", "Spider-Woman", 65, 165.0)
hobie = Variant("Hobie Brown", "Spider-Punk", 138, 210.0)

print("\n Create Your Own Variant")
name = input("\nEnter Variant Name: ")
alias = input("Enter Variant Alias: ")

while True:
    try:
        earth = int(input("Enter Earth Number (whole number): "))
        break
    except ValueError:
        print("Error: Please enter a valid whole number for the Earth.")

while True:
    try:
        health = int(input("Enter Health Number (number): "))
        break
    except ValueError:
        print("Error: Please enter a valid number for the health.")

user_variant = Variant(name, alias, earth, health)

print("\nUpdated Variant Collection")


print("New Variant:", user_variant.name, "\nAlias:", user_variant.alias, "\nEarth:", user_variant.earth, "\nHealth:", user_variant.health)

