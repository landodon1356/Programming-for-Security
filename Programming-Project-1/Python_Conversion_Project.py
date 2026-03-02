"""
This program will be a conversion program, using gui to convert most measurements, including length, volume, temperature, and weight.
"""
import easygui
#These dictionaries convert all units to the base unit
LENGTH_TO_M = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1.0,
    "km": 1000.0,
    "in": 0.025,
    "ft": 0.305,
    "yd": 0.914,
    "mi": 1609.344,
}

WEIGHT_TO_KG = {
    "g": 0.001,
    "kg": 1.0,
    "oz": 0.028,
    "lb": 0.454,
}

VOLUME_TO_L = {
    "ml": 0.001,
    "l": 1.0,
    "tsp": 0.005,
    "tbsp": 0.015,
    "fl oz": 0.03,
    "cup": 0.237,
    "pt": 0.473,
    "qt": 0.946,
    "gal": 3.785,
}
#These dictionaries divide the units into their respective categories
METRIC_UNITS = {
    "Length": ["mm", "cm", "m", "km"],
    "Weight": ["g", "kg"],
    "Volume": ["ml", "l"],
    "Temperature": ["C", "K"],
}

IMPERIAL_UNITS = {
    "Length": ["in", "ft", "yd", "mi"],
    "Weight": ["oz", "lb"],
    "Volume": ["tsp", "tbsp", "fl oz", "cup", "pt", "qt", "gal"],
    "Temperature": ["F"],
}

def convert_general(value, from_u, to_u, table):
    #This line converts the value into the base unit
    base = value * table[from_u]
    #This line converts from the base unit
    return base / table[to_u]

def convert_temperature(value, from_u, to_u):
    #convert to Celsius
    if from_u == "F":
        value = (value - 32) * 5/9
    elif from_u == "K":
        value = value - 273.15
    #convert from Celsius to target
    if to_u == "F":
        return value * 9/5 + 32
    elif to_u == "K":
        return value + 273.15
    elif to_u == "C":
        return value

def format_number(x):
    return round(x, 3)

measure_type = easygui.choicebox(
    "Choose measurement type:",
    "Unit Converter",
    ["Volume", "Length", "Weight", "Temperature"]
)

if not measure_type:
    quit()
    
direction = easygui.choicebox(
    "Choose conversion direction:",
    "Unit Converter",
    ["Metric to Imperial", "Imperial to Metric"]
)

if not direction:
    quit()
    
if direction == "Metric to Imperial":
    from_units = METRIC_UNITS[measure_type]
    to_units = IMPERIAL_UNITS[measure_type]
else:
    from_units = IMPERIAL_UNITS[measure_type]
    to_units = METRIC_UNITS[measure_type]

from_unit = easygui.choicebox(
    "Choose the unit you are using:",
    "Unit Converter",
    from_units
)

if not from_unit:
    quit()
#This while loop ensures that the user inputs a valid number
while True:
    amount_str = easygui.enterbox("Enter the amount:")
    if amount_str == None:
        quit()
    try:
        amount = float(amount_str)
        break
    except:
        easygui.msgbox("Invalid number. Try again.")

to_unit = easygui.choicebox(
    "Choose the unit to convert to:",
    "Unit Converter",
    to_units
)

if not to_unit:
    quit()
#These lines use the functions defined above to convert the units
if measure_type == "Length":
    result = convert_general(amount, from_unit, to_unit, LENGTH_TO_M)
elif measure_type == "Weight":
    result = convert_general(amount, from_unit, to_unit, WEIGHT_TO_KG)
elif measure_type == "Volume":
    result = convert_general(amount, from_unit, to_unit, VOLUME_TO_L)
elif measure_type == "Temperature":
    result = convert_temperature(amount, from_unit, to_unit)
#This line outputs the final conversion
easygui.msgbox(
    f"{format_number(amount)} {from_unit} = {format_number(result)} {to_unit}",
    "Result"
)
