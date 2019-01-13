import json
from urllib.request import urlopen


with urlopen("http://api.dataatwork.org/v1/spec/skills-api.json") as response:
    source = response.read()
    # print(source)

    data = json.loads(source)
    data = json.dumps(data, indent=2)
    # Print whatever you want
    print(data)
    print(data['paths']['/jobs']['get']['summary'])
    
