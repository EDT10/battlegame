# TASK 1

wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50


# TASK 2
# print("1-Wizard")
# print("2-Elf")
# print("3-Human")
# print("4-Dragon")

# character = int(input("Choose your character:"))

# TASK 3

while True:
    print("1-Wizard")
    print("2-Elf")
    print("3-Human")
    print("4-Dragon")

    character = int(input("Choose your character:"))

    if character == 1:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == 2:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == 3:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
        break

print("You've chosen the character:", character,"with damage:", my_damage, "and horse power of:", my_hp)
