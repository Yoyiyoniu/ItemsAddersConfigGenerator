import yaml

# Cargar el archivo YAML
with open('../utils/ymlTemplate.yml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Modificar los valores
data['info']['namespace'] = 'weapons'
data['items']['azure_axe']['display_name'] = 'Super Azure Axe'
data['items']['azure_axe']['durability']['custom_durability'] = 1542
data['items']['azure_axe']['resource']['material'] = 'NETHERITE_AXE'
data['items']['azure_axe']['resource']['model_path'] = 'azure/azureset/axe'

# Guardar los cambios en el archivo YAML
with open('../output/gen.yml', 'w') as file:
    yaml.dump(data, file, default_flow_style=False)
