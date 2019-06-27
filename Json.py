
#working with json
import json


x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y["age"])
print(x)


#convert data from python to json
data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

convert = json.dumps(data,indent=4)
print(convert)