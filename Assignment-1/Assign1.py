# Assignment #1 - Juan Espinal Comp Sci 1026 A
# Oct 6th, 2021 - This program computes the total electricity cost based on
#                 the kwh usage of the user input - applying appropriate discounts.


# Rates of Electricity + Taxes
OFF_PEAK_RATE = 0.085
PEAK_RATE = 0.176
MID_PEAK_RATE = 0.119
TAX_RATE = 1.13
# Priming Read
offPeak = float(input("Enter kwh during Off Peak Period: "))
# Loop that asks for user input until 0 is an input
while offPeak != 0:
    # prompts user input
    onPeak = float(input("Enter kwh during On Peak Period: "))
    midPeak = float(input("Enter kwh during Mid Peak Period: "))
    senior = (input("Is owner Senior? (y,n): ")).upper()

    # Resets the variables
    discount = 1.0
    check = False
    #  computes total power usage
    totalUsage = offPeak + onPeak + midPeak

    # Applies discount based on user input
    if totalUsage < 400:
        discount = discount - 0.04
        check = True

    if onPeak < 150 and check == False:
        onPeak = onPeak * 0.95  # Applies the 5 % discount

    if senior == "Y":
        discount = discount - 0.11

    # computes the Electricity cost before taxes
    beforeTax = (offPeak * OFF_PEAK_RATE) + (onPeak * PEAK_RATE) + (midPeak * MID_PEAK_RATE)

    # Applies discount
    beforeTax = beforeTax * discount
    # Computes the total discount
    totalCost = beforeTax * TAX_RATE

    # prints the Electricity Cost
    print("Electricity Cost: $%.2f " % totalCost)
    print("\n")
    # Modification read
    offPeak = float(input("Enter kwh during Off Peak Period: "))




