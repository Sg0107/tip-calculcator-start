#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_amt = float(input("Enter the Bill Amount: "))
tip_amt = float(input("Enter the Tip Amount in percent: "))
split_no = float(input("Enter the No. of persons: "))
amt_paid = (bill_amt / split_no) * (1 + tip_amt / 100)
amt_paid = round(amt_paid, 2)
print(format(amt_paid, '.4f'))
