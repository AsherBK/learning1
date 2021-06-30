from time import sleep

print("................\nW E L C O M E !\n................\n\n")
sleep(2)

print("""----MENU-----
1. Insert a number and power it by 3
2. Insert 4 IPs to a list and print it
3. Insert 4 entries to DNS_dictioanary and print it
4. Check if a string is Polindrom
""")
sleep(0.5)
print("Waiting for your choose...")
choose = int(input())
if (choose==1):
            num1 = int(input("\ninsert here your number"))
            sleep(1.5)
            print("\nYour number power 3 is: " +str(pow(num1, 3)))
elif (choose==2):
            print("\ninsert here IPs:\n")
            ip_list = []
            print(ip_list.append(input("Enter new IP")))
            print(ip_list.append(input("Enter new IP")))
            print(ip_list.append(input("Enter new IP")))
            print(ip_list.append(input("Enter new IP")))
            print("\nProccessing...")
            sleep(2)
            print("\nYour IP list is: \n"+str(ip_list))
elif (choose==3):
            print("\nProccesing your DNS dictioanary...\n")
            sleep(0.5)
            DNS_list = {}
            DNS_list.update({input("Enter new URL"): input("Enter new IP")})
            DNS_list.update({input("Enter new URL"): input("Enter new IP")})
            DNS_list.update({input("Enter new URL"): input("Enter new IP")})
            DNS_list.update({input("Enter new URL"): input("Enter new IP")})
            print("\nYour DNS dictioanary is: \n"+ str(DNS_list))
elif (choose==4):
            poli = input("\nEnter here your string, and let's check if it's polindrom:")
            print("Procceessing...")
            sleep(0.7)
            if (poli==poli[::-1]):
                        print("\nIT IS POLINDROM!!")
            else:
                        print("\nToo bad... it is not a polindrom...")
else:
            print("\nEnter only 1-4!!")
