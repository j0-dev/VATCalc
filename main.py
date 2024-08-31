


######################
### VAT CALCULATOR ###
######################



### FUNCTIONS ### 

# VAT calculation function
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
        _, pence = value.split(".")
        return len(pence) <= max
    except ValueError:
        return True
    
# Calculation and error handling
def calc(event=None):
    try:
        # Retrieve input (!update for GUI later)
        net = int(input("Net amount (excluding VAT): £"))

        # Check for decimal
        if not decimal(net):
            raise ValueError("Pence amount should not have more than two decimal places.")
        
        # Convert input (!for later)
        net = float(net)

        # Checks for non-negative
        if net < 0:
            raise ValueError("Net value must be non-negative.")
        
        # Upper limit:
        if net > 1000000000:
            raise ValueError("Net value must be less than £1b.")
        
        # Calculation proper
        result = vat(net)
        print(f"Gross amount (including VAT): £{result:.2f}")

    except ValueError as error:
        print(f"Error: {error}")
