# Header
print('---------------------------------------------------------')
print("\t\tSeries and Parallel Calculator")
print('---------------------------------------------------------')

# Function to get resistance values from the user
def get_resistance():
    resistor_list = []
    i = 0
    r = 1
    try:
        n = int(input("How many Resistors do you want to add? : "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

    while i < n:
        try:
            resistor_input = int(input(f"Enter the value of R{r}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        resistor_list.append(resistor_input)
        r += 1
        i += 1

    return resistor_list

# Function to calculate the total resistance
def r_total(r_list):
    return sum(r_list)

# Function to calculate the total current
def i_total(r_total, v_total):
    return v_total / r_total

# Function to calculate voltage drops across resistors
def v_drops(r_list, i_total):
    return [round(x * i_total, 2) for x in r_list]

# Function to display the current table
def display_current_table(resistor_list, voltage_drop_list):
    print("%-4s %s %4s %s  %1s" % ("|", "Resistance", "|", "Voltage Drop", "|"))
    print('-------------------------------------')
    for i in range(len(resistor_list)):
        print("%-8s %4.1f %8s %4.1f %8s" % ("|", resistor_list[i], "Ω |", voltage_drop_list[i], "V |"))
    print('-------------------------------------')

# Main loop
while True:
    try:
        slt = str(input("Enter if it's Parallel or Series: ")).lower()
    except ValueError:
        print("Please enter a valid input.")
        continue

    if slt != "series" and slt != "parallel":
        print("Invalid Input, Please Enter 'Parallel' or 'Series'")
    else:
        continue

    # Series Calculator
    if slt == "series":
        try:
            v_total = int(input("Total Voltage: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        print("\nInput Resistor Values:")
        r_list = get_resistance()
        if r_list is None:
            continue

        r_total_value = r_total(r_list)
        i_total_value = i_total(r_total_value, v_total)
        voltage_drop_list = v_drops(r_list, i_total_value)

        display_current_table(r_list, voltage_drop_list)

    # Parallel Calculator
    elif slt == "parallel":
        try:
            v_total = int(input("Total Voltage: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        print("\nInput Resistor Values:")
        r_list = get_resistance()
        if r_list is None:
            continue

        r_total_value = r_total(r_list)
        i_total_value = i_total(r_total_value, v_total)
        current_list = [round(v_total / x, 2) for x in r_list]

        print("%-4s %s %6s %s  %4s" % ("|", "Resistance", "|", "Current", "|"))
        print('-------------------------------------')
        for i in range(len(r_list)):
            print("%-8s %4.1f %8s %4.1f %8s" % ("|", r_list[i], "Ω |", current_list[i], "A |"))
        print('-------------------------------------')

    # Ask the user if they want to run the calculator again
    print("Do you want to run the calculator again?")
    try:
        ans = str(input(" ")).lower()
    except ValueError:
        print("Invalid Input! Please answer with yes or no.")
        continue

    if ans == "yes":
        continue
    elif ans == "no":
        break
    else:
        print("Invalid Answer! Please answer with yes or no.")
        continue
