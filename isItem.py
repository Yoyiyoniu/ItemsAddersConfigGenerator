class CreateItem:
    def defaultItem(DisplayName: str, MATERIAL: str, ModelPath: str, custom_durability: int, AttackDamage: float,
                    AttackSpeed: float):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'durability': {
                'custom_durability': custom_durability
            },
            "attribute_modifiers": {
                'mainhand': {
                    'attackDamage': AttackDamage,
                    'attackSpeed': AttackSpeed
                }
            }

        }

    def isSword(DisplayName: str, MATERIAL: str, ModelPath: str):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'attribute_modifiers': {
                'mainhand': {
                    'attackDamage': 12,
                    'attackSpeed': 1.6
                }
            },
            'durability': {
                'custom_durability': 2234
            }
        }

    def isAxe(DisplayName: str, MATERIAL: str, ModelPath: str):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'attribute_modifiers': {
                'mainhand': {
                    'attackDamage': 14,
                    'attackSpeed': 1
                }
            },
            'durability': {
                'custom_durability': 2234
            }
        }

    def isPicaxe(DisplayName: str, MATERIAL: str, ModelPath: str):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'attribute_modifiers': {
                'mainhand': {
                    'attackDamage': 10,
                    'attackSpeed': 1.2
                }
            },
            'durability': {
                'custom_durability': 2234
            }
        }

    def isShovel(DisplayName: str, MATERIAL: str, ModelPath: str):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'attribute_modifiers': {
                'mainhand': {
                    'attackDamage': 9,
                    'attackSpeed': 1
                }
            },
            'durability': {
                'custom_durability': 2234
            }
        }

    def isHoe (DisplayName: str, MATERIAL: str, ModelPath: str):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'attribute_modifiers': {
                'mainhand': {
                    'attackDamage': 2,
                    'attackSpeed': 4
                }
            },
            'durability': {
                'custom_durability': 2234
            }
        }

    def isDagger(DisplayName: str, MATERIAL: str, ModelPath: str):
        return {
            'display_name': DisplayName,
            'permission': 'prm',
            'resource': {
                'generate': False,
                'material': MATERIAL,
                'model_path': ModelPath
            },
            'attribute_modifiers': {
                'mainhand': {
                    'attackDamage': 2,
                    'attackSpeed': 4
                }
            },
            'durability': {
                'custom_durability': 2234
            }
        }