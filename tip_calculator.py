#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# tip_calculator.py

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

num_of_split = int(input("How many people to split the bill? "))

calculate_bill = bill * (1 + (tip/100)) / num_of_split

#A format of . 2f (note the f ) means to display the number with two digits after the decimal point

final_amount = "{:.2f}".format(calculate_bill, 2)

if tip == 10:
        print(f"Each person should pay: ${final_amount}")
elif tip == 12:
        print(f"Each person should pay: ${final_amount}")
else:
        print(f"Each person should pay: ${final_amount}")