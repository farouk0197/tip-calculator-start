#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip Calculator ")
bill = float(input("What was the bill? "))
people = float(input("How many people to split the bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))/100 +1
#Each person should pay (150.00 / 5) * 1.12 = 33.6
total = str(round((bill/people) * tip,2))

#Format the result to 2 decimal places = 33.60
print("Each person should pay: "+total)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