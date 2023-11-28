car = {"model":"m1 ","color":"red","price":100}
# print(car.get('model'))
print(car.keys())

# for i in car:
#     for j in car.values:
#       print(i,j)

# for i in car.values():
#     print(i)

for i,j in car.items():
    print(i,j)

cars = {"car1":{"model":"m1 ","color":"red","price":100},
        "car2":{"model":"m2 ","color":"blue","price":1000}}

for i,j in cars.items():
    for k in j.items():
       print(i,k)
