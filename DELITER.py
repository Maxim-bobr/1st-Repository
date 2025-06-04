import json

f = open('FAHRZEUGTYP_R05X_full.json')
data = json.load(f)
print(data)

for i in data['FAHRZEUGTYP']:
    besh = i['BESCHREIBUNG']
    result = besh[:besh.find('KW')]
    result = result[:result.find('kW')]
    result = result + 'KW'
    print(result)
