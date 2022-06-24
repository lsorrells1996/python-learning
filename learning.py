import json
# first_num = float(input("First: "))
# second_num = float(input("Second: "))

# total = first_num + second_num

# print("Sum: " + str(total))

# temperature = int(input("What is the current tempurature? "))

# if temperature >= 80:
#     print('It\'s a hot day!')
# elif temperature >= 65:
#     print("It's a lovely day, go outside!")
# else:
#     print("It's a bit nippy, wear a jacket :)")

# print("Done")


# weight = float(input("Weight: "))
# thing = input("(K)g or (L)bs: ")

# if thing.capitalize() == "K":
#     weight_in_kg = weight * 2.2
#     print("Weight in Lbs: " + str(weight_in_kg))
# elif thing.capitalize() == "L":
#     weight_in_lbs = weight / 2.2
#     print("Weight in Kg: " + str(weight_in_lbs))
# else:
#     print("Invalid response, please enter either K or L")
# print("Done")

# for i in range(5):
#     print(i)

dude = []

for i in range(5):
    dude.append(i)


x = {
    "Numbers": dude
}

print(x)
y = json.dumps(x)
print(y)