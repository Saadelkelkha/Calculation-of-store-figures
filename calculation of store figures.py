ma=int(input("enter the purchase amount :"))
TVA=int(input("enter the VAT value :"))
print("the amount of the discount is :",(ma/100)*3)
print("the tax is :",(ma/100)*TVA)
print("the amount to be paid is :",ma+(ma/100)*TVA-(ma/100)*3 )