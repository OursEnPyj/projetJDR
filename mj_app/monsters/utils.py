import random


def generate_monster():
    names = ["Gobelin", "Orc", "Dragonnet", "Spectre", "Loup géant"]
    types = ["Humanoïde", "Bête", "Mort-vivant", "Dragon"]


    return {
        "name": random.choice(names),
        "type": random.choice(types),
        "hit_points": random.randint(5, 100),
        "armor_class": random.randint(8, 20),
        "strength": random.randint(3, 18),
        "dexterity": random.randint(3, 18),
        "constitution": random.randint(3, 18),
        "intelligence": random.randint(3, 18),
        "wisdom": random.randint(3, 18),
        "charisma": random.randint(3, 18),
        "description": "Une créature générée aléatoirement."
}