import json

f = open('FAHRZEUGTYP_S15A_full.json')
data = json.load(f)
names1 = []
names2 = []
allnames1 = []
allnames2 = []
for i in data['FAHRZEUGTYP']:
    allnames1.append(i['NAME'])
    if i['BESCHREIBUNG'] == None:
        names1.append(i['NAME'])

m = open('S15_FAHRZEUGTYP_202506032205.json')
data2 = json.load(m)
for n in data2['FAHRZEUGTYP']:
    allnames2.append(n['NAME'])
    if n['BESCHREIBUNG'] == None:
        names2.append(n['NAME'])

print(allnames1)
print(allnames2)
pon = []
for i in allnames1:
    if i not in allnames2:
        pon.append(i)
print(pon)
print('--------------------')
print(names1)
print(names2)
print('--------------------')
gotov = []
besh = []
for i in names1:
    if i not in names2:
        gotov.append(i)
list1 = data2['FAHRZEUGTYP']
for n in gotov:
    for i in list1:
        if n == i['NAME']:
            besh.append(i['BESCHREIBUNG'])
print(besh)
print(gotov)

for h in data['FAHRZEUGTYP']:
    if h['NAME'] in gotov:
        b = gotov.index(h['NAME'])
        h['BESCHREIBUNG'] = besh[b]

with open('FAHRZEUGTYP_S15A_full_edit.json', "w") as outfile:
    json.dump(data, outfile)

f.close()
m.close()
