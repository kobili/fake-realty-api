from json import dumps as json_dumps
from models import Property

properties = {}

for i in range(0, 150):
    property = Property()
    properties[property.mls] = property.to_dict()

with open("output.json", "w") as f:
    f.write(json_dumps(properties, indent=4))
