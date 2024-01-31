item_taken= input("what have you bought; ") 
item_price= input("price of the item; ")
quantity_taken= input("how many items have you bought; ")
total_amount= int(item_price)*int(quantity_taken)
print(f"Amount; {total_amount}")

birth_date= int(input("which year were you born; "))
current_date= int(input("which year are we in; "))
age= current_date - birth_date
print(age)