# This is a program to store new vehicle inventory and assist with monthly payments
#Made by Landon Donahoe
# Create variable of your favorite car brand (e.g., brand = ‘RAM’)
brand = "BMW"
# Create list of 5 of their models from cheapest to most expensive
bmw_models = ["2 Series","3 Series","4 Series","5 Series","7 Series"]
# Append a 6th model to the list
bmw_models.append("i7")
# Create list of 5 standard colors for all models
bmw_colors = ["Alpine White","Black Sapphire Metallic","Mineral White Metallic","Carbon Black Metallic","Phytonic Blue"]
# Replace your last color with a different color
bmw_colors[-1] = "Red"
# Create variable of the current year (e.g., YEAR = ‘2026’)
YEAR = "2026"
# Create MSRP constant number (not string) of each of the models (e.g., MSRP_1500Truck = 33000)
MSRP_2Series,MSRP_3Series,MSRP_4Series,MSRP_5Series,MSRP_7Series,MSRP_i7=40000,48000,53000,60500,99300,105700
# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans (e.g., fouryr = 48, sixyr = 72)
FOURYR,FIVEYR,SIXYR=48,60,72
# Create a variable for the guest's name. Be courteous in your upcoming messages :)
guest = "Walter White"
# Create message variable (with f-string) welcoming customer to your new car store
msg = f"Welcome to the BMW store, {guest}!"
# Create awesome banner with your brand/name/dealership, however you want to welcome customers
dealership = "Century BMW"
name = "Landon Donahoe"
banner = f"""
Welcome to {dealership}
Official {brand} Dealership
Sales Consultant: {name}
"""
# Print awesome banner and welcome message
print(f"{banner}\n{msg}\n")
# Using title methods, print the vehicles in alphabetical order, with the year and available colors.
print(f"We have plenty of {YEAR} models to choose from:")
bmw_models.sort()
for model in bmw_models:
    print(model)
print("\nAvailable colors:")
for color in bmw_colors:
    print(color)
# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle. Do not let more than two decimals to occur.
five_2Series = round(MSRP_2Series / FIVEYR, 2)
# and print that in a nice, kind message. Don't be rude/pushy to the customer :)
print(f"\nThe 2 Series is very cheap, with a monthly payment of only ${five_2Series} for 5 years.")
# Do the same thing, but give them 4yr and 6yr options for the same vehicle
four_2Series = round(MSRP_2Series / FOURYR, 2)
six_2Series = round(MSRP_2Series / SIXYR, 2)
print(f"For a 4 year plan, a monthly payment would be about ${four_2Series}.")
print(f"For a 6 year plan, a monthly payment would be just ${six_2Series}.")
#NEW FUNCTION
THREEYR = 36
three_2Series = round(MSRP_2Series / THREEYR, 2)
print(f"For a 3 year plan, a monthly payment would be just ${three_2Series}.\n")
#NEW FUNCTION
cash_discount_rate = 0.05
cash_price_2Series = round(MSRP_2Series * (1 - cash_discount_rate), 2)
print(f"Paying all cash? You could get the 2 Series for only ${cash_price_2Series} (5% off)!")
#NEW FUNCTION
accessory = "Sunroof"
accessory_price = 1800
print(f"\nAdd a {accessory} to your 2 Series for just ${accessory_price}!\n")
# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested
print(f"Here are 5-year monthly payments for our other models:")

print(f"3 Series: ${round(MSRP_3Series / FIVEYR, 2)} per month")
print(f"4 Series: ${round(MSRP_4Series / FIVEYR, 2)} per month")
print(f"5 Series: ${round(MSRP_5Series / FIVEYR, 2)} per month")
print(f"7 Series: ${round(MSRP_7Series / FIVEYR, 2)} per month")
print(f"i7: ${round(MSRP_i7 / FIVEYR, 2)} per month")
