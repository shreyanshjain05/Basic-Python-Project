#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calculator")
total_bill=float (input ("enter the total bill amount \n $"))
number_of_people=float (input("enter number of people \n"))
percentage_of_tip= float (input("enter the percentage of tip you will to give \n "))
final_bill_after_tip=float (total_bill+total_bill*(percentage_of_tip/100))
bill_per_head=round(final_bill_after_tip/number_of_people,2)
# for input 150,5 and 12 output is 33.6 not 33.60
#so for 33.60 we'll use format specifier
bill_per_head= format(bill_per_head, ".2f") #so we used fomat specifier
print(f"bill per head is ${bill_per_head} ")
