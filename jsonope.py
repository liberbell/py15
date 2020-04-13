import json

car = """{ "model":"Civic",
"make":"honda",
"variants":["Sedan","Coupe"]
}"""

print(car)

car_dict = json.loads(car)
print(car_dict)
print(car_dict['variants'])