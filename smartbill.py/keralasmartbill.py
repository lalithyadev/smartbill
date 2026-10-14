print("="*50)
print (("KERALA FRESH MART".center(50)))
print (("SMART BILING".center(50)))
print("="*50)

customerName=input("customer name:")
itemname=input("item name:")
quantity=int(input("quantity:"))
Priceperunit=int(input("Price per unit(Rs:)"))
loyaltymember=input("loyalty member:(y/n):").lower()
paymentMode=input("paymentmode:(upi,cash/card):").lower()


amount=quantity*Priceperunit

if(amount>=2000):
  discount_rate = 10
elif(amount>=1000 and amount>=2000):
  discount_rate=5
elif (amount>=500 and amount>=1000):
  discount_rate=2
elif(amount>=500):
    discount_rate=0
else:
  discount_rate=0

discount=amount*discount_rate/100

loyalty_bonus=0
if loyalty_bonus =="y"and amount>=500:
  bonus=25


taxable_amount=amount-discount-loyalty_bonus
Gst=taxable_amount*5/100
grand_total=taxable_amount+Gst

print(f"{'Customername:':<40}{customerName:>10}")
print("-"*50)
print(f"{'item':<15}{'qty':>10}{'price':>10}{'amount':>10}")
print("-"*50)
print(f"{'Amount:':<40}{amount:>10.2f}")
print(f"{'discount Rate:':<40}{discount_rate:>10.2f}")
print(f"{'Loyalty Bonus:':<40}{loyalty_bonus:>10.2f}")
print(f"{'Taxable Amount:':<40}{taxable_amount:>10.2f}")
print(f"{'GST:':<40}{Gst:>10.2f}")
print(f"{'GrandTotal:':<40}{grand_total:>10.2f}")
print("="*50)


if quantity%12==0:
  bag="yes"
else:
  bag="no"

if bag=="yes":
  print(f"Bonus: free cloth bag with this order!")
if paymentMode=="cash"and grand_total>10000:
  print(f"Refused: pay by UPI or card")
elif paymentMode=="cash"or paymentMode=="upi"or paymentMode=="card":
  print(f"Payment accepted"),paymentMode.upper()
else:
  print(f"Invalid payment mode")
