import tkinter as tk
from tkinter import ttk

# Function to handle unit conversions
def convert_units():
    conversion_type = conversion_type_var.get()
    unit1 = unit1_var.get()
    unit2 = unit2_var.get()
    try:
        num1 = float(entry_value.get())
    except ValueError:
        result_var.set("Invalid input")
        return

    # Define conversion dictionaries for each type
    conversions = {
        "Length": {
            ("cm", "m"): lambda x: x / 100,
            ("mm", "cm"): lambda x: x / 10,
            ("m", "cm"): lambda x: x * 100,
            ("cm", "mm"): lambda x: x * 10,
            ("mm", "m"): lambda x: x / 1000,
            ("m", "mm"): lambda x: x * 1000,
            ("km", "m"): lambda x: x * 1000,
            ("m", "km"): lambda x: x / 1000,
            ("mm", "km"): lambda x: x / 1000000,
            ("m", "ft"): lambda x: x * 3.28084,
            ("ft", "m"): lambda x: x / 3.28084,
            ("m", "inch"): lambda x: x * 39.3701,
            ("inch", "m"): lambda x: x / 39.3701,
        },
        "Mass": {
            ("cg", "g"): lambda x: x / 100,
            ("mg", "cg"): lambda x: x / 10,
            ("g", "cg"): lambda x: x * 100,
            ("cg", "mg"): lambda x: x * 10,
            ("mg", "g"): lambda x: x / 1000,
            ("g", "mg"): lambda x: x * 1000,
            ("kg", "g"): lambda x: x * 1000,
            ("g", "kg"): lambda x: x / 1000,
            ("mg", "kg"): lambda x: x / 1000000,
            ("g", "oz"): lambda x: x * 0.035,
            ("oz", "g"): lambda x: x / 0.035,
            ("lb", "kg"): lambda x: x * 0.454,
            ("t", "kg"): lambda x: x * 907.185,
        },
        "Capacity": {
            ("cL", "L"): lambda x: x / 100,
            ("mL", "cL"): lambda x: x / 10,
            ("L", "cL"): lambda x: x * 100,
            ("cL", "mL"): lambda x: x * 10,
            ("mL", "L"): lambda x: x / 1000,
            ("L", "mL"): lambda x: x * 1000,
            ("kL", "L"): lambda x: x * 1000,
            ("L", "kL"): lambda x: x / 1000,
            ("mL", "kL"): lambda x: x / 1000000,
        },
        "Temperature": {
            ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
            ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
            ("Celsius", "Kelvin"): lambda x: x + 273.15,
            ("Kelvin", "Celsius"): lambda x: x - 273.15,
            ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
            ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        },
        "Pressure": {
            ("atm", "Pa"): lambda x: x * 101325,
            ("Pa", "atm"): lambda x: x / 101325,
            ("psi", "Pa"): lambda x: x * 6894.76,
            ("Pa", "psi"): lambda x: x / 6894.76,
            ("kPa", "Pa"): lambda x: x * 1000,
            ("Pa", "kPa"): lambda x: x / 1000,
            ("mbar", "Pa"): lambda x: x * 100,
            ("Pa", "mbar"): lambda x: x / 100,
            ("mmHg", "Pa"): lambda x: x * 133.322,
            ("Pa", "mmHg"): lambda x: x / 133.322,
        },
        "Energy": {
            ("Joule", "Calorie"): lambda x: x * 0.239005736,
            ("Calorie", "Joule"): lambda x: x / 0.239005736,
            ("Joule", "kWh"): lambda x: x / 3600000,
            ("kWh", "Joule"): lambda x: x * 3600000,
            ("Calorie", "kWh"): lambda x: x * 0.00116222,
            ("kWh", "Calorie"): lambda x: x / 0.00116222,
        },
        "Volume": {
            ("cubic meter", "liter"): lambda x: x * 1000,
            ("liter", "cubic meter"): lambda x: x / 1000,
            ("gallon", "liter"): lambda x: x * 3.78541,
            ("liter", "gallon"): lambda x: x / 3.78541,
            ("cubic inch", "cubic meter"): lambda x: x / 61023.7,
            ("cubic meter", "cubic inch"): lambda x: x * 61023.7,
            ("cubic foot", "cubic meter"): lambda x: x / 35.3147,
            ("cubic meter", "cubic foot"): lambda x: x * 35.3147,
            ("cubic centimeter", "cubic meter"): lambda x: x / 1000000,
            ("cubic meter", "cubic centimeter"): lambda x: x * 1000000,
        },
    }

    if (unit1, unit2) in conversions[conversion_type]:
        conversion_function = conversions[conversion_type][(unit1, unit2)]
        result = conversion_function(num1)
        result_var.set(f"{num1} {unit1} = {result:.4f} {unit2}")
    else:
        result_var.set("Invalid unit conversion")

