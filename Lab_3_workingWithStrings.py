name = "ben"
mail = "aaa@gmail.com"
age = int("28")

print("My name is: " + name +"\nMy mail is: "+ mail +"\nMy age is: "+ str(age)+".")

print("My reverse name is: "+ name[::-1]+ "\nMy age now is double 3 so it is: "+ str(age*3))
print("\nAnd, now let's check if my name is in the next list:\nidan ben dudu yuval shimon yael gal adam shahar yana\n\nTrue/false:")
print(name in "idan ben dudu yuval shimon yael gal adam shahar yana")