# JSON example
import json

x = {
    "name":"John",
    "age": 33,
    "city":"London",
    "car":[
        {"model":"Fiat"}
    ]
}
# convert into JSON
y = json.dumps(x)

print(y)
