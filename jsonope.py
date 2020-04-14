import json

car = """{ "model":"Civic",
"make":"honda",
"variants":["Sedan","Coupe"]
}"""

print(car)

car_dict = json.loads(car)
print(car_dict)
print(car_dict['variants'])

with open("data_file/currency.json", "r") as json_file:
    data = json.load(json_file)
    print(data)

currency = {"Countyry": "India", "Currency": "Rupee"}

json_var = json.dump(currency)
print(json_var)