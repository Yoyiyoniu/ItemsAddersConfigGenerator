class BaseItem:
    def __init__(self, display_name: str, material: str, model_path: str, attack_damage: float, attack_speed: float,
                 custom_durability: int):
        self.item_data = {
            'display_name': display_name,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': material,
                'model_path': model_path
            },
            'durability': {
                'custom_durability': custom_durability
            },
            "attribute_modifiers": {
                'mainhand': {
                    'attackDamage': attack_damage,
                    'attackSpeed': attack_speed
                }
            }
        }

    def get_item_data(self):
        return self.item_data


class Sword(BaseItem):
    def __init__(self, display_name: str, material: str, model_path: str):
        super().__init__(display_name, material, model_path, 12, 1.6, 2234)


class Axe(BaseItem):
    def __init__(self, display_name: str, material: str, model_path: str):
        super().__init__(display_name, material, model_path, 14, 1, 2234)


class Pickaxe(BaseItem):
    def __init__(self, display_name: str, material: str, model_path: str):
        super().__init__(display_name, material, model_path, 10, 1.2, 2234)


class Shovel(BaseItem):
    def __init__(self, display_name: str, material: str, model_path: str):
        super().__init__(display_name, material, model_path, 9, 1, 2234)


class Hoe(BaseItem):
    def __init__(self, display_name: str, material: str, model_path: str):
        super().__init__(display_name, material, model_path, 2, 4, 2234)


class Dagger(BaseItem):
    def __init__(self, display_name: str, material: str, model_path: str):
        super().__init__(display_name, material, model_path, 2, 4, 2234)