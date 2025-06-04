import json

f = open('FAHRZEUGTYP_R05X_full.json')
data = json.load(f)
print(data)
f.close()
for i in data['FAHRZEUGTYP']:
    besh = i['BESCHREIBUNG']
    i['BESCHREIBUNG'] = besh[:besh.find('KW')]
    result = besh[:besh.find('KW')]
    i['BESCHREIBUNG'] = result[:result.find('kW')]
    i['BESCHREIBUNG'] = i['BESCHREIBUNG'] + 'KW'

with open('FAHRZEUGTYP_R05X_full.json', "w") as outfile:
    json.dump(data, outfile)

