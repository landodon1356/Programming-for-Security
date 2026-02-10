def make_sandwich(*items):
    print("Making a sandwich with:")
    for item in items:
        print(f"- {item}")
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info
user_profile = build_profile("Landon","Donahoe",location="VA/SC",school="Anderson",major="Cyber/Crim.Jus.")
def make_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model
    return car_info
car_profile = make_car("Nissan","Altima 2023 SV",color="Matte Black",heated_seats="True")
