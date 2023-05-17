bikes = ["yamaha", "honda", "suzuki", "kawasaki"]

for bike in bikes:
    if bike == 'honda':
        print(bike.upper())
    else:
        print(bike.title())


# equality is case-sensitive
for bike in bikes:
    if bike == 'Honda':
        print(bike.upper())
    else:
        print(bike.title())

for bike in bikes:
    if bike.title() == 'Honda':
        print(bike.upper())
    else:
        print(bike.title())

print("\n")
bike = "kawasaki"
print("Is bike == 'kawasaki'? I predict True.")
print(bike == "kawasaki")

print("Is bike == 'honda'? I predict False.")
print(bike == "honda")

print(1 == 1) # true
print(1 <= 4) # true
print("kawasaki" == "kawasaki") # true
print("Kawasaki" == "kawasaki") # false
print("Honda" == "kawasaki") # false
print("Honda" == "Honda") # true
print("Honda".lower() == "honda") # true
print(1 != 10) # true
print("honda" == "suzuki") # false
print("400cc is a great idea" != 1) # true

print("-----------------")
print(1 in list([value for value in range(1, 10)])) # true
print(1000 in list([value for value in range(1, 10)])) # true
print(1000 not in list([value for value in range(1, 10)])) # true
