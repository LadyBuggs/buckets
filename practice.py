import json

# arr = 'Main:Spend-40'
# print(arr)
# if open('userFile.json') != True:
#     d= {'Main':{}}
# # ':' separates the Main categories, while - separates the subcategories
# (key, val) = arr.split(':')
# (tempKey, tempVal) = val.split('-')
# d[str(key)] = {tempKey:int(tempVal)}


# print(d)
# print('New List')
# d['Main'].update(Saving = 30)
# print (d)
# with open('userFile.json', 'w+') as f:
#     f.write(json.dumps(d))
# f.close
def readFile():
    with open('userFile.json', 'r') as f:
        d =  json.loads(f)
        return d
    f.close

def createCatDict(cat, percent):
    d = readFile()
    val = {cat : int(percent)}
    d['Main'].update(val)
    with open('userFile.json', 'w+') as f:
        f.write(json.dumps(d))
    f.close()

def createSubCatDict(cat, sub, percent):
    val = {sub : int(percent)}
    val = {cat:val}
    d.update(val)
    with open('userFile.json', 'w+') as f:
        f.write(json.dumps(d))
    f.close

# print('Checking Function')
# createCatDict('Invest', 20)
# createSubCatDict('Spend','Bills', 9)
# print(d)
