print("\n------------------------------------------\nD I C T I O N A R Y    E X E R C I S E S\n------------------------------------------\n\n")

dict1 = {"Avi":20000, "Gadi":100000, "Ben":52590, "Sivan":31247, "Dudu":43750}
print("my first dictionary in python is "+str(dict1)+".\n")
print("And now let's sum the money of Avi & Dudu:")
print(dict1["Avi"]+dict1["Dudu"])

print("\nAnd now, let's append Yosi with the total sum of Avi & Dudu: ")
dict1["Yosi"]=dict1["Avi"] + dict1["Dudu"]
print(dict1)

print("\nThe number of the entries is "+ str(len(dict1)) + ".\n")

print("Let's check if \"Idan\" is insided our dictionary:")
print("idan" in dict1)