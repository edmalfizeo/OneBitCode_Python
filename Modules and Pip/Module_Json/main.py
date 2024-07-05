import json

# 1 - Convert String to Dictionary
person = '{"name": "John", "age": 30, "city": "New York"}'
person_dict = json.loads(person)
print(person_dict)
print(person_dict['name'])

# 2 - Convert Dictionary to Json
person_json = json.dumps(person_dict)
print(person_json)

# 3 - Convert Dictionary to Json with indent
person_json = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_json)

# 4 - Saving Json to a file Txt
with open('person.txt', 'w') as json_file:
    json.dump(person_dict, json_file)

# 5 - Reading External Json File
with open('person.txt', 'r') as json_file:
    person_dict = json.load(json_file)
    print(person_dict)
    print(person_dict['name'])
