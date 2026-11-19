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

print("Name:", miles.name, "Alias:", miles.alias, "Earth:", miles.earth, "Health:", miles.health)
print("Name:", gwen.name, "Alias:", gwen.alias, "Earth:", gwen.earth, "Health:", gwen.health)
print("Name:", hobie.name, "Alias:", hobie.alias, "Earth:", hobie.earth, "Health:", hobie.health)



#Miles's earth and health change
miles.earth = 42
#A spider from another earth bit him, making him a "glitch"
miles.health = 200.0

print("\nMiles Morales Updated...")
print("Name:", miles.name, "Alias:", miles.alias, "Earth:", miles.earth, "Health:", miles.health)
print("Name:", gwen.name, "Alias:", gwen.alias, "Earth:", gwen.earth, "Health:", gwen.health)
print("Name:", hobie.name, "Alias:", hobie.alias, "Earth:", hobie.earth, "Health:", hobie.health)