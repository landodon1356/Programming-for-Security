#Dictionaries
#1
person = {
    "f_name": "Landon",
    "l_name": "Donahoe",
    "age": 18,
    "hometown": "Fredericksburg, VA",
    "current_city": "Anderson, SC",
    "username": "landodon1356"
}
print(person)
print(person["f_name"])
print(person["l_name"])
print(person["age"])
print(person["hometown"])
print(person["current_city"])
print(person["username"])

#2
print(f"This person's first name is {person['f_name']}, last name is {person['l_name']}, and their username is {person['username']}.")
print(f"For security reasons, we might ask them for their hometown, which is {person['hometown']}.")

#3
definitions = {
    "python": "A programming language used to write software.",
    "variable": "A name that stores a value in a program.",
    "list": "A collection of items stored in one variable.",
    "method": "A function that belongs to an object.",
    "if statement": "A statement that runs code if a condition is true.",
    "dictionary": "A collection of key-value pairs.",
    "function": "A block of reusable code that performs a task."
}
for word, meaning in definitions.items():
    print(f"{word}: {meaning}\n")

#4 (See above)
#5
sc_county_seats = {
    "Abbeville": "Abbeville",
    "Aiken": "Aiken",
    "Allendale": "Allendale",
    "Anderson": "Anderson",
    "Bamberg": "Bamberg",
    "Barnwell": "Barnwell"
}

#6
sc_counties_list = [
    "Abbeville", "Aiken", "Allendale", "Anderson", "Bamberg",
    "Barnwell", "Beaufort", "Berkeley", "Calhoun", "Charleston"
]
for county in sc_counties_list:
    if county in sc_county_seats:
        print(f"{county} is in our dictionary, and the capital/seat is {sc_county_seats[county]}.")
    else:
        print(f"{county} is not in our dictionary. We will add this county shortly. Thanks!")

#7
anderson = {"Anderson": 27000, "Clemson": 18000, "Belton": 4000, "Iva": 1200, "Honea Path": 3800}
pickens = {"Pickens": 3300, "Easley": 22000, "Liberty": 3500, "Central": 5300, "Six Mile": 900}
greenville = {"Greenville": 72000, "Mauldin": 25000, "Simpsonville": 24000, "Taylors": 23000, "Greer": 37000}
spartanburg = {"Spartanburg": 38000, "Boiling Springs": 9500, "Duncan": 3400, "Lyman": 6200, "Wellford": 2600}
oconee = {"Walhalla": 4300, "Seneca": 8700, "Westminster": 2500, "Salem": 1300, "Mountain Rest": 900}
county_dict_list = [anderson, pickens, greenville, spartanburg, oconee]
for county in county_dict_list:
    for city, population in county.items():
        print(f"In {city.title()}, the current population is {population}.")

#8
sc_counties = {
    "Anderson": ["Anderson", "Clemson", "Belton"],
    "Pickens": ["Easley", "Central", "Pickens"],
    "Greenville": ["Greenville", "Greer", "Mauldin"],
    "Spartanburg": ["Spartanburg", "Boiling Springs", "Greer"],
    "Oconee": ["Seneca", "Walhalla", "Westminster"]
}
for county, cities in sc_counties.items():
    print(f"In {county}, the largest cities are {cities[0]}, {cities[1]}, and {cities[2]}.")

#User Input
#1
def welcome():
    name = input("What is your name?: ")
    print(f"Hello {name}, and welcome to Anderson University!")
welcome()

#2
processor = {"i3": 120, "i5": 130, "i7": 330, "i9": 420}
money = int(input("How much money you got cuh?(Just the number no $ please): "))
i = 0
affordable = ""
for proc, price in processor.items():
    if money >= price:
        affordable = proc
        i+=1
if i > 0:
    print(f"Congrats twin! You can afford the {affordable} processor!")
else:
    print(f"You're broke twin! Get more money before buying a processor!")

#3
run = 0
while run == 0:
    num = int(input("Enter a number: "))
    if num %2 ==0:
        print("This integer is even.")
    else:
        print("This integer is odd.")
    if input("To leave, say 'guess'. Otherwise, say anything else.: ") == 'guess':
        run = 1
print("aw shucks :(")

#4
run = 0
while run < 5:
    thing = input("Type something (or type 'quit' to stop): ")
    if thing == "quit":
        print("You quit the program.")
        break
    print(f"You typed: '{thing}'")
    run += 1
if run == 5:
    print("Loop ended.")

#5
valid_flavors = [
    "Ubuntu", "Kubuntu", "Lubuntu", "Xubuntu", "Ubuntu MATE",
    "Ubuntu Budgie", "Ubuntu Studio", "Ubuntu Kylin"
]
poll = {}
while True:
    username = input("Enter your username (or type 'quit' to stop): ")
    if username == "quit":
        break
    flavor = input("Enter your favorite Ubuntu flavour: ")
    if flavor in valid_flavors:
        poll[username] = flavor
    else:
        print("That is not a legitimate Ubuntu flavour.")
        print(f"Valid options are: {", ".join(valid_flavors)}.")
for item in poll:
    print(poll[item])