#Jessica Alexander
#Tip Program
#05/13/2019

billAmt = 0.0
tipAmt = 0.0
tipPercent = 0.0

billAmt = float(input('Enter the amount of the bill: '))
tipPercent = float(input('Enter the tip percent: '))

tipAmt = billAmt* (tipPercent/100)
print("Your tip based on your tipPercent  is ", tipAmt)
totalBill = billAmt + tipAmt
print("Your totalBill based on your tip is ", totalBill)

