motorbikes = ["yamaha", "aprilia", "triumph", "suzuki", "ktm", "bmw"]

for bike in motorbikes:
    print(bike)

# for num in range(1,21):
#     print(num)

# for num in range(1, 1_000_001):
#     print(num)

oneMillion = list(range(1, 1_000_001))

print(max(oneMillion))
print(min(oneMillion))

oneMillion = sum([value for value in range(1,1_000_001)])
print(oneMillion)

odds = [val for val in range(1, 21, 2)]
print(odds)

# other way to print:
for num in odds:
    print(num)

threes = [three*3 for three in range(1, 11)]
print(threes)

cubes = [cubes**3 for cubes in range(1, 11)]
print(cubes)