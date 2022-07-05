print("********** WELCOME TO MY BATTLEGAME. GOOD LUCK! **********")

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


# #TASK 2
# print("1-Wizard")
# print("2-Elf")
# print("3-Human")
# print("4-Dragon")

# character = input("Choose your character:").lower()

# TASK 3

while True:
    print("1.) Wizard")
    print("2.) Elf")
    print("3.) Human")

    character = input("Choose your character:").lower()

    if character == "1" or character == "Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print("Unknown character")
        break

print("----")
print("You've chosen the character:", character,"with damage:", my_damage, "and horse power of:", my_hp)
print("----")

while True:
    dragon_hp = dragon_hp - my_damage
    print("The", character, "damaged the Dragon")
    print("The Dragon hits point are now", dragon_hp)
    print("----")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    my_hp = my_hp - dragon_damage
    print("Your", character, "HP is now", my_hp, "because the Dragon hit you")

    if my_hp <= 0:
        print("The", character, "lost the battle")
        break
    print("----")    
             
  
