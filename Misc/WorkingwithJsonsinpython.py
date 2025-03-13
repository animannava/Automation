import json
from pydoc import sort_attributes
from xml.etree.ElementTree import indent

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
#print(json.dumps(x,indent=4))
print(json.dumps(x,separators=("| ", " = ")))
print(json.dumps(x,separators=("| ", " = "),sort_keys=True))