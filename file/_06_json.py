""" JavaScript Object Notation """

import json


people_json = '''
{
  "people": [
    {
      "name": "Mr. Ant",
      "phone": "123456",
      "has_license": false
    },
    {
      "name": "Mr. Pant",
      "phone": "654321",
      "has_license": true
    }
  ]
}
'''

# Conversion in json to python dict
data = json.loads(people_json)
print("Type is:", type(data))
print(data)

# Person name
for person in data['people']:
    print(person['name'])


# Deleting Phone number
for person in data['people']:
    del person['phone']

new_json = json.dumps(data, indent=2)
print(new_json)
