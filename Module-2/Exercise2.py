#4.1
pizzas = ["Pepperoni","Meat Lovers","Mac n Cheese"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")
#4.2
animals = ["dog","cat","horse"]
for animal in animals:
    print(f"A {animal} would make a great pet")
print("All of these animals are mammals.")
#4.3
for i in range(1,21):
    print(i)
#4.4
for i in range(1,1000001):
    print(i)
#4.5
million = []
for i in range(1,1000001):
    million.append(i)
print(f"List min = {min(million)}\nList max = {max(million)}")
print(f"Sum of list = {sum(million)}")
#4.6
for i in range(1,21,2):
    print(i)
#4.7
threes = []
count = 0
for i in range(3,31,3):
    threes.append(i)
    print(threes[count])
    count+=1
#4.8
for i in range(1,11):
    print(i**3)
#4.9
cubes = [i**3 for i in range(1, 11)]
print(cubes)
#4.10
print(f"The first three items in the list are {str(cubes[0:3])}")
print(f"Three items from the middle of the list are {str(cubes[3:6])}")
print(f"The last three items in the list are {str(cubes[7:11])}")
#4.11
pizzas = ["Pepperoni","Meat Lovers","Mac n Cheese"]
friend_pizzas = pizzas[:]
pizzas.append("Cheese")
friend_pizzas.append("Hawaiian")
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
#4.12
my_food = ["Fish","Gummies","Mexican"]
friend_food = ["Burger","Italian","Ice Cream"]
print("My food is:")
for food in my_food:
    print(food)
print("My friend's food is:")
for food in friend_food:
    print(food)
#4.13
buffet = ("Pizza","Burgers","Tacos","Pasta","Fish")
for food in buffet:
    print(food)
#buffet[0] = "Hotdog"
buffet = ("Hotdogs","Burgers","Tacos","Cakes","Fish")
for food in buffet:
    print(food)
#5.1
object = "mouse"
print("Is object == 'mouse'? I predict True.")
print(object == "mouse")
print("Is object == 'keyboard'? I predict False.")
print(object == "keyboard")
print(object != "keyboard")
print(object == "mousepad")
print(object != "mousepad")
print(object == "plug")
print(object != "plug")
print(object == "laptop")
print(object != "laptop")
print(object == "screen")
print(object != "screen")
print(object == "usb")
#5.2
object = "Thing"
print(object == "Thing")
print(object != "Thing")
print(object == object.lower())
print(object != object.lower())
print(len(object) >= 5)
print(len(object) < 5)
print(object == "bus" or 1+1 == 2)
print(object == "bus" and 1+1 == 2)
print(type(object) == list)
print(type(object) != list)
#5.3
alien_color = "green"
if alien_color == "green":
    print("You earned 5 points")
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points")
#5.4
alien_color = "Red"
if alien_color == "Green":
    print("You have earned 5 points for shooting the alien")
else:
    print("You have earned 10 points")
alien_color = "Green"
if alien_color == "Green":
    print("You have earned 5 points for shooting the alien")
else:
    print("You have earned 10 points")
#5.5
alien_color = "Green"
if alien_color == "Green":
    print("You have earned 5 points")
elif alien_color == "Yellow":
    print("You have earned 10 points")
else:
    print("You have earned 15 points")
alien_color = "Yellow"
if alien_color == "Green":
    print("You have earned 5 points")
elif alien_color == "Yellow":
    print("You have earned 10 points")
else:
    print("You have earned 15 points")
alien_color = "Red"
if alien_color == "Green":
    print("You have earned 5 points")
elif alien_color == "Yellow":
    print("You have earned 10 points")
else:
    print("You have earned 15 points")
#5.6
age = 20
if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are an elder")
#5.7
favorite_fruits = ["Cherry","Grape","Raspberry"]
if "Cherry" in favorite_fruits:
    print("You like cherries")
if "Grape" in favorite_fruits:
    print("You like grapes")
if "Raspberry" in favorite_fruits:
    print("You like raspberries")
if "Peach" in favorite_fruits:
    print("You like peaches")
if "Strawberry" in favorite_fruits:
    print("You like strawberries")
#5.8
usernames = ["admin","user1","user2","user3","landon"]
for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again")
#5.9
usernames = []
if len(usernames) == 0:
    print("We need to find some users!")
for name in usernames:
    if name == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}, thank you for logging in again")
#5.10
current_users = ["admin","user1","user2","user3","landon"]
new_users = ["user2","user3","user4","user5","user6"]
lower_users = []
for name in current_users:
    lower_users.append(name.lower())
for name in new_users:
    if name.lower() in lower_users:
        print(f"{name} is already taken, enter a new username")
    else:
        print(f"{name} is available")
#5.11
nums = [1,2,3,4,5,6,7,8,9]
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")

#5.12
#I went through my programs and double-checked them
#5.13
#Chess, 2-player game, steganography