import tkinter as tk
import random

def generate_pick_three():
    return [random.randint(0, 9) for _ in range(3)]

def generate_pick_four():
    return [random.randint(0, 9) for _ in range(4)]

def generate_powerball():
    main_numbers = [random.randint(1, 69) for _ in range(5)]
    powerball_number = random.randint(1, 26)
    return main_numbers, powerball_number

def generate_numbers():
    choice = number_choice.get()
    if choice == 1:
        numbers = generate_pick_three()
    elif choice == 2:
        numbers = generate_pick_four()
    elif choice == 3:
        main_numbers, powerball_number = generate_powerball()
        numbers = f"Main numbers: {main_numbers}\nPowerball number: {powerball_number}"
    else:
        numbers = "Invalid choice."

    result_label.config(text=numbers)

# Create the main window
root = tk.Tk()
root.title("Lottery Number Generator")

# Create a label widget
title_label = tk.Label(root, text="Choose a lottery type:")
title_label.pack(pady=10)

# Create a radio button to choose Pick Three
number_choice = tk.IntVar()
pick_three_radio = tk.Radiobutton(root, text="Pick Three", variable=number_choice, value=1)
pick_three_radio.pack(anchor=tk.W)

# Create a radio button to choose Pick Four
pick_four_radio = tk.Radiobutton(root, text="Pick Four", variable=number_choice, value=2)
pick_four_radio.pack(anchor=tk.W)

# Create a radio button to choose Powerball
powerball_radio = tk.Radiobutton(root, text="Powerball", variable=number_choice, value=3)
powerball_radio.pack(anchor=tk.W)

# Create a button widget to generate numbers
generate_button = tk.Button(root, text="Generate Numbers", command=generate_numbers)
generate_button.pack(pady=5)

# Create a label to display the generated numbers
result_label = tk.Label(root, text="", wraplength=250)
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
