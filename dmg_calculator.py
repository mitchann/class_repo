import random  

def calc_dmg(base_damage: int, armor: int, pierce: int) -> int:
    adjusted_armor = max(armor - pierce, 0)
    adjusted_dmg = max(base_damage - adjusted_armor, 0)
    return adjusted_dmg
pierce = random.randint(0, 10)
base_damage = random.randint(0, 20)
armor = int(input("Armor: "))

x = calc_dmg(base_damage, armor, pierce)
print(f"you received {x} points of damage!")