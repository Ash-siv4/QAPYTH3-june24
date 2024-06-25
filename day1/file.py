print("Hello World")

print(1234 + 4563)

temp = 28
rain = False

if temp < 24:
    print("brrr cold")
# elif temp >= 24 and temp <= 27:
elif 24 <= temp <= 27:
    print("Perfect!")
    # if rain == True:
    if rain:
        print("outdoor shower :)")
    else:
        print("ideal")
else:
    print("hot")

temp = 50
# check = bool(temp = 50) -> must use == not = since single equal is assignment and double equal is comparison
check = bool(temp == 50)
print(check)

num = 4
num_str = "4"
print(bool(num == num_str))

val = 0  # 9

while val < 10:
    val += 1  # val = 9+1 = 10
    print(val)

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print(number)
        break
    else:
        print("Invalid number, try again")

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if 1 <= number <= 10:
        print(number)
        break
    else:
        print("Invalid number, try again")

pets = ["dog", "cat", "hamster", "parrot"]

for pet in pets:
    print(pet)
