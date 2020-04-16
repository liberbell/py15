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

# with open("data_file/currency.json", "w") as json_file:
#     json_file.write(json_var)

written_data = json.load(open("data_file/currency.json"))
print(written_data)

dessert = {"Name": "Ice cream",
"Flavors": ["Chocolate", "Pineapple"],
"Topping": True,
"WaffleCone": "Yes"
}

# dessert_str = json.dumps(dessert)
# print(dessert_str)
# print(type(dessert_str))

# with open("data_file/eat.txt", "w") as json_file:
#     json.dump(dessert, json_file)

print(dessert)

print(json.dumps(dessert, indent=2))
print(json.dumps(dessert, separators=(":", "=")))