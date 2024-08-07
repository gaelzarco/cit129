###
# Name: Gael Zarco
# Course and Section: CIT 129 - 1002 - 1003
# Date of Completion: 07/16/24
# Time To Complete: 50 Minutes
# Purpose: Calculate and print report of sale and sale statistics for cusomter
###

company_name = input("Please enter the name of your company:")
# Program ends if company name is invalid
if company_name!= "CSN":
    print("Invalid company name!")    
else:
    # Retrieve items purchased
    items_purchased = float(input("Enter the number of items purchased:"))

    # Program ends if items_purchased is not a valid number
    if items_purchased <= 0:
        print("Items purchased must be greater than 0!")
    else:
        # Retrieving item price as float
        retail_value = float(input("Enter the price of the item:"))
        # Retrieve tax rate and convert to decimal to streamline operations
        tax_rate = float(input("Enter the tax rate:")) * 0.01
        # Total cost before discounts and tax
        subtotal = retail_value * items_purchased
        # Amount of tax
        tax = subtotal * tax_rate

        # Calculate shipping cost based on items purchased
        if items_purchased >= 50:
            shipping = 0
        else:
            shipping = 35

        # Calculate discount rate based on items purchased
        if items_purchased >= 10 and items_purchased <= 19:
            discount_rate = .1
        elif items_purchased >= 20 and items_purchased <= 39:
            discount_rate = .15
        elif items_purchased >= 40 and items_purchased <= 79:
            discount_rate = .2
        elif items_purchased >= 80 and items_purchased <= 99:
            discount_rate = .25
        elif items_purchased >= 100:
            discount_rate = .3
        else:
            # Default rate is items purchased is less than 10
            discount_rate = 0

        # Calculate the amount saved after taxes
        discount = subtotal * discount_rate            
        # Calculate the grand total
        total = (subtotal + tax + shipping) - discount
         
        # Print relevant values, ensuring to format string appropriately
        print("\n\nCompany Name:", company_name)
        print("Number of items sold:", format(items_purchased, '.0f'))
        print("Unit Price: $", format(retail_value, '.2f'), sep="")
        print("Cost before discount and tax: $", format(subtotal, '.2f'), sep="")
        print("Tax Amount: $", format(tax, '.2f'), sep="")
        print("Shipping Amount: $", format(shipping, '.2f'), sep="")
        print("Amount Discounted: $", format(discount, '.2f'), sep="")
        print("Total: $", format(total, '.2f'), sep="")
