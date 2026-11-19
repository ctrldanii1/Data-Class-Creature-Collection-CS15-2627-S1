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


print("New Variant:", user_variant.name, "|Alias:", user_variant.alias, "|Earth:", user_variant.earth, "|Health:", user_variant.health)
print("Name:", miles.name, "|Alias:", miles.alias, "|Earth:", miles.earth, "|Health:", miles.health)
print("Name:", gwen.name, "|Alias:", gwen.alias, "|Earth:", gwen.earth, "|Health:", gwen.health)
print("Name:", hobie.name, "|Alias:", hobie.alias, "|Earth:", hobie.earth, "|Health:", hobie.health)
