import json

car = """{ "model":"Civic",
"make":"honda",
"variants":["Sedan","Coupe"]
}"""

print(car)

car_dict = json.loads(car)
print(car_dict)
print(car_dict['variants'])

# with open("data_file/currency.json", "r") as json_file:
#     data = json.load(json_file)
#     print(data)

currency = {"Countyry": "India", "Currency": "Rupee"}

json_var = json.dumps(currency)
print(json_var)
print(type(json_var))

with open("data_file/currency.json", "w") as json_file:
    json_file.write(json_var)

written_data = json.load("data_file/currency.json")
print(written_data)