unit = int(input("Enter Electricity units:"))

if unit <= 100:
    bill = unit*5

elif unit<=300:
    bill = 100*5+(unit-100)*7

else: 
    bill = 100*5+200*7+(unit-300)*10

gst = bill*0.18
total = bill+gst
print("bill amount",bill)
print("gst",round(gst,2))
print("total bill",round(total,2))
