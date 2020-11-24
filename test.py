
user_input1 = input("Please choose your state - CA, MN or NY.")
state = user_input1
user_input2 = int(input("Please state your purchase amount:"))
purchase_amount = user_input2


if state == "CA":
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from " + state + ", your total cost is "+str(total_cost)

elif state == "MN":
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from " + state + ", your total cost is "+str(total_cost)

elif state == "NY":
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from " + state + ", your total cost is "+str(total_cost)

else:
    result= "Please pick from one of 3 states provided"
    
print(result)