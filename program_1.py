# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.
#programmer:Devin Goshaw 
#date:10/16/25
#program: Rainfall program 

months=[
    "january", "Febuary", "March", "April", "May", "June", "July", "Agust", "September", "October", "November", "December"
]
rainfall=[]
for month in months:
    amount= float(input('Enter the total rainfall for ' + month +':'))
    rainfall.append(amount)

total_Rain=sum(rainfall)
average_Rain=total_Rain/12

max_Rain=max(rainfall)
min_Rain=min(rainfall)
max_Month=months[rainfall.index(max_Rain)]
min_Month=months[rainfall.index(min_Rain)]

print("\n Rainfall Statistics ")
print("Total rainfall for the year: ", round(total_Rain, 2), "inches")
print("Average monthly rainfall: ", round(average_Rain, 2), "inches")
print("largest amount rainfall: ", max_Month, "=", round(max_Rain, 2), "inches ")
print("minimum amount of rainfall: ", min_Month, "=", round(min_Rain, 2), "inches ")