# Initialize main window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("550x300")
root.resizable(False, False)

# Title label
title_label = ttk.Label(root, text="PetroConvert", font=("Arial", 30))
title_label.grid(column=0, row=0, columnspan=4, pady=20)

# Conversion type options
conversion_types = ["Length", "Mass", "Capacity", "Temperature", "Pressure", "Energy", "Volume"]
conversion_type_var = tk.StringVar(value=conversion_types[0])

# Labels
ttk.Label(root, text="Conversion Type:", font=("Arial", 12)).grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
ttk.Label(root, text="Convert From:", font=("Arial", 12)).grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
ttk.Label(root, text="Convert To:", font=("Arial", 12)).grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
ttk.Label(root, text="Value:", font=("Arial", 12)).grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)
ttk.Label(root, text="Result:", font=("Arial", 12)).grid(column=3, row=2, padx=10, pady=10, sticky=tk.W)

# Dropdown for conversion type
conversion_type_dropdown = ttk.OptionMenu(root, conversion_type_var, conversion_types[0], *conversion_types)
conversion_type_dropdown.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

# Variables for units and value
unit1_var = tk.StringVar()
unit2_var = tk.StringVar()
entry_value = tk.Entry(root, width=10, font=("Arial", 12))

# Dropdowns for unit selection
unit1_dropdown = ttk.OptionMenu(root, unit1_var, "")
unit2_dropdown = ttk.OptionMenu(root, unit2_var, "")
unit1_dropdown.grid(column=0, row=3, padx=10, pady=10)
unit2_dropdown.grid(column=1, row=3, padx=10, pady=10)

# Entry for value input
entry_value.grid(column=2, row=3, padx=10, pady=10)

# Label for displaying result
result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, font=("Arial", 12))
result_label.grid(column=3, row=3, padx=10, pady=10)

# Convert button
convert_button = ttk.Button(root, text="Convert", command=convert_units)
convert_button.grid(column=2, row=4, padx=10, pady=20)

# Function to update unit options based on conversion type
def update_units(*args):
    conversion_type = conversion_type_var.get()
    unit_options = {
        "Length": ["cm", "m", "mm", "km", "ft", "inch"],
        "Mass": ["cg", "g", "mg", "kg", "oz", "lb", "t"],
        "Capacity": ["cL", "L", "mL", "kL"],
        "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
        "Pressure": ["atm", "Pa", "psi", "kPa", "mbar", "mmHg"],
        "Energy": ["Joule", "Calorie", "kWh"],
        "Volume": ["cubic meter", "liter", "gallon", "cubic inch", "cubic foot", "cubic centimeter"]
    }
    unit1_var.set(unit_options[conversion_type][0])
    unit2_var.set(unit_options[conversion_type][1])
    unit1_dropdown["menu"].delete(0, "end")
    unit2_dropdown["menu"].delete(0, "end")
    for option in unit_options[conversion_type]:
        unit1_dropdown["menu"].add_command(label=option, command=tk._setit(unit1_var, option))
        unit2_dropdown["menu"].add_command(label=option, command=tk._setit(unit2_var, option))

# Bind the update_units function to the conversion type dropdown
conversion_type_var.trace("w", update_units)

# Initial call to update units
update_units()

# Start the GUI event loop
root.mainloop()