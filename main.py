import yaml

import isItem

with open('utils/ymlTemplate.yml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

total = {
    "info": {
        'namespace': 'new_items',
    },
    "items": {
        'gran_espada': isItem.Axe("Gran Espada", "NETHERITE_SWORD", "item/handheld").get_item_data(),
    }

}

# Actualiza los valores en 'data'
data['info'] = total
data.update(total)

# Guardar los cambios en el archivo YAML
with open('output/gen.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
print("Todo GOOD!")
