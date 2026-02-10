#Pt. 1
#8.3
def make_shirt(size, msg):
    print(f"The shirt size is {size} and it will print: '{msg}'")
make_shirt("Medium","hi")
make_shirt(size="Large", msg="hello")
#8.4
def make_shirt(size="Large", message="I love Python"):
    print(f"The shirt size is {size} and it will print: '{message}'")
make_shirt()
make_shirt(size="Medium")
make_shirt(size="Small", message="hi")
#8.5
def describe_city(city, country="United States"):
    print(f"{city} is in {country}.")
describe_city("Anderson")
describe_city("Fredericksburg")
describe_city("Reykjavik", "Iceland")
#8.6
def city_country(city, country):
    print(f"{city}, {country}")
city_country("Anderson", "United States")
city_country("Fredericksburg", "United States")
city_country("London", "England")
#8.7
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs != None:
        album["songs"] = songs
    return album
album1 = make_album("Travis Scott", "Rodeo")
album2 = make_album("Tame Impala", "Currents")
album3 = make_album("The Neighbourhood", "Ultrasound", 15)
print(album1)
print(album2)
print(album3)
#8.8
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs != None:
        album["songs"] = songs
    return album
while True:
    print("Enter album information (type 'quit' to stop).")
    artist = input("Artist name: ")
    if artist == "quit":
        break
    title = input("Album title: ")
    if title == "quit":
        break
    songs = input("Number of songs (press Enter to skip): ")
    if songs:
        album = make_album(artist, title, int(songs))
    else:
        album = make_album(artist, title)
    print(album)
#8.9
def show_messages(messages):
    for message in messages:
        print(message)
messages = [
    "wassup cuh",
    "yo yo yo",
    "it's waltuh whyte"
]
show_messages(messages)
#8.10
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
messages = [
    "wassup cuh",
    "yo yo yo",
    "it's waltuh whyte"
]
sent_messages = []
send_messages(messages, sent_messages)
print("Original messages list:", messages)
print("Sent messages list:", sent_messages)
#8.11
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
messages = [
    "wassup cuh",
    "yo yo yo",
    "it's waltuh whyte"
]
sent_messages = []
send_messages(messages[:], sent_messages)
print("Original messages list:", messages)
print("Sent messages list:", sent_messages)
#8.12
def make_sandwich(*items):
    print("Making a sandwich with:")
    for item in items:
        print(f"- {item}")
make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "bacon", "tomato", "mayo")
make_sandwich("peanut butter", "jelly")
#8.13
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
user_profile = build_profile("Landon","Donahoe",location="VA/SC",school="Anderson",major="Cyber/Crim.Jus.")
print(user_profile)
#8.14
def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info
car_profile = make_car("Nissan","Altima 2023 SV",color="Matte Black",heated_seats="True")
print(car_profile)
#8.15
#8.16
import single_function
single_function.single("True")
from single_function import single
single("False")
from single_function import single as sin
sin("True")
import single_function as sin
sin.single("False")
from single_function import *
single("True")
#8.17
#Done
#Pt. 2
import easygui as eg
eg.msgbox("Welcome to the Study Planner App!")
start = eg.ynbox("Do you want to create a study plan?")
if not start:
    eg.msgbox("Goodbye!")
    quit()
name = eg.enterbox("Enter your name:")
password = eg.passwordbox("Create a password for your plan:")
subject = eg.choicebox(
    "Choose a subject to study:",
    choices=["Math", "Science", "English", "History", "Computer Science"]
)
topics = eg.multchoicebox(
    "Select topics you want to study:",
    choices=["Homework", "Test Review", "Projects", "Reading", "Practice Problems"]
)
plan_type = eg.buttonbox(
    "Pick your study plan type:",
    choices=["Daily", "Weekly", "Monthly"]
)
notes = eg.textbox("Write your study notes here:")
open_file = eg.fileopenbox("Choose a file to open:")
save_file = eg.filesavebox("Choose where to save your study plan:")
if save_file:
    with open(save_file, "w") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Subject: {subject}\n")
        f.write(f"Topics: {topics}\n")
        f.write(f"Plan Type: {plan_type}\n")
        f.write(f"Notes:\n{notes}\n")
    eg.msgbox("Study plan saved!")
folder = eg.diropenbox("Pick a folder to store extra files:")
eg.msgbox("Here is a study motivation image!", image="motivation.png")
eg.msgbox("Thank you for using the Study Planner!")
