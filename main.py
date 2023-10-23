import yaml
from isItem import CreateItem
with open('utils/ymlTemplate.yml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

info = {
    'namespace': 'Cambiame'
}
items = {
    'items': {
        'item1': CreateItem.isSword('DispalayName', 'ModelPath', 'Material'),
        'item2': CreateItem.isAxe('DispalayName2', 'ModelPath', 'Material'),
    }
}

# Actualiza los valores en 'data'
data['info'] = info
data.update(items)

# Guardar los cambios en el archivo YAML
with open('output/gen.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
print("Todo GOOD!")