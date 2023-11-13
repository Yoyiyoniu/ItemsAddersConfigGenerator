import isItem


def takeForCreate():
    itemType = input(
        "Que crearemos hoy?\n1. Normal\n2. Sword\n3. Pickaxe\n4. Axe\n5. Shovel\n6. Hoe\n7. Dagger\n")

    display_name = input("Display Name: ")
    material = input("Material: ")
    model_path = input("Model Path: ")

    if itemType == "1":
        custom_durability = input("Custom Durability: ")
        attack_damage = input("Attack Damage: ")
        attack_speed = input("Attack Speed: ")
        item = isItem.BaseItem.__init__(display_name, material, model_path, custom_durability, attack_damage,
                                        attack_speed)
    elif itemType == "2":
        item = isItem.Sword(display_name, material, model_path)
    elif itemType == "3":
        item = isItem.Pickaxe(display_name, material, model_path)
    elif itemType == "4":
        item = isItem.Axe(display_name, material, model_path)
    elif itemType == "5":
        item = isItem.Shovel(display_name, material, model_path)
    elif itemType == "6":
        item = isItem.Hoe(display_name, material, model_path)
    elif itemType == "7":
        item = isItem.Dagger(display_name, material, model_path)
    else:
        print("Proseso cancelado.")
        return None

    print(f"Creating {itemType.lower()}...")
    return item.get_item_data()


print(takeForCreate())
