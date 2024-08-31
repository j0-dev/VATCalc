


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


# Test
if __name__ == "__main__":
    net = float(input("Net amount (excluding VAT): £"))
    print(f"Gross amount (including VAT): £{gross:.2f}")


# x = int(input("Net amount (Excluding VAT(£)): "))

# result = vat(x)
# print(f"The gross amount (Including VAT(£)): {result:.2f}")