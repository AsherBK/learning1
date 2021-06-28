tomatoPrice = 3
cucumberPrice = 2
chickenPrice = 20
colaPrice = 5

print("\n-----------------------------------\nWELCOME TO OUR MARKETING APP!!\n-----------------------------------\n")
print("M E N U :\ntomatoes (1 kilo) ---------------3")
print("Cucumbers (1 kilo) --------------2")
print("Chicken (1 kilo) --------------20")
print("Cola (1 bottle) --------------2")

tomatoQuan = int(input("Enter here how many kilos of tomatoes you buy:\n"))
cucumberQuan = int(input("Enter here how many kilos of cucumbers you buy:\n"))
chickenQuan = int(input("Enter here how many kilos of chicken you buy:\n"))
colaQuan = int(input("Enter here how many bottles of cola you buy:\n"))

totalTomato = tomatoPrice*tomatoQuan
totalCucumber = cucumberPrice*cucumberQuan
totalChicken = chickenPrice*chickenQuan
totalCola = colaPrice*colaQuan
tax = 0.17*(totalTomato+totalCucumber+totalChicken+totalCola)

print("And your bill is:\n------------------------------\n\n")
print("total price of tomatows is "+str(totalTomato)+".\n")
print("total price of cucumbers is "+str(totalCucumber)+".\n")
print("total price of chicken is "+str(totalChicken)+".\n")
print("total price of cola bottles is "+str(totalCola)+".\n-------------------------------\n")
print("Total payment before tax is "+str(totalTomato+totalCucumber+totalChicken+totalCola)+".\n\n")
print("TOTAL PAYMENT IS "+str(tax+totalTomato+totalCucumber+totalChicken+totalCola)+".\n------------------------------------\n")
print("HAVE A NICE DAY!!")