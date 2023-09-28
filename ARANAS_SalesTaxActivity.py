# Allow user to enter purchase amount
Purchase_Amount = float(input("Enter Purchase Amount: "))

Sales_Tax = Purchase_Amount * 0.06

# Display sales tax with two decimal digits after decimal points
print("Sales tax: ", round(Sales_Tax, 2))