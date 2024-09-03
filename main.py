import tkinter as tk
from tkinter import font as tkfont
import ttkbootstrap as tkb



######################
### VAT CALCULATOR ###
######################



### FUNCTIONS ### 

# VAT calculation function (NOW UNUSED)
def vat(net):
    rate = 0.2
    amount = net * rate
    gross = net + amount
    return gross

# # Console test
# if __name__ == "__main__":
#     net = float(input("Net amount (excluding VAT): £"))
#     gross = vat(net)
#     print(f"Gross amount (including VAT): £{gross:.2f}")
# Check for decimal

def decimal(value, max=2):
    try:
        float_value = float(value)
        str_value = f"{float_value:.{max}f}"
        _, pence = str_value.split(".")
        return len(pence) == max
    except ValueError:
        return False
    
# Add VAT function
def add_vat():
    try:
        # Retrieve and clean input
        input_value = net_entry.get().strip().replace("£", "")

        # Check for empty input
        if not input_value:
            raise ValueError("Input must not be empty.")
        
        # Check for leading zeroes
        if input_value.startswith("0") and not input_value.startswith("0."):
            raise ValueError("Remove leading zeroes.")
        
        # Check for non-number
        if not input_value.replace(".", "", 1).isdigit():
            raise ValueError("Input must be a valid number.")

        # Check for decimal
        if not decimal(input_value):
            raise ValueError("Pence must be two decimals.")
        
        # Convert input
        net = float(input_value)

        # Checks for non-negative
        if net < 0:
            raise ValueError("Net value must be non-negative.")
        
        # Upper limit:
        if net > 1000000000:
            raise ValueError("Net value must be less than £1b.")
        
        # Calc
        result = net * 1.2

        # Update entry
        net_entry.delete(0, tk.END)
        net_entry.insert(0, f"£{result:.2f}")

    except ValueError as e:
        error_label.config(text=str(e))

def remove_vat():
    try:
        # Retrieve and clean input
        input_value = net_entry.get().strip().replace("£", "")

        # Check for empty input
        if not input_value:
            raise ValueError("Input must not be empty.")
        
        # Check for leading zeroes
        if input_value.startswith("0") and not input_value.startswith("0."):
            raise ValueError("Remove leading zeroes.")
        
        # Check for non-number
        if not input_value.replace(".", "", 1).isdigit():
            raise ValueError("Input must be a valid number.")

        # Check for decimal
        if not decimal(input_value):
            raise ValueError("Pence must be two decimals.")
        
        # Convert input
        gross = float(input_value)

        # Checks for non-negative
        if gross < 0:
            raise ValueError("Gross value must be non-negative.")
        
        # Upper limit:
        if gross > 1000000000:
            raise ValueError("Gross value must be less than £1b.")
        
        # Calc
        result = gross / 1.2

        # Update entry
        net_entry.delete(0, tk.END)
        net_entry.insert(0, f"£{result:.2f}")

    except ValueError as e:
        error_label.config(text=str(e))

# Button presses
def button_press(value):
    current_text = net_entry.get()

    if value == '.' and '.' in current_text:    # Don't allow 2 decimal points.
        return
    
    if '.' in current_text:    # Don't allow more than 2 decimal places.
        whole, decimal = current_text.split('.')
        if len(decimal) >= 2 and value != 'C':
            return
        
    if current_text == "£" and value == "C":    # Ignore £ sign being removed.
        clear()
        return
        
    if current_text == "£" and value == "C":    # Ensure £ sign stays at start.
        net_entry.insert(tk.END, value)
    else:
        net_entry.delete(0, tk.END)
        net_entry.insert(0, current_text + value)

# Keep £ sign
def keep_pound_sign(event=None):
    current_text = net_entry.get()

    if not current_text.startswith("£"):
        current_text = current_text.replace("£", "")
        net_entry.delete(0, tk.END)
        net_entry.insert(0, "£" + current_text)

    net_entry.icursor(tk.END)


# Clear entry
def clear():
    net_entry.delete(0, tk.END)
    net_entry.insert(0, "£")
    error_label.config(text="")



### GUI ###

# Main
if __name__ == "__main__":
    root = tk.Tk()
    root.title("VAT Calculator")

    # Window styling
    root.geometry("375x600")
    root.resizable(False, False)

    # Styling
    bg_colour = "#1e1e1e"
    fg_colour = "#f4f4f4"
    accent_colour = "#005a9e"
    entry_bg_colour = "#333333"
    button_colour = "#0078d7"

    title_font = tkfont.Font(family="Segoe UI", size=22)
    main_font = tkfont.Font(family="Segoe UI", size=12)
    result_font = tkfont.Font(family="Segoe UI", size=16)

    style = tkb.Style()
    style.theme_use('cosmo')
    style.configure("TFrame", background=bg_colour)
    style.configure("TLabel", background=bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TEntry", fieldbackground=entry_bg_colour, foreground=fg_colour, font=main_font)
    style.configure("TButton", background=button_colour, foreground=fg_colour, font=main_font)
    style.map("TButton", background=[('active', accent_colour)])

    # Configure main frame
    frame = tkb.Frame(root, padding="10")
    frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)
    frame.configure(border=0, relief="flat")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Header
    header_label = tkb.Label(frame, text="VAT Calculator", font=title_font, anchor=("center"))
    header_label.grid(column=0, row=0, columnspan=3, pady=(0, 20))

    # Input
    input_frame = tkb.Frame(frame)
    input_frame.grid(column=0, row=2, columnspan=3, pady=(0, 20), sticky=(tk.E, tk.W))
    net_entry = tkb.Entry(input_frame, justify="right", font=main_font, width=20)
    net_entry.grid(row=0, column=1, sticky=(tk.W))
    net_entry.insert(0, "£")

    # Error
    error_label = tkb.Label(frame, text="", font=main_font, foreground="red")
    error_label.grid(column=0, row=1, columnspan=3, ipady=15)

    # Numpad
    numpad_frame = tkb.Frame(frame)
    numpad_frame.grid(column=0, row=3, columnspan=3, pady=(20, 20))
    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), 
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), 
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), 
        ("C", 4, 0), ("0", 4, 1), (".", 4, 2), 
        ]

    for (text, row, col) in buttons:    # Loop to create each button
        action = lambda x=text: button_press(x) if x != 'C' else clear()
        tkb.Button(numpad_frame, text=text, command=action).grid(row=row, column=col, padx=5, pady=5, ipadx=15, ipady=10)


    add_vat_button = tkb.Button(frame, text="Add VAT (+)", width=10, command=add_vat)
    add_vat_button.grid(column=0, row=5, pady=(20, 20), padx=10, ipady=10, sticky=(tk.W, tk.E))

    minus_vat_button = tkb.Button(frame, text="Remove VAT (-)", width=10, command=remove_vat)
    minus_vat_button.grid(column=2, row=5, pady=(20, 20), padx=10, ipady=10, sticky=(tk.W, tk.E))

    # Grid
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.rowconfigure(1, weight=0)
    frame.rowconfigure(2, weight=0)
    input_frame.columnconfigure(0, weight=1)
    input_frame.columnconfigure(1, weight=0)
    input_frame.columnconfigure(2, weight=1)

    # Binds
    net_entry.bind("<KeyRelease>", keep_pound_sign)
    net_entry.bind("")

    # Event loop
    root.configure(bg=bg_colour)
    root.mainloop()