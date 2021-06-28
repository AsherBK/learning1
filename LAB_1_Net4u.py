alafim = input("Enter the number of the alafim")
meot = input("Enter the number of the meot")
asarot = input("Enter the number of the asarot")
yehidot = input("Enter the number of the yehidot")

print("your whole number is...\n"+alafim + meot + asarot + yehidot)


print("And now...\nlet's try other trick...\n")
num = int(input("Enter here a number with 4 digits\n"))

print("Your thousand digit is "+str(num//1000)+"!")
print("Your hundred digit is "+str((num%1000)//100)+"!")
print("Your ten digit is "+str((num%100)//10)+"!")
print("And your one digit is "+str(num%10)+"!")