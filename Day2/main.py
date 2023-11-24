print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
amout_of_people = int(input("How many people split the bill? " ))
with_tip = total_bill*tip_percentage/100+total_bill
with_tip /= amout_of_people
final_amout = "{:.2f}".format(with_tip)
print(f"Each person should pay: ${final_amout}")

